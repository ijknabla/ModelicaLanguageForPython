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

from arpeggio import Optional, ZeroOrMore

from .. import syntax
from ._future import Syntax


def class_definition():  # type: ignore
    """
    class_definition =
        ENCAPSULATED? class_prefixes class_specifier
    """
    return (
        Optional(Syntax.ENCAPSULATED),
        class_prefixes,
        class_specifier,
    )


def class_prefixes():  # type: ignore
    """
    class_prefixes =
        PARTIAL?
        (
            CLASS / MODEL / OPERATOR? RECORD / BLOCK / EXPANDABLE? CONNECTOR
            / TYPE / PACKAGE / (PURE / IMPURE)? OPERATOR? FUNCTION / OPERATOR
        )
    """
    return (
        Optional(Syntax.PARTIAL),
        [
            Syntax.CLASS,
            Syntax.MODEL,
            (Optional(Syntax.OPERATOR), Syntax.RECORD),
            Syntax.BLOCK,
            (Optional(Syntax.EXPANDABLE), Syntax.CONNECTOR),
            Syntax.TYPE,
            Syntax.PACKAGE,
            (
                Optional([Syntax.PURE, Syntax.IMPURE]),
                Optional(Syntax.OPERATOR),
                Syntax.FUNCTION,
            ),
            Syntax.OPERATOR,
        ],
    )


def class_specifier():  # type: ignore
    """
    class_specifier =
        long_class_specifier / short_class_specifier / der_class_specifier
    """
    return [
        long_class_specifier,
        short_class_specifier,
        der_class_specifier,
    ]


def long_class_specifier():  # type: ignore
    """
    long_class_specifier =
        EXTENDS IDENT class_modification? string_comment composition END IDENT
        / IDENT string_comment composition END IDENT
    """
    return [
        (
            Syntax.EXTENDS,
            Syntax.IDENT,
            Optional(syntax.class_modification),
            syntax.string_comment,
            syntax.composition,
            Syntax.END,
            Syntax.IDENT,
        ),
        (
            Syntax.IDENT,
            syntax.string_comment,
            syntax.composition,
            Syntax.END,
            Syntax.IDENT,
        ),
    ]


def short_class_specifier():  # type: ignore
    """
    short_class_specifier =
        IDENT "=" ENUMERATION "(" (":" / enum_list?) ")" comment
        / IDENT "=" base_prefix type_specifier array_subscripts?
          class_modification? comment
    """
    return [
        (
            Syntax.IDENT,
            "=",
            Syntax.ENUMERATION,
            "(",
            [":", Optional(syntax.enum_list)],
            ")",
            syntax.comment,
        ),
        (
            Syntax.IDENT,
            "=",
            syntax.base_prefix,
            syntax.type_specifier,
            Optional(syntax.array_subscripts),
            Optional(syntax.class_modification),
            syntax.comment,
        ),
    ]


def der_class_specifier():  # type: ignore
    """
    der_class_specifer =
        IDENT "=" DER "(" type_specifier "," IDENT ("," IDENT)* ")" comment
    """
    return (
        Syntax.IDENT,
        "=",
        Syntax.DER,
        "(",
        syntax.type_specifier,
        ",",
        Syntax.IDENT,
        ZeroOrMore(",", Syntax.IDENT),
        ")",
        syntax.comment,
    )


def base_prefix():  # type: ignore
    """
    base_prefix =
        (INPUT / OUTPUT)?
    """
    return Optional([Syntax.INPUT, Syntax.OUTPUT])


def enum_list():  # type: ignore
    """
    enum_list = enumeration_literal ("," enumeration_literal)*
    """
    return syntax.enumeration_literal, ZeroOrMore(
        ",", syntax.enumeration_literal
    )


def enumeration_literal():  # type: ignore
    """
    enumeration_literal = IDENT comment
    """
    return Syntax.IDENT, syntax.comment


def composition():  # type: ignore
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
                (Syntax.PUBLIC, syntax.element_list),  # type: ignore
                (Syntax.PROTECTED, syntax.element_list),  # type: ignore
                syntax.equation_section,
                syntax.algorithm_section,
            ]
        ),
        Optional(
            Syntax.EXTERNAL,
            Optional(syntax.language_specification),
            Optional(syntax.external_function_call),
            Optional(syntax.annotation),
            ";",
        ),
        Optional(syntax.annotation, ";"),
    )


def language_specification():  # type: ignore
    """
    language_specification =
        STRING
    """
    return Syntax.STRING


def external_function_call():  # type: ignore
    """
    external_function_call =
        (component_reference "=")? IDENT "(" expression_list? ")"
    """
    return (
        Optional(syntax.component_reference, "="),
        Syntax.IDENT,
        "(",
        Optional(syntax.expression_list),
        ")",
    )


def element_list():  # type: ignore
    """
    element_list =
        (element ";")*
    """
    return ZeroOrMore(syntax.element, ";")


def element():  # type: ignore
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
            Optional(Syntax.REDECLARE),
            Optional(Syntax.FINAL),
            Optional(Syntax.INNER),
            Optional(Syntax.OUTER),
            [
                (
                    Syntax.REPLACEABLE,
                    [syntax.class_definition, syntax.component_clause],
                    Optional(syntax.constraining_clause, syntax.comment),
                ),
                [syntax.class_definition, syntax.component_clause],
            ],
        ),
    ]


def import_clause():  # type: ignore
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
        Syntax.IMPORT,
        [
            (Syntax.IDENT, "=", syntax.name),
            (
                syntax.name,
                Optional(
                    ".",
                    [
                        "*",
                        ("{", syntax.import_list, "}"),  # type: ignore
                    ],
                ),
            ),
        ],
        syntax.comment,
    )


def import_list():  # type: ignore
    """
    import_list =
        IDENT ("," IDENT)*
    """
    return Syntax.IDENT, ZeroOrMore(",", Syntax.IDENT)
