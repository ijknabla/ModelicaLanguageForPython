__all__ = ("Parser",)

import arpeggio
from typing import Any, List, Optional, Tuple
from typing_extensions import Final
import warnings

from .exceptions import ParserWarning


# ## Lexical symbols & keywords
LEXICAL_ASSIGNMENT_OPERATOR: Final[List[str]] = ["=", "|="]
SYNTAX_ASSIGNMENT_OPERATOR: Final[List[str]] = [":", "|:"]
NOT_OPERATOR: Final[str] = "!"
OR_OPERATOR: Final[str] = "|"

KEYWORD_RULE_NAME: Final[str] = "$KEYWORD"
COMMENT_RULE_NAME: Final[str] = "$COMMENT"
EOF_RULE_NAME: Final[str] = "$EOF"


# ## Lexical rules
def KEYWORD() -> arpeggio.RegExMatch:
    return arpeggio.RegExMatch("`[a-z]+`")


def TEXT() -> arpeggio.RegExMatch:
    return arpeggio.RegExMatch(r'"[^"]*"+')


def REGEX() -> arpeggio.RegExMatch:
    return arpeggio.RegExMatch(r"""r'[^'\\]*(?:\\.[^'\\]*)*'""")


def LEXICAL_RULE_IDENTIFIER() -> arpeggio.RegExMatch:
    return arpeggio.RegExMatch("[A-Z]([0-9A-Z]|-)*")


def LEXICAL_RULE_REFERENCE() -> Any:
    return (
        [
            (
                LEXICAL_RULE_IDENTIFIER,
                arpeggio.Not(LEXICAL_ASSIGNMENT_OPERATOR),
            ),
            (KEYWORD_RULE_NAME, arpeggio.Not(LEXICAL_ASSIGNMENT_OPERATOR)),
        ],
    )


def SYNTAX_RULE_IDENTIFIER() -> arpeggio.RegExMatch:
    return arpeggio.RegExMatch("[a-z]([0-9a-z]|-)*")


def SYNTAX_RULE_REFERENCE() -> Any:
    return [
        (LEXICAL_RULE_IDENTIFIER, arpeggio.Not(LEXICAL_ASSIGNMENT_OPERATOR)),
        (SYNTAX_RULE_IDENTIFIER, arpeggio.Not(SYNTAX_ASSIGNMENT_OPERATOR)),
        EOF_RULE_NAME,
    ]


# ## Syntax rules
def grammar() -> Any:
    return (arpeggio.OneOrMore([lexical_rule, syntax_rule]), arpeggio.EOF)


def lexical_rule() -> Any:
    # In the lexical rule, the special rules
    # $KEYWORD and $COMMENT can be defined.
    # However, $EOF cannot be defined.
    return (
        [
            KEYWORD_RULE_NAME,
            COMMENT_RULE_NAME,
            LEXICAL_RULE_IDENTIFIER,
        ],
        LEXICAL_ASSIGNMENT_OPERATOR,
        lexical_expression,
    )


def syntax_rule() -> Any:
    return (
        SYNTAX_RULE_IDENTIFIER,
        SYNTAX_ASSIGNMENT_OPERATOR,
        syntax_expression,
    )


# ## expression rule
def lexical_expression() -> Any:
    return (lexical_ordered_choice,)


def lexical_ordered_choice() -> Any:
    return arpeggio.OneOrMore(
        (arpeggio.Not(LEXICAL_ASSIGNMENT_OPERATOR), lexical_sequence),
        sep=OR_OPERATOR,
    )


def lexical_sequence() -> Any:
    return arpeggio.OneOrMore(lexical_quantity)


def lexical_quantity() -> Any:
    return [
        ("[", lexical_expression, "]"),
        ("{", lexical_expression, "}"),
        lexical_term,
    ]


def lexical_term() -> Any:
    return arpeggio.Optional(NOT_OPERATOR), lexical_primary


def lexical_primary() -> Any:
    return [
        ("(", lexical_expression, ")"),
        KEYWORD,
        TEXT,
        REGEX,
        LEXICAL_RULE_REFERENCE,
    ]


def syntax_expression() -> Any:
    return (syntax_ordered_choice,)


def syntax_ordered_choice() -> Any:
    return arpeggio.OneOrMore(syntax_sequence, sep=OR_OPERATOR)


def syntax_sequence() -> Any:
    return arpeggio.OneOrMore(syntax_quantity)


def syntax_quantity() -> Any:
    return [
        ("[", syntax_expression, "]"),
        ("{", syntax_expression, "}"),
        syntax_primary,
    ]


def syntax_primary() -> Any:
    return [
        ("(", syntax_expression, ")"),
        KEYWORD,
        TEXT,
        SYNTAX_RULE_REFERENCE,
    ]


# ## Comment rule
def comment() -> Any:
    return [
        arpeggio.RegExMatch(r"//.*"),
        arpeggio.RegExMatch(r"/\*([^*]|\*[^/])*\*/"),
    ]


class GrammarVisitor(
    arpeggio.PTNodeVisitor,  # type: ignore
):
    ...


class Parser(
    arpeggio.Parser,  # type: ignore
):
    def __init__(
        self,
        language_def: str,
        root_rule_name: str,
        comment_rule_name: str = COMMENT_RULE_NAME,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Constructs parser from textual PEG definition.

        Args:
            language_def (str): A string describing language grammar using
                PEG notation.
            root_rule_name(str): The name of the root rule.
            comment_rule_name(str): The name of the rule for comments.
        """

        ignore_case = kwargs.get("ignore_case", None)
        if ignore_case:
            warnings.warn(
                (
                    f"ignore_case is {ignore_case!r}\n"
                    "Modelica grammar should be Case sensitive."
                ),
                ParserWarning,
            )

        super().__init__(*args, ignore_case=ignore_case, **kwargs)
        self.root_rule_name = root_rule_name
        self.comment_rule_name = comment_rule_name

        # PEG Abstract Syntax Graph
        self.parser_model, self.comments_model = self._from_peg(language_def)
        # Comments should be optional and there can be more of them
        if self.comments_model:
            self.comments_model.root = True
            self.comments_model.rule_name = comment_rule_name

        # In debug mode export parser model to dot for
        # visualization
        if self.debug:
            from arpeggio.export import PMDOTExporter

            root_rule = self.parser_model.rule_name
            PMDOTExporter().exportFile(
                self.parser_model, "{}_peg_parser_model.dot".format(root_rule)
            )

    def _parse(self) -> Any:  # TODO check type
        return self.parser_model.parse(self)

    def _from_peg(
        self, language_def: str
    ) -> Tuple[
        arpeggio.ParsingExpression,
        Optional[arpeggio.ParsingExpression],
    ]:
        parser = arpeggio.ParserPython(
            grammar, comment, reduce_tree=False, debug=self.debug
        )
        parser.root_rule_name = self.root_rule_name
        parse_tree = parser.parse(language_def)

        return arpeggio.visit_parse_tree(  # type: ignore
            parse_tree,
            GrammarVisitor(
                self.root_rule_name,
                self.comment_rule_name,
                self.ignore_case,
                debug=self.debug,
            ),
        )
