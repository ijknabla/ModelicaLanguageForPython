
__all__ = (
    "modification",
    "class_modification",
    "argument_list",
    "argument",
    "element_modification_or_replaceable",
    "element_modification",
    "element_redeclaration",
    "element_replaceable",
    "component_clause1",
    "component_declaration1",
    "short_class_definition",
)

from arpeggio import (
    Optional, OneOrMore
)
from .. import syntax


def modification():
    """
    modification =
        "=" expression
        / ":=" expression
        / class_modification ("=" expression)?
    """
    return [
        ("=", syntax.expression),
        (":=", syntax.expression),
        (syntax.class_modification, Optional("=", syntax.expression)),
    ]


def class_modification():
    """
    class_modification =
        "(" argument_list? ")"
    """
    return "(", Optional(syntax.argument_list), ")"


def argument_list():
    """
    argument_list =
        argument ("," argument)*
    """
    return OneOrMore(syntax.argument, sep=",")


def argument():
    """
    argument =
        element_redeclaration
        / element_modification_or_replaceable
    """
    return [
        syntax.element_redeclaration,
        syntax.element_modification_or_replaceable,
    ]


def element_modification_or_replaceable():
    """
    element_modification_or_replaceable =
        EACH? FINAL? (element_modification / element_replaceable)
    """
    return (
        Optional(syntax.EACH),
        Optional(syntax.FINAL),
        [syntax.element_modification, syntax.element_replaceable],
    )


def element_modification():
    """
    element_modification =
        name modification? string_comment
    """
    return (
        syntax.name, Optional(syntax.modification), syntax.string_comment,
    )


def element_redeclaration():
    """
    element_redeclaration =
        REDECLARE EACH? FINAL?
        ((short_class_definition / component_clause1) / element_replaceable)
    """
    return (
        syntax.REDECLARE,
        Optional(syntax.EACH), Optional(syntax.FINAL),
        [
            [
                syntax.short_class_definition,
                syntax.component_clause1,
            ],
            syntax.element_replaceable,
        ],
    )


def element_replaceable():
    """
    element_replaceable =
        REPLACEABLE (short_class_definition / component_clause1)
        constraining_clause?
    """
    return (
        syntax.REPLACEABLE,
        [syntax.short_class_definition, syntax.component_clause1],
        Optional(syntax.constraining_clause),
    )


def component_clause1():
    """
    component_clause1 =
        type_prefix type_specifier component_declaration1
    """
    return (
        syntax.type_prefix,
        syntax.type_specifier,
        syntax.component_declaration1,
    )


def component_declaration1():
    """
    component_declaration1 =
        declaration comment
    """
    return syntax.declaration, syntax.comment


def short_class_definition():
    """
    short_class_definition =
        class_prefixes short_class_specifier
    """
    return syntax.class_prefixes, syntax.short_class_specifier
