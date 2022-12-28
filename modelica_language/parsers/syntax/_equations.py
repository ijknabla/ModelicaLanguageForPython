__all__ = (
    "equation_section",
    "algorithm_section",
    "equation",
    "statement",
    "if_equation",
    "if_statement",
    "for_equation",
    "for_statement",
    "for_indices",
    "for_index",
    "while_statement",
    "when_equation",
    "when_statement",
    "connect_clause",
)

from arpeggio import Optional, ZeroOrMore

from .. import syntax
from ._future import Syntax


def equation_section():  # type: ignore
    """
    equation_section =
        INITIAL? EQUATION (equation ";")*
    """
    return (
        Optional(Syntax.INITIAL),
        Syntax.EQUATION,
        ZeroOrMore(syntax.equation, ";"),
    )


def algorithm_section():  # type: ignore
    """
    algorithm_section =
        INITIAL? ALGORITHM (statement ";")*
    """
    return (
        Optional(Syntax.INITIAL),
        Syntax.ALGORITHM,
        ZeroOrMore(syntax.statement, ";"),
    )


def equation():  # type: ignore
    """
    equation =
        (
            if_equation
            / for_equation
            / connect_clause
            / when_equation
            / simple_expression "=" expression
            / component_reference function_call_args
        )
        comment
    """
    return (
        [
            syntax.if_equation,
            syntax.for_equation,
            syntax.connect_clause,
            syntax.when_equation,
            (syntax.simple_expression, "=", syntax.expression),
            (syntax.component_reference, syntax.function_call_args),
        ],
        syntax.comment,
    )


def statement():  # type: ignore
    """
    statement =
        (
            BREAK
            / RETURN
            / if_statement
            / for_statement
            / while_statement
            / when_statement
            / "(" output_expression_list ")" ":="
              component_reference function_call_args
            / component_reference (":=" expression / function_call_args)
        )
        comment
    """
    return (
        [
            Syntax.BREAK,
            Syntax.RETURN,
            syntax.if_statement,
            syntax.for_statement,
            syntax.while_statement,
            syntax.when_statement,
            (
                "(",
                syntax.output_expression_list,
                ")",
                ":=",
                syntax.component_reference,
                syntax.function_call_args,
            ),
            (
                syntax.component_reference,
                [(":=", syntax.expression), syntax.function_call_args],
            ),
        ],
        syntax.comment,
    )


def if_equation():  # type: ignore
    """
    if_equation =
        IF     expression THEN (equation ";")*
      ( ELSEIF expression THEN (equation ";")* )*
      ( ELSE                   (equation ";")* )?
        END IF
    """
    return (
        Syntax.IF,
        syntax.expression,
        Syntax.THEN,
        ZeroOrMore(
            syntax.equation,
            ";",
        ),
        ZeroOrMore(
            Syntax.ELSEIF,
            syntax.expression,
            Syntax.THEN,
            ZeroOrMore(
                syntax.equation,
                ";",
            ),
        ),
        Optional(
            Syntax.ELSE,
            ZeroOrMore(
                syntax.equation,
                ";",
            ),
        ),
        Syntax.END,
        Syntax.IF,
    )


def if_statement():  # type: ignore
    """
    if_statement =
        IF     expression THEN (statement ";")*
      ( ELSEIF expression THEN (statement ";")* )*
      ( ELSE                   (statement ";")* )?
        END IF
    """
    return (
        Syntax.IF,
        syntax.expression,
        Syntax.THEN,
        ZeroOrMore(
            syntax.statement,
            ";",
        ),
        ZeroOrMore(
            Syntax.ELSEIF,
            syntax.expression,
            Syntax.THEN,
            ZeroOrMore(
                syntax.statement,
                ";",
            ),
        ),
        Optional(
            Syntax.ELSE,
            ZeroOrMore(
                syntax.statement,
                ";",
            ),
        ),
        Syntax.END,
        Syntax.IF,
    )


def for_equation():  # type: ignore
    """
    for_equation =
        FOR for_indices LOOP
            (equation ";")*
        END FOR
    """
    return (
        Syntax.FOR,
        syntax.for_indices,
        Syntax.LOOP,
        ZeroOrMore(
            syntax.equation,
            ";",
        ),
        Syntax.END,
        Syntax.FOR,
    )


def for_statement():  # type: ignore
    """
    for_statement =
        FOR for_indices LOOP
            (statement ";")*
        END FOR
    """
    return (
        Syntax.FOR,
        syntax.for_indices,
        Syntax.LOOP,
        ZeroOrMore(
            syntax.statement,
            ";",
        ),
        Syntax.END,
        Syntax.FOR,
    )


def for_indices():  # type: ignore
    """
    for_indices =
        for_index ("," for_index)*
    """
    return syntax.for_index, ZeroOrMore(",", syntax.for_index)


def for_index():  # type: ignore
    """
    for_index =
        IDENT (IN expression)?
    """
    return Syntax.IDENT, Optional(Syntax.IN, syntax.expression)


def while_statement():  # type: ignore
    """
    while_statement =
        WHILE expression LOOP
            (statement ";")*
        END WHILE
    """
    return (
        Syntax.WHILE,
        syntax.expression,
        Syntax.LOOP,
        ZeroOrMore(
            syntax.statement,
            ";",
        ),
        Syntax.END,
        Syntax.WHILE,
    )


def when_equation():  # type: ignore
    """
    when_equation =
        WHEN     expression THEN (equation ";")*
      ( ELSEWHEN expression THEN (equation ";")* )*
        END WHEN
    """
    return (
        Syntax.WHEN,
        syntax.expression,
        Syntax.THEN,
        ZeroOrMore(
            syntax.equation,
            ";",
        ),
        ZeroOrMore(
            Syntax.ELSEWHEN,
            syntax.expression,
            Syntax.THEN,
            ZeroOrMore(
                syntax.equation,
                ";",
            ),
        ),
        Syntax.END,
        Syntax.WHEN,
    )


def when_statement():  # type: ignore
    """
    when_statement =
        WHEN     expression THEN (statement ";")*
      ( ELSEWHEN expression THEN (statement ";")* )*
        END WHEN
    """
    return (
        Syntax.WHEN,
        syntax.expression,
        Syntax.THEN,
        ZeroOrMore(
            syntax.statement,
            ";",
        ),
        ZeroOrMore(
            Syntax.ELSEWHEN,
            syntax.expression,
            Syntax.THEN,
            ZeroOrMore(
                syntax.statement,
                ";",
            ),
        ),
        Syntax.END,
        Syntax.WHEN,
    )


def connect_clause():  # type: ignore
    """
    connect_clause =
        CONNECT "(" component_reference "," component_reference ")"
    """
    return (
        Syntax.CONNECT,
        "(",
        syntax.component_reference,
        ",",
        syntax.component_reference,
        ")",
    )
