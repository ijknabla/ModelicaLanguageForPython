from arpeggio import EOF, Not, OneOrMore, Optional, RegExMatch, StrMatch
from arpeggio.peg import regex
from typing import Any

LEXICAL_ASSIGNMENT_OPERATOR = ["=", "|="]
NOT_OPERATOR = "!"
OR_OPERATOR = "|"


# lexical rules
def KEYWORD() -> RegExMatch:
    return RegExMatch("`[a-z]+`")


def TEXT() -> RegExMatch:
    return RegExMatch(r'"[^"]*"+')


def REGEX() -> Any:
    return regex


def KEYWORDS_RULE_NAME() -> StrMatch:
    return StrMatch("@KEYWORDS@")


def LEXICAL_RULE_NAME() -> RegExMatch:
    return RegExMatch("[A-Z]([0-9A-Z]|-)*")


# grammar rules
def grammar() -> Any:
    return (
        OneOrMore(lexical_rule),
        EOF,
    )


def lexical_rule() -> Any:
    return [
        keywords_assignment,
        lexical_assignment,
    ]


def keywords_assignment() -> Any:
    return (
        KEYWORDS_RULE_NAME,
        LEXICAL_ASSIGNMENT_OPERATOR,
        OneOrMore(KEYWORD, sep=OR_OPERATOR),
    )


def lexical_assignment() -> Any:
    return (
        LEXICAL_RULE_NAME,
        LEXICAL_ASSIGNMENT_OPERATOR,
        lexical_expression,
    )


def lexical_expression() -> Any:
    return (lexical_ordered_choice,)


def lexical_ordered_choice() -> Any:
    return OneOrMore(lexical_sequence, sep=OR_OPERATOR)


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
        KEYWORDS_RULE_NAME,
        LEXICAL_RULE_NAME,
    ], Not(LEXICAL_ASSIGNMENT_OPERATOR)


# comment rule
def comment() -> Any:
    return [
        RegExMatch(r"//.*"),
        RegExMatch(r"/\*([^*]|\*[^/])*\*/"),
    ]
