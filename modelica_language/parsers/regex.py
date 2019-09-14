
__all__ = (
    # quote character
    "single_quote", "double_quote",
    # character set
    "s_char", "q_char", "s_escape", "digit", "nondigit",
    # lexical unit
    "string", "unsigned_integer", "unsigned_number",
    "q_ident", "ident",
    # comment
    "single_line_comment", "multi_line_comment",
    "cpp_style_comment",
)


# # regex for quote character

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
