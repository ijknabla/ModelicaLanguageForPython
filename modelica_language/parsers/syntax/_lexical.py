
__all__ = (
    "IDENT", "STRING", "UNSIGNED_NUMBER",
    "CPP_STYLE_COMMENT",
)

from arpeggio import RegExMatch, Not
from .. import syntax
from .. import regex


def IDENT():
    return Not(syntax.ANY_KEYWORD), RegExMatch(regex.ident)


def STRING():
    return RegExMatch(regex.string)


def UNSIGNED_NUMBER():
    return RegExMatch(regex.unsigned_number)


def CPP_STYLE_COMMENT():
    return RegExMatch(regex.cpp_style_comment)


def regexPEG(regex: str) -> str:
    return "r'{}'".format(regex.replace("\'", r"\'"))


IDENT.__doc__ = (
    f"IDENT = !ANY_KEYWORD {regexPEG(regex.ident)}"
)
STRING.__doc__ = (
    f"STRING = {regexPEG(regex.string)}"
)
UNSIGNED_NUMBER.__doc__ = (
    f"UNSIGNED_NUMBER = {regexPEG(regex.unsigned_number)}"
)
CPP_STYLE_COMMENT.__doc__ = (
    f"CPP_STYLE_COMMENT = {regexPEG(regex.cpp_style_comment)}"
)
