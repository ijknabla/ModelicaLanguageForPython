from arpeggio import EOF, Not, OneOrMore, Optional, RegExMatch, StrMatch
from arpeggio.peg import regex
from typing import Any

LEXICAL_ASSIGNMENT_OPERATOR = ["=", "|="]
SYNTAX_ASSIGNMENT_OPERATOR = [":", "|:"]
NOT_OPERATOR = "!"
OR_OPERATOR = "|"


# # lexical rules
def KEYWORD() -> RegExMatch:
    return RegExMatch("`[a-z]+`")


def TEXT() -> RegExMatch:
    return RegExMatch(r'"[^"]*"+')


def REGEX() -> Any:
    return regex


def KEYWORDS_RULE_NAME() -> StrMatch:
    return StrMatch("$KEYWORD")


def EOF_RULE_NAME() -> StrMatch:
    return StrMatch("$EOF")


def LEXICAL_RULE_NAME() -> RegExMatch:
    return RegExMatch("[A-Z]([0-9A-Z]|-)*")


def SYNTAX_RULE_NAME() -> RegExMatch:
    return RegExMatch("[a-z]([0-9a-z]|-)*")


# # grammar rule
def grammar() -> Any:
    return (
        OneOrMore(
            [
                keywords_assignment,
                lexical_assignment,
                syntax_assignment,
            ]
        ),
        EOF,
    )


def keywords_assignment() -> Any:
    return (
        KEYWORDS_RULE_NAME,
        LEXICAL_ASSIGNMENT_OPERATOR,
        keywords_expression,
    )


def lexical_assignment() -> Any:
    return (
        LEXICAL_RULE_NAME,
        LEXICAL_ASSIGNMENT_OPERATOR,
        lexical_expression,
    )


def syntax_assignment() -> Any:
    return (
        SYNTAX_RULE_NAME,
        SYNTAX_ASSIGNMENT_OPERATOR,
        syntax_expression,
    )


# ## expression rule
def keywords_expression() -> Any:
    return (keywords_ordered_choice,)


def keywords_ordered_choice() -> Any:
    return OneOrMore(KEYWORD, sep=OR_OPERATOR)


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
        lexical_rule_reference,
    ]


def lexical_rule_reference() -> Any:
    return [
        (KEYWORDS_RULE_NAME, Not(LEXICAL_ASSIGNMENT_OPERATOR)),
        (LEXICAL_RULE_NAME, Not(LEXICAL_ASSIGNMENT_OPERATOR)),
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
        syntax_rule_reference,
    ]


def syntax_rule_reference() -> Any:
    return [
        (LEXICAL_RULE_NAME, Not(LEXICAL_ASSIGNMENT_OPERATOR)),
        (SYNTAX_RULE_NAME, Not(SYNTAX_ASSIGNMENT_OPERATOR)),
        EOF_RULE_NAME,
    ]


# # comment rule
def comment() -> Any:
    return [
        RegExMatch(r"//.*"),
        RegExMatch(r"/\*([^*]|\*[^/])*\*/"),
    ]
