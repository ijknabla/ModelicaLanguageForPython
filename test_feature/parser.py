__all__ = ("Parser",)

from arpeggio import (
    EOF,
    Not,
    OneOrMore,
    Optional,
    Parser as ArpeggioParser,
    RegExMatch,
)
from typing import Any, List
from typing_extensions import Final


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


def LEXICAL_RULE_REFERENCE() -> Any:
    return (
        [
            (LEXICAL_RULE_IDENTIFIER, Not(LEXICAL_ASSIGNMENT_OPERATOR)),
            (KEYWORD_RULE_NAME, Not(LEXICAL_ASSIGNMENT_OPERATOR)),
        ],
    )


def SYNTAX_RULE_IDENTIFIER() -> RegExMatch:
    return RegExMatch("[a-z]([0-9a-z]|-)*")


def SYNTAX_RULE_REFERENCE() -> Any:
    return [
        (LEXICAL_RULE_IDENTIFIER, Not(LEXICAL_ASSIGNMENT_OPERATOR)),
        (SYNTAX_RULE_IDENTIFIER, Not(SYNTAX_ASSIGNMENT_OPERATOR)),
        EOF_RULE_NAME,
    ]


# ## Syntax rules
def grammar() -> Any:
    return (OneOrMore([lexical_rule, syntax_rule]), EOF)


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
    return OneOrMore(
        (Not(LEXICAL_ASSIGNMENT_OPERATOR), lexical_sequence), sep=OR_OPERATOR
    )


def lexical_sequence() -> Any:
    return OneOrMore(lexical_quantity)


def lexical_quantity() -> Any:
    return [
        ("[", lexical_expression, "]"),
        ("{", lexical_expression, "}"),
        lexical_term,
    ]


def lexical_term() -> Any:
    return Optional(NOT_OPERATOR), lexical_primary


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
    return OneOrMore(syntax_sequence, sep=OR_OPERATOR)


def syntax_sequence() -> Any:
    return OneOrMore(syntax_quantity)


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
        RegExMatch(r"//.*"),
        RegExMatch(r"/\*([^*]|\*[^/])*\*/"),
    ]


class Parser(ArpeggioParser):
    ...
