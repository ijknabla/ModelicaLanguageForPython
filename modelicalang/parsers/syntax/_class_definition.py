
__all__ = (
    "class_definition",
    "class_prefixes",
    "class_specifier",
    "long_class_specifier",
    "short_class_specifier",
    "der_class_specifier",
    "base_prefix",
    "enum_list",
    "enumeration_literal",
    "composition",
    "language_specification",
    "external_function_call",
    "element_list",
    "element",
    "import_clause",
    "import_list",
)

from arpeggio import (
    Optional, ZeroOrMore, OneOrMore,
)
from .. import syntax


def class_definition():
    """
    class_definition =
        ENCAPSULATED? class_prefixes class_specifier
    """
    return (
        Optional(syntax.ENCAPSULATED), class_prefixes, class_specifier,
    )


def class_prefixes():
    """
    class_prefixes =
        PARTIAL?
        (
            CLASS / MODEL / OPERATOR? RECORD / BLOCK / EXPANDABLE? CONNECTOR
            / TYPE / PACKAGE / (PURE / IMPURE)? OPERATOR? FUNCTION / OPERATOR
        )
    """
    return (
        Optional(syntax.PARTIAL),
        [
            syntax.CLASS,
            syntax.MODEL,
            (Optional(syntax.OPERATOR), syntax.RECORD),
            syntax.BLOCK,
            (Optional(syntax.EXPANDABLE), syntax.CONNECTOR),
            syntax.TYPE,
            syntax.PACKAGE,
            (
                Optional(
                    [syntax.PURE, syntax.IMPURE]
                ),
                Optional(syntax.OPERATOR),
                syntax.FUNCTION
            ),
            syntax.OPERATOR,
        ],
    )


def class_specifier():
    """
    class_specifier =
        long_class_specifier / short_class_specifier / der_class_specifier
    """
    return [
        long_class_specifier,
        short_class_specifier,
        der_class_specifier,
    ]


def long_class_specifier():
    """
    long_class_specifier =
        EXTENDS IDENT class_modification? string_comment composition END IDENT
        / IDENT string_comment composition END IDENT
    """
    return [
        (
            syntax.EXTENDS, syntax.IDENT, Optional(syntax.class_modification),
            syntax.string_comment, syntax.composition, syntax.END, syntax.IDENT
        ),
        (
            syntax.IDENT, syntax.string_comment, syntax.composition,
            syntax.END, syntax.IDENT
        ),
    ]


def short_class_specifier():
    """
    short_class_specifier =
        IDENT "=" ENUMERATION "(" (":" / enum_list?) ")" comment
        / IDENT "=" base_prefix type_specifier array_subscripts?
          class_modification? comment
    """
    return [
        (
            syntax.IDENT, "=", syntax.ENUMERATION,
            "(", [":", Optional(syntax.enum_list)], ")",
            syntax.comment,
        ),
        (
            syntax.IDENT, "=", syntax.base_prefix, syntax.type_specifier,
            Optional(syntax.array_subscripts),
            Optional(syntax.class_modification), syntax.comment,
        ),
    ]


def der_class_specifier():
    """
    der_class_specifer =
        IDENT "=" DER "(" type_specifier "," IDENT ("," IDENT)* ")" comment
    """
    return (
        syntax.IDENT, "=", syntax.DER, "(", syntax.type_specifier, ",",
        OneOrMore(syntax.IDENT, sep=","), ")", syntax.comment
    )


def base_prefix():
    """
    base_prefix =
        (INPUT / OUTPUT)?
    """
    return Optional([syntax.INPUT, syntax.OUTPUT])


def enum_list():
    """
    enum_list = enumeration_literal ("," enumeration_literal)*
    """
    return OneOrMore(syntax.enumeration_literal, sep=",")


def enumeration_literal():
    """
    enumeration_literal = IDENT comment
    """
    return syntax.IDENT, syntax.comment


def composition():
    """
    composition =
        element_list
        (
            PUBLIC element_list
            / PROTECTED element_list
            / equation_section
            / algorithm_section
        )*
        (
            EXTERNAL language_specification?
            external_function_call? annotation? ";"
        )?
        (annotation ";")?
    """
    return (
        syntax.element_list,
        ZeroOrMore(
            [
                (syntax.PUBLIC, syntax.element_list),
                (syntax.PROTECTED, syntax.element_list),
                syntax.equation_section,
                syntax.algorithm_section,
            ]
        ),
        Optional(
            syntax.EXTERNAL, Optional(syntax.language_specification),
            Optional(syntax.external_function_call),
            Optional(syntax.annotation), ";",
        ),
        Optional(syntax.annotation, ";"),
    )


def language_specification():
    """
    language_specification =
        STRING
    """
    return syntax.STRING


def external_function_call():
    """
    external_function_call =
        (component_reference "=")? IDENT "(" expression_list? ")"
    """
    return (
        Optional(syntax.component_reference, "="),
        syntax.IDENT, "(", Optional(syntax.expression_list), ")",
    )


def element_list():
    """
    element_list =
        (element ";")*
    """
    return ZeroOrMore(syntax.element, ';')


def element():
    """
    element =
        import_clause
        extends_clause
        / REDECLARE? FINAL? INNER? OUTER?
            (
                REPLACEABLE (class_definition / component_clause)
                  (constraining_clause comment)?
                / (class_definition / component_clause)
            )
    """
    return [
        syntax.import_clause,
        syntax.extends_clause,
        (
            Optional(syntax.REDECLARE),
            Optional(syntax.FINAL),
            Optional(syntax.INNER),
            Optional(syntax.OUTER),
            [
                (
                    syntax.REPLACEABLE,
                    [
                        syntax.class_definition,
                        syntax.component_clause
                    ],
                    Optional(syntax.constraining_clause, syntax.comment)
                ),
                [syntax.class_definition, syntax.component_clause],
            ],
        ),
    ]


def import_clause():
    """
    import_clause =
        import
        (
            IDENT "=" name
            / name ("." ("*" / "{" import_list "}") )?
        )
        comment
    """
    return (
        syntax.IMPORT,
        [
            (syntax.IDENT, "=", syntax.name),
            (
                syntax.name,
                Optional(
                    ".",
                    [
                        "*",
                        ("{", syntax.import_list, "}"),
                    ],
                ),
            ),
        ],
        syntax.comment,
    )


def import_list():
    """
    import_list =
        IDENT ("," IDENT)*
    """
    return OneOrMore(syntax.IDENT, sep=",")
