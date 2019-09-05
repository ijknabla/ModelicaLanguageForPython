
__all__ = (
    "IDENT", "STRING", "UNSIGNED_NUMBER",
    "CPP_STYLE_COMMENT",
)

from arpeggio import RegExMatch, Not
from .. import syntax

single_quote = "'"
double_quote = '"'


# # regex for lexical unit STRING

s_char = rf'[^\\{double_quote}]'
# any member of the Unicode character set
# except double-quote """, and backslash "\"

s_escape = (
    rf'\\{single_quote}|\\{double_quote}|'
    r'\\\?|\\\\|\\a|\\b|\\f|\\n|\\r|\\t|\\v'
)

string = (
    rf'{double_quote}'
    rf'({s_char}|{s_escape})*'
    rf'{double_quote}'
)


# # regex for lexical unit UNSIGNED_NUMBER

digit = r'[0-9]'
nondigit = r'_|[a-z]|[A-Z]'

unsigned_integer = rf'({digit})+'
unsigned_number = (
    rf'{unsigned_integer}(\.({unsigned_integer})?)?'
    rf'([eE][+-]?{unsigned_integer})?'
)


# # regex for lexical unit IDENT

q_char = (
    rf'{nondigit}|{digit}'
    r'|!|#|\$|%|&|\(|\)|\*|\+|,|-|\.|/|'
    r':|;|<|>|=|\?|@|\[|\]|\^|{|}|\||~| '
)
q_ident = (
    rf'{single_quote}'
    rf'({q_char}|{s_escape})'
    rf'({q_char}|{s_escape}|{double_quote})*'
    rf'{single_quote}'
)
ident = rf'(({nondigit})({digit}|{nondigit})*)|({q_ident})'


# # regex for lexical unit C++ style comment

single_line_comment = r'//.*'
multi_line_comment = r'/\*([^*]|\*(?!/))*\*/'
cpp_style_comment = rf'({single_line_comment})|({multi_line_comment})'


def IDENT(): return Not(syntax.ANY_KEYWORD), RegExMatch(ident)
def STRING(): return RegExMatch(string)
def UNSIGNED_NUMBER(): return RegExMatch(unsigned_number)
def CPP_STYLE_COMMENT(): return RegExMatch(cpp_style_comment)


def regexPEG(regex: str) -> str:
    return "r'{}'".format(regex.replace("'", r"\'"))


IDENT.__doc__ = (
    f"IDENT = !ANY_KEYWORD {regexPEG(ident)}"
)
STRING.__doc__ = (
    f"STRING = {regexPEG(string)}"
)
UNSIGNED_NUMBER.__doc__ = (
    f"UNSIGNED_NUMBER = {regexPEG(unsigned_number)}"
)
CPP_STYLE_COMMENT.__doc__ = (
    f"CPP_STYLE_COMMENT = {regexPEG(cpp_style_comment)}"
)
