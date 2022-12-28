__all__ = (
    "component_clause",
    "type_prefix",
    "component_list",
    "component_declaration",
    "condition_attribute",
    "declaration",
)

from arpeggio import Optional, ZeroOrMore

from .. import syntax
from ._future import Syntax


def component_clause():  # type: ignore
    """
    component_clause =
        type_prefix type_specifier array_subscripts? component_list
    """
    return (
        syntax.type_prefix,
        syntax.type_specifier,
        Optional(syntax.array_subscripts),
        syntax.component_list,
    )


def type_prefix():  # type: ignore
    """
    type_prefix =
        (FLOW/STREAM)? (DISCRETE/PARAMETER/CONSTANT)? (INPUT/OUTPUT)?
    """
    return (
        Optional([Syntax.FLOW, Syntax.STREAM]),
        Optional(
            [
                Syntax.DISCRETE,
                Syntax.PARAMETER,
                Syntax.CONSTANT,
            ]
        ),
        Optional(
            [
                Syntax.INPUT,
                Syntax.OUTPUT,
            ]
        ),
    )


def component_list():  # type: ignore
    """
    component_list =
        component_declaration ("," component_declaration)*
    """
    return syntax.component_declaration, ZeroOrMore(
        ",", syntax.component_declaration
    )


def component_declaration():  # type: ignore
    """
    component_declaration =
        declaration condition_attribute? comment
    """
    return (
        syntax.declaration,
        Optional(syntax.condition_attribute),
        syntax.comment,
    )


def condition_attribute():  # type: ignore
    """
    condition_attribute =
        IF expression
    """
    return Syntax.IF, syntax.expression


def declaration():  # type: ignore
    """
    declaration =
        IDENT array_subscripts? modification?
    """
    return (
        Syntax.IDENT,
        Optional(syntax.array_subscripts),
        Optional(syntax.modification),
    )
