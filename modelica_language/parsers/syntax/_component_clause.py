
__all__ = (
    "component_clause",
    "type_prefix",
    "component_list",
    "component_declaration",
    "condition_attribute",
    "declaration",
)

from arpeggio import (
    Optional, OneOrMore,
)
from .. import syntax


def component_clause():
    """
    component_clause =
        type_prefix type_specifier array_subscripts? component_list
    """
    return (
        syntax.type_prefix, syntax.type_specifier,
        Optional(syntax.array_subscripts), syntax.component_list
    )


def type_prefix():
    """
    type_prefix =
        (FLOW/STREAM)? (DISCRETE/PARAMETER/CONSTANT)? (INPUT/OUTPUT)?
    """
    return (
        Optional(
            [
                syntax.FLOW,
                syntax.STREAM
            ]
        ),
        Optional(
            [
                syntax.DISCRETE,
                syntax.PARAMETER,
                syntax.CONSTANT,
            ]
        ),
        Optional(
            [
                syntax.INPUT,
                syntax.OUTPUT,
            ]
        ),
    )


def component_list():
    """
    component_list =
        component_declaration ("," component_declaration)*
    """
    return OneOrMore(syntax.component_declaration, sep=",")


def component_declaration():
    """
    component_declaration =
        declaration condition_attribute? comment
    """
    return (
        syntax.declaration, Optional(syntax.condition_attribute),
        syntax.comment,
    )


def condition_attribute():
    """
    condition_attribute =
        IF expression
    """
    return syntax.IF, syntax.expression


def declaration():
    """
    declaration =
        IDENT array_subscripts? modification?
    """
    return (
        syntax.IDENT,
        Optional(syntax.array_subscripts),
        Optional(syntax.modification),
    )
