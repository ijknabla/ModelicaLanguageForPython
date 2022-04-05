from arpeggio import EOF, OneOrMore, RegExMatch
from typing import Any


# lexical rules
def KEYWORD() -> RegExMatch:
    return RegExMatch("`[a-z]+`")


# grammar rules
def grammar() -> Any:
    return (
        OneOrMore(lexical_rule),
        EOF,
    )


def lexical_rule() -> Any:
    return [keywords_assignment]


def keywords_assignment() -> Any:
    return (
        "@KEYWORDS@",
        ["=", "|="],
        OneOrMore(KEYWORD, sep="|"),
    )


# comment rule
def comment() -> Any:
    return [
        RegExMatch(r"//.*"),
        RegExMatch(r"/\*([^*]|\*[^/])*\*/"),
    ]
