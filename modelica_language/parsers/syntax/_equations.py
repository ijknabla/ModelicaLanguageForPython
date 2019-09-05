
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

from arpeggio import (
    Optional, ZeroOrMore, OneOrMore,
)
from .. import syntax


def equation_section():
    """
    equation_section =
        INITIAL? EQUATION (equation ";")*
    """
    return (
        Optional(syntax.INITIAL), syntax.EQUATION,
        ZeroOrMore(syntax.equation, ";"),
    )


def algorithm_section():
    """
    algorithm_section =
        INITIAL? ALGORITHM (statement ";")*
    """
    return (
        Optional(syntax.INITIAL), syntax.ALGORITHM,
        ZeroOrMore(syntax.statement, ";"),
    )


def equation():
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


def statement():
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
            syntax.BREAK,
            syntax.RETURN,
            syntax.if_statement,
            syntax.for_statement,
            syntax.while_statement,
            syntax.when_statement,
            (
                "(", syntax.output_expression_list, ")", ":=",
                syntax.component_reference, syntax.function_call_args,
            ),
            (
                syntax.component_reference,
                [(":=", syntax.expression), syntax.function_call_args],
            ),
        ],
        syntax.comment,
    )


def if_equation():
    """
    if_equation =
        IF     expression THEN (equation ";")*
      ( ELSEIF expression THEN (equation ";")* )*
      ( ELSE                   (equation ";")* )?
        END IF
    """
    return (
        (
            syntax.IF, syntax.expression, syntax.THEN,
            ZeroOrMore(
                syntax.equation, ";",
            ),
        ),
        ZeroOrMore(
            syntax.ELSEIF, syntax.expression, syntax.THEN,
            ZeroOrMore(
                syntax.equation, ";",
            ),
        ),
        Optional(
            syntax.ELSE,
            ZeroOrMore(
                syntax.equation, ";",
            ),
        ),
        syntax.END, syntax.IF,
    )


def if_statement():
    """
    if_statement =
        IF     expression THEN (statement ";")*
      ( ELSEIF expression THEN (statement ";")* )*
      ( ELSE                   (statement ";")* )?
        END IF
    """
    return (
        (
            syntax.IF, syntax.expression, syntax.THEN,
            ZeroOrMore(
                syntax.statement, ";",
            ),
        ),
        ZeroOrMore(
            syntax.ELSEIF, syntax.expression, syntax.THEN,
            ZeroOrMore(
                syntax.statement, ";",
            ),
        ),
        Optional(
            syntax.ELSE,
            ZeroOrMore(
                syntax.statement, ";",
            ),
        ),
        syntax.END, syntax.IF,
    )


def for_equation():
    """
    for_equation =
        FOR for_indices LOOP
            (equation ";")*
        END FOR
    """
    return (
        syntax.FOR, syntax.for_indices, syntax.LOOP,
        ZeroOrMore(
            syntax.equation, ";",
        ),
        syntax.END, syntax.FOR,
    )


def for_statement():
    """
    for_statement =
        FOR for_indices LOOP
            (statement ";")*
        END FOR
    """
    return (
        syntax.FOR, syntax.for_indices, syntax.LOOP,
        ZeroOrMore(
            syntax.statement, ";",
        ),
        syntax.END, syntax.FOR,
    )


def for_indices():
    """
    for_indices =
        for_index ("," for_index)*
    """
    return OneOrMore(syntax.for_index, sep=",")


def for_index():
    """
    for_index =
        IDENT (IN expression)?
    """
    return syntax.IDENT, Optional(syntax.IN, syntax.expression)


def while_statement():
    """
    while_statement =
        WHILE expression LOOP
            (statement ";")*
        END WHILE
    """
    return (
        syntax.WHILE, syntax.expression, syntax.LOOP,
        ZeroOrMore(
            syntax.statement, ";",
        ),
        syntax.END, syntax.WHILE,
    )


def when_equation():
    """
    when_equation =
        WHEN     expression THEN (equation ";")*
      ( ELSEWHEN expression THEN (equation ";")* )*
        END WHEN
    """
    return (
        (
            syntax.WHEN, syntax.expression, syntax.THEN,
            ZeroOrMore(
                syntax.equation, ";",
            ),
        ),
        ZeroOrMore(
            syntax.ELSEWHEN, syntax.expression, syntax.THEN,
            ZeroOrMore(
                syntax.equation, ";",
            ),
        ),
        syntax.END, syntax.WHEN,
    )


def when_statement():
    """
    when_statement =
        WHEN     expression THEN (statement ";")*
      ( ELSEWHEN expression THEN (statement ";")* )*
        END WHEN
    """
    return (
        (
            syntax.WHEN, syntax.expression, syntax.THEN,
            ZeroOrMore(
                syntax.statement, ";",
            ),
        ),
        ZeroOrMore(
            syntax.ELSEWHEN, syntax.expression, syntax.THEN,
            ZeroOrMore(
                syntax.statement, ";",
            ),
        ),
        syntax.END, syntax.WHEN,
    )


def connect_clause():
    """
    connect_clause =
        CONNECT "(" component_reference "," component_reference ")"
    """
    return (
        syntax.CONNECT,
        "(", syntax.component_reference, ",", syntax.component_reference, ")",
    )
