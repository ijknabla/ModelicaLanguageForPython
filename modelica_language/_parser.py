__all__ = ("Parser",)

from arpeggio import (
    Combine,
    CrossRef,
    EndOfFile,
    Not,
    OneOrMore,
    Optional,
    OrderedChoice,
    PTNodeVisitor,
    ParseTreeNode,
    Parser as ArpeggioParser,
    ParserPython as ArpeggioPythonParser,
    ParsingExpression,
    RegExMatch,
    Sequence,
    StrMatch,
    ZeroOrMore,
    visit_parse_tree,
)
from copy import copy
from typing import (
    Set,
    Any,
    List,
    MutableMapping,
    Optional as NoneOr,
    Tuple,
    Union,
)
from typing_extensions import Final
import warnings

from .exceptions import ParserWarning, SemanticError


ParsingExpressionLike = Union[ParsingExpression, CrossRef]


# ## Lexical symbols & keywords
LEXICAL_ASSIGNMENT_OPERATOR: Final[List[str]] = ["=", "|="]
SYNTAX_ASSIGNMENT_OPERATOR: Final[List[str]] = [":", "|:"]
NOT_OPERATOR: Final[str] = "!"
OR_OPERATOR: Final[str] = "|"

KEYWORD_RULE_NAME: Final[str] = "$KEYWORD"
COMMENT_RULE_NAME: Final[str] = "$COMMENT"
EOF_RULE_NAME: Final[str] = "$EOF"


# ## Lexical rules
def KEYWORD() -> RegExMatch:
    return RegExMatch("`[a-z]+`")


def TEXT() -> RegExMatch:
    return RegExMatch(r'"[^"]*"+')


def REGEX() -> RegExMatch:
    return RegExMatch(r"""r'[^'\\]*(?:\\.[^'\\]*)*'""")


def LEXICAL_RULE_IDENTIFIER() -> RegExMatch:
    return RegExMatch("[A-Z]([0-9A-Z]|-)*")


def LEXICAL_RULE_REFERENCE() -> ParsingExpression:
    return Sequence(
        OrderedChoice([LEXICAL_RULE_IDENTIFIER, KEYWORD_RULE_NAME]),
        Not(LEXICAL_ASSIGNMENT_OPERATOR),
    )


def SYNTAX_RULE_IDENTIFIER() -> RegExMatch:
    return RegExMatch("[a-z]([0-9a-z]|-)*")


def WORD_REFERENCE() -> ParsingExpression:
    return Sequence(LEXICAL_RULE_IDENTIFIER, Not(LEXICAL_ASSIGNMENT_OPERATOR))


def SYNTAX_REFERENCE() -> ParsingExpression:
    return OrderedChoice(
        [
            Sequence(SYNTAX_RULE_IDENTIFIER, Not(SYNTAX_ASSIGNMENT_OPERATOR)),
            EOF_RULE_NAME,
        ]
    )


# ## Syntax rules
def grammar() -> ParsingExpression:
    return Sequence(OneOrMore([lexical_rule, syntax_rule]), EndOfFile())


def lexical_rule() -> ParsingExpression:
    # In the lexical rule, the special rules
    # $KEYWORD and $COMMENT can be defined.
    # However, $EOF cannot be defined.
    return Sequence(
        OrderedChoice(
            [
                KEYWORD_RULE_NAME,
                COMMENT_RULE_NAME,
                LEXICAL_RULE_IDENTIFIER,
            ]
        ),
        LEXICAL_ASSIGNMENT_OPERATOR,
        lexical_expression,
    )


def syntax_rule() -> ParsingExpression:
    return Sequence(
        SYNTAX_RULE_IDENTIFIER,
        SYNTAX_ASSIGNMENT_OPERATOR,
        syntax_expression,
    )


# ## expression rule
def lexical_expression() -> ParsingExpression:
    return Sequence(
        lexical_ordered_choice,
    )


def lexical_ordered_choice() -> ParsingExpression:
    return OneOrMore(
        (Not(LEXICAL_ASSIGNMENT_OPERATOR), lexical_sequence),
        sep=OR_OPERATOR,
    )


def lexical_sequence() -> ParsingExpression:
    return OneOrMore(lexical_quantity)


def lexical_quantity() -> ParsingExpression:
    return OrderedChoice(
        [
            Sequence("[", lexical_expression, "]"),
            Sequence("{", lexical_expression, "}"),
            lexical_term,
        ]
    )


def lexical_term() -> ParsingExpression:
    return Sequence(Optional(NOT_OPERATOR), lexical_primary)


def lexical_primary() -> ParsingExpression:
    return OrderedChoice(
        [
            Sequence("(", lexical_expression, ")"),
            KEYWORD,
            TEXT,
            REGEX,
            LEXICAL_RULE_REFERENCE,
        ]
    )


def syntax_expression() -> ParsingExpression:
    return Sequence(
        syntax_ordered_choice,
    )


def syntax_ordered_choice() -> ParsingExpression:
    return OneOrMore(syntax_sequence, sep=OR_OPERATOR)


def syntax_sequence() -> ParsingExpression:
    return OneOrMore(syntax_quantity)


def syntax_quantity() -> ParsingExpression:
    return OrderedChoice(
        [
            Sequence("[", syntax_expression, "]"),
            Sequence("{", syntax_expression, "}"),
            syntax_primary,
        ]
    )


def syntax_primary() -> ParsingExpression:
    return OrderedChoice(
        [
            Sequence("(", syntax_expression, ")"),
            KEYWORD,
            TEXT,
            WORD_REFERENCE,
            SYNTAX_REFERENCE,
        ]
    )


# ## Comment rule
def comment() -> ParsingExpression:
    return OrderedChoice(
        [
            RegExMatch(r"//.*"),
            RegExMatch(r"/\*([^*]|\*[^/])*\*/"),
        ]
    )


class GrammarVisitor(PTNodeVisitor):
    __root_rule_name: str
    __comment_rule_name: str
    __ignore_case: bool
    __rules: MutableMapping[str, ParsingExpressionLike]

    __DEFAULT_RULES = {
        EOF_RULE_NAME: EndOfFile(),
    }

    def __init__(
        self,
        root_rule_name: str,
        comment_rule_name: str,
        ignore_case: bool,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.__root_rule_name = root_rule_name
        self.__comment_rule_name = comment_rule_name
        self.__ignore_case = ignore_case
        self.__rules = dict(self.__DEFAULT_RULES)

    @property
    def __skipws(self) -> RegExMatch:
        skipws = RegExMatch(r"\s*")
        skipws.compile()
        return skipws

    def visit_KEYWORD(self, node: Any, children: Any) -> Any:
        match = RegExMatch(
            rf"{node.value[1:-1]}(?![0-9_a-zA-Z])",
            ignore_case=self.__ignore_case,
        )
        match.compile()
        return match

    def visit_TEXT(self, node: Any, children: Any) -> Any:
        return StrMatch(node.value[1:-1], ignore_case=self.__ignore_case)

    def visit_REGEX(self, node: Any, children: Any) -> Any:
        match = RegExMatch(node.value[2:-1], ignore_case=self.__ignore_case)
        match.compile()
        return match

    def __visit_REFERENCE(self, node: Any, children: Any) -> Any:
        return CrossRef(node.value)

    visit_LEXICAL_RULE_REFERENCE = __visit_REFERENCE

    def visit_WORD_REFERENCE(self, node: Any, children: Any) -> Any:
        crossref = self.__visit_REFERENCE(node, children)
        return Sequence(nodes=[self.__skipws, crossref])

    visit_SYNTAX_REFERENCE = __visit_REFERENCE

    def visit_lexical_term(self, node: Any, children: Any) -> Any:
        if len(children) == 2:
            operator, child = children
        else:
            operator, (child,) = None, children

        if operator is None:
            return child
        elif operator == "!":
            return Not(nodes=[child])

        raise NotImplementedError()

    def __visit_quantity(self, node: Any, children: Any) -> Any:
        (child,) = children
        try:
            L, _, R = node
        except ValueError:
            L, R = None, None

        if (L, R) == (None, None):
            return child
        elif (L, R) == ("[", "]"):
            return Optional(nodes=[child])
        elif (L, R) == ("{", "}"):
            return ZeroOrMore(nodes=[child])
        raise NotImplementedError()

    visit_lexical_quantity = __visit_quantity
    visit_syntax_quantity = __visit_quantity

    def __visit_sequence(self, node: Any, children: Any) -> Any:
        head, *tail = children
        if not tail:
            return head
        else:
            return Sequence(nodes=[head, *tail])

    def visit_lexical_sequence(self, node: Any, children: Any) -> Any:
        return Combine(nodes=self.__visit_sequence(node, children))

    visit_syntax_sequence = __visit_sequence

    def __visit_ordered_choice(self, node: Any, children: Any) -> Any:
        head, *tail = (
            child
            for child in children
            if isinstance(child, (ParsingExpression, CrossRef))
        )
        if not tail:
            return head
        else:
            return OrderedChoice(nodes=[head, *tail])

    visit_lexical_ordered_choice = __visit_ordered_choice
    visit_syntax_ordered_choice = __visit_ordered_choice

    def __visit_rule(self, node: Any, children: Any) -> Any:
        rule_name, operator, new_rule = children

        if operator in {"=", ":"}:
            rule = new_rule
        elif operator in {"|=", "|:"}:
            try:
                previous_rule = self.__rules[rule_name]
            except KeyError as keyError:
                raise SemanticError(
                    f'Rule "{rule_name}" does not exists.'
                ) from keyError
            rule = OrderedChoice(nodes=[previous_rule, new_rule])
        else:
            raise NotImplementedError()

        # Keep a map of parser rules for cross reference
        # resolving.
        rule.rule_name = rule_name
        rule.root = True
        self.__rules[rule_name] = rule
        return rule

    visit_lexical_rule = __visit_rule
    visit_syntax_rule = __visit_rule

    def visit_grammar(
        self, node: Any, children: Any
    ) -> Tuple[ParsingExpression, NoneOr[ParsingExpression]]:
        resolved: Set[ParsingExpressionLike] = set()

        def _resolve(
            node: ParsingExpressionLike,
        ) -> ParsingExpression:
            """
            Resolves CrossRefs from the parser model.
            """

            if node in resolved:
                # Why? : The rule already included in `resolved`
                # has been determined to be ParsingExpression.
                assert isinstance(node, ParsingExpression)
                return node
            resolved.add(node)

            def get_rule_by_name(rule_name: str) -> ParsingExpressionLike:
                try:
                    return self.__rules[rule_name]
                except KeyError:
                    raise SemanticError(
                        'Rule "{}" does not exists.'.format(rule_name)
                    )

            def resolve_rule_by_name(
                rule_name: str,
            ) -> ParsingExpression:

                if self.debug:
                    self.dprint("Resolving crossref {}".format(rule_name))

                resolved_rule = get_rule_by_name(rule_name)
                while isinstance(resolved_rule, CrossRef):
                    target_rule = resolved_rule.target_rule_name
                    resolved_rule = get_rule_by_name(target_rule)

                # If resolved rule hasn't got the same name it
                # should be cloned and preserved in the peg_rules cache
                if resolved_rule.rule_name != rule_name:
                    resolved_rule = copy(resolved_rule)
                    resolved_rule.rule_name = rule_name
                    self.__rules[rule_name] = resolved_rule
                    if self.debug:
                        self.dprint(
                            "Resolving: cloned to {} = > {}".format(
                                resolved_rule.rule_name, resolved_rule.name
                            )
                        )
                return resolved_rule

            if isinstance(node, CrossRef):
                # The root rule is a cross-ref
                resolved_rule = resolve_rule_by_name(node.target_rule_name)
                return _resolve(resolved_rule)
            else:
                # Resolve children nodes
                for i, n in enumerate(node.nodes):
                    node.nodes[i] = _resolve(n)
                resolved.add(node)
                return node

        # Find root and comment rules
        root_rule, comment_rule = None, None
        for rule in children:
            if rule.rule_name == self.__root_rule_name:
                root_rule = _resolve(rule)
            if rule.rule_name == self.__comment_rule_name:
                comment_rule = _resolve(rule)

        if root_rule is None:
            raise SemanticError("Root rule not found!")
        return root_rule, comment_rule


class Parser(ArpeggioParser):
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

        super().__init__(*args, **kwargs)
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

    def _parse(self) -> ParseTreeNode:
        return self.parser_model.parse(self)

    def _from_peg(
        self, language_def: str
    ) -> Tuple[ParsingExpression, NoneOr[ParsingExpression]]:
        parser = ArpeggioPythonParser(
            grammar, comment, reduce_tree=False, debug=self.debug
        )
        parse_tree = parser.parse(language_def)

        return visit_parse_tree(  # type: ignore
            parse_tree,
            GrammarVisitor(
                self.root_rule_name,
                self.comment_rule_name,
                self.ignore_case,
                debug=self.debug,
            ),
        )
