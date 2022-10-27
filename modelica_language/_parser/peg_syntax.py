from typing import Callable, Sequence, Union

from arpeggio import (
    EndOfFile,
    Not,
    OneOrMore,
    Optional,
    ParsingExpression,
    RegExMatch,
)

ParsingExpressionLike__0 = Union[
    str, ParsingExpression, Callable[[], ParsingExpression]
]
ParsingExpressionLike__1 = Union[
    ParsingExpressionLike__0, Sequence[ParsingExpressionLike__0]
]
ParsingExpressionLike__2 = Union[
    ParsingExpressionLike__1, Sequence[ParsingExpressionLike__1]
]


ParsingExpressionLike = ParsingExpressionLike__2


def parsing_expression(
    syntax: Callable[[], ParsingExpressionLike]
) -> Callable[[], ParsingExpression]:
    return syntax  # type: ignore


# ## PEG lexical rules
@parsing_expression
def LEXICAL_ASSIGNMENT() -> ParsingExpressionLike:
    return "="


@parsing_expression
def LEXICAL_INPLACE_OR() -> ParsingExpressionLike:
    return "|="


@parsing_expression
def SYNTAX_ASSIGNMENT() -> ParsingExpressionLike:
    return ":"


@parsing_expression
def SYNTAX_INPLACE_OR() -> ParsingExpressionLike:
    return "|:"


@parsing_expression
def NOT() -> ParsingExpressionLike:
    return "!"


@parsing_expression
def OR() -> ParsingExpressionLike:
    return "|"


@parsing_expression
def OPEN_SQUARE_BRACKET() -> ParsingExpressionLike:
    return "["


@parsing_expression
def CLOSE_SQUARE_BRACKET() -> ParsingExpressionLike:
    return "]"


@parsing_expression
def OPEN_BRACE() -> ParsingExpressionLike:
    return "{"


@parsing_expression
def CLOSE_BRACE() -> ParsingExpressionLike:
    return "}"


@parsing_expression
def KEYWORD() -> ParsingExpressionLike:
    return RegExMatch("`[a-z]+`")


@parsing_expression
def TEXT() -> ParsingExpressionLike:
    return [
        RegExMatch(r"'([^']|'(?='))*'"),
        RegExMatch(r'"([^"]|"(?="))*"'),
    ]


@parsing_expression
def REGEX() -> ParsingExpressionLike:
    return [
        RegExMatch(r"r'([^'\\]|\\.)*'"),
        RegExMatch(r'r"([^"\\]|\\.)*"'),
    ]


@parsing_expression
def EOF_RULE() -> ParsingExpressionLike:
    return "$EOF"


@parsing_expression
def LEXICAL_RULE() -> ParsingExpressionLike:
    return Not(EOF_RULE), RegExMatch(r"\$?[A-Z]([0-9A-Z]|-)*")


@parsing_expression
def SYNTAX_RULE() -> ParsingExpressionLike:
    return RegExMatch("[a-z]([0-9a-z]|-)*")


# ## PEG syntax rules
@parsing_expression
def grammar() -> ParsingExpressionLike:
    return (
        OneOrMore([lexical_rule_statement, syntax_rule_statement]),
        EndOfFile(),
    )


@parsing_expression
def lexical_rule_statement() -> ParsingExpressionLike:
    return (
        LEXICAL_RULE,
        [LEXICAL_ASSIGNMENT, LEXICAL_INPLACE_OR],
        lexical_expression,
    )


@parsing_expression
def syntax_rule_statement() -> ParsingExpressionLike:
    return (
        SYNTAX_RULE,
        [SYNTAX_ASSIGNMENT, SYNTAX_INPLACE_OR],
        syntax_expression,
    )


# ## Lexical expression
@parsing_expression
def lexical_expression() -> ParsingExpressionLike:
    return (lexical_ordered_choice,)


@parsing_expression
def lexical_ordered_choice() -> ParsingExpressionLike:
    return OneOrMore(lexical_sequence, sep=OR)


@parsing_expression
def lexical_sequence() -> ParsingExpressionLike:
    return OneOrMore(lexical_quantity)


@parsing_expression
def lexical_quantity() -> ParsingExpressionLike:
    return [
        (OPEN_SQUARE_BRACKET, lexical_expression, CLOSE_SQUARE_BRACKET),
        (OPEN_BRACE, lexical_expression, CLOSE_BRACE),
        lexical_term,
    ]


@parsing_expression
def lexical_term() -> ParsingExpressionLike:
    return Optional(NOT), lexical_primary


@parsing_expression
def lexical_primary() -> ParsingExpressionLike:
    return [
        ("(", lexical_expression, ")"),
        LEXICAL_KEYWORD,
        LEXICAL_TEXT,
        LEXICAL_REGEX,
        lexical_reference,
    ]


@parsing_expression
def LEXICAL_KEYWORD() -> ParsingExpressionLike:
    return KEYWORD


@parsing_expression
def LEXICAL_TEXT() -> ParsingExpressionLike:
    return TEXT


@parsing_expression
def LEXICAL_REGEX() -> ParsingExpressionLike:
    return REGEX


@parsing_expression
def lexical_reference() -> ParsingExpressionLike:
    return LEXICAL_RULE, Not([LEXICAL_ASSIGNMENT, LEXICAL_INPLACE_OR])


# ## Syntax expression
@parsing_expression
def syntax_expression() -> ParsingExpressionLike:
    return (syntax_ordered_choice,)


@parsing_expression
def syntax_ordered_choice() -> ParsingExpressionLike:
    return OneOrMore(syntax_sequence, sep=OR)


@parsing_expression
def syntax_sequence() -> ParsingExpressionLike:
    return OneOrMore(syntax_quantity)


@parsing_expression
def syntax_quantity() -> ParsingExpressionLike:
    return [
        (OPEN_SQUARE_BRACKET, syntax_expression, CLOSE_SQUARE_BRACKET),
        (OPEN_BRACE, syntax_expression, CLOSE_BRACE),
        syntax_primary,
    ]


@parsing_expression
def syntax_primary() -> ParsingExpressionLike:
    return [
        ("(", syntax_expression, ")"),
        SYNTAX_KEYWORD,
        SYNTAX_TEXT,
        syntax_reference,
    ]


@parsing_expression
def SYNTAX_KEYWORD() -> ParsingExpressionLike:
    return KEYWORD


@parsing_expression
def SYNTAX_TEXT() -> ParsingExpressionLike:
    return TEXT


@parsing_expression
def syntax_reference() -> ParsingExpressionLike:
    return [
        (LEXICAL_RULE, Not([LEXICAL_ASSIGNMENT, LEXICAL_INPLACE_OR])),
        (SYNTAX_RULE, Not([SYNTAX_ASSIGNMENT, SYNTAX_INPLACE_OR])),
        EOF_RULE,
    ]


# ## Comment rule
@parsing_expression
def comment() -> ParsingExpressionLike:
    return [
        RegExMatch(r"//.*"),
        RegExMatch(r"/\*([^*]|\*[^/])*\*/"),
    ]
