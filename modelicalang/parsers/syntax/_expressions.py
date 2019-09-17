
__all__ = (
    "expression",
    "simple_expression",
    "logical_expression",
    "logical_term",
    "logical_factor",
    "relation",
    "relational_operator",
    "arithmetic_expression",
    "add_operator",
    "term",
    "mul_operator",
    "factor",
    "primary",
    "type_specifier",
    "name",
    "component_reference",
    "function_call_args",
    "function_arguments",
    "function_arguments_non_first",
    "array_arguments",
    "array_arguments_non_first",
    "named_arguments",
    "named_argument",
    "function_argument",
    "output_expression_list",
    "expression_list",
    "array_subscripts",
    "subscript",
    "comment",
    "string_comment",
    "annotation",
)

from arpeggio import (
    Optional,
    ZeroOrMore, OneOrMore
)
from .. import syntax


def expression():
    """
    expression =
        simple_expression
        / IF expression THEN expression
        (ELSEIF expression THEN expression)*
        ELSE expression
    """
    return [
        syntax.simple_expression,
        (
            (
                syntax.IF, syntax.expression, syntax.THEN, syntax.expression,
            ),
            ZeroOrMore(
                syntax.ELSEIF, syntax.expression, syntax.THEN, syntax.expression,
            ),
            (
                syntax.ELSE, syntax.expression,
            ),
        ),
    ]


def simple_expression():
    """
    simple_expression =
        logical_expression (":" logical_expression (":" logical_expression)?)?
    """
    return (
        syntax.logical_expression,
        Optional(
            ":", syntax.logical_expression,
            Optional(
                ":", syntax.logical_expression
            )
        ),
    )


def logical_expression():
    """
    logical_expression =
        logical_term (OR logical_term)*
    """
    return OneOrMore(syntax.logical_term, sep=syntax.OR)


def logical_term():
    """
    logical_term =
        logical_factor (AND logical_factor)*
    """
    return OneOrMore(syntax.logical_factor, sep=syntax.AND)


def logical_factor():
    """
    logical_factor =
        NOT? relation
    """
    return Optional(syntax.NOT), syntax.relation


def relation():
    """
    relation =
        arithmetic_expression (relational_operator arithmetic_expression)?
    """
    return (
        syntax.arithmetic_expression,
        Optional(syntax.relational_operator, syntax.arithmetic_expression)
    )


def relational_operator():
    """
    relational_operator =
        "<>" / "<=" / ">=" / "<" / ">" / "=="
    """
    return ["<>", "<=", ">=", "<", ">", "=="]


def arithmetic_expression():
    """
    arithmetic_expression =
        add_operator? term (add_operator term)*
    """

    return (
        Optional(syntax.add_operator),
        OneOrMore(syntax.term, sep=syntax.add_operator),
    )


def add_operator():
    """
    add_operator =
        "+" / "-" / ".+" / ".-"
    """
    return ["+", "-", ".+", ".-"]


def term():
    """
    term =
        factor (mul_operator factor)*
    """
    return OneOrMore(syntax.factor, sep=syntax.mul_operator)


def mul_operator():
    """
    mul_operator =
        "*" / "/" / ".*" / "./"
    """
    return ["*", "/", ".*", "./"]


def factor():
    """
    factor =
        primary (("^" / ".^") primary)?
    """
    return syntax.primary, Optional(["^", ".^"], syntax.primary)


def primary():
    """
    primary =
        FALSE
        / TRUE
        / END
        / UNSIGNED_NUMBER
        / STRING
        / "(" output_expression_list ")"
        / "[" expression_list (";" expression_list)* "]"
        / "{" array_arguments "}"
        / (component_reference / DER / INITIAL / PURE) function_call_args
        / component_reference
    """
    return [
        syntax.FALSE,
        syntax.TRUE,
        syntax.END,
        syntax.UNSIGNED_NUMBER,
        syntax.STRING,
        ("(", syntax.output_expression_list, ")"),
        ("[", OneOrMore(syntax.expression_list, sep=";"), "]"),
        ("{", syntax.array_arguments, "}"),
        (
            [
                syntax.component_reference,
                syntax.DER,
                syntax.INITIAL,
                syntax.PURE,
            ],
            syntax.function_call_args,
        ),
        syntax.component_reference,
    ]


def type_specifier():
    """
    type_specifier = "."? name
    """
    return Optional("."), syntax.name


def name():
    """
    name = IDENT ("." IDENT)*
    """
    return OneOrMore(syntax.IDENT, sep='.')


def component_reference():
    """
    component_reference =
        "."? IDENT array_subscripts? ("." IDENT array_subscripts?)*
    """
    return (
        Optional("."), syntax.IDENT, Optional(syntax.array_subscripts),
        ZeroOrMore(".", syntax.IDENT, Optional(syntax.array_subscripts)),
    )


def function_call_args():
    """
    function_call_args =
        "(" function_arguments? ")"
    """
    return "(", Optional(syntax.function_arguments), ")"


def function_arguments():
    """
    function_arguments =
        FUNCTION name "(" named_arguments? ")"
          ("," function_arguments_non_first)?
        / named_arguments
        / expression ("," function_arguments_non_first / FOR for_indices)
    """
    return [
        (
            syntax.FUNCTION, syntax.name,
            "(", Optional(syntax.named_arguments), ")",
            Optional(",", syntax.function_arguments_non_first),
        ),
        syntax.named_arguments,
        (
            syntax.expression,
            Optional(
                [
                    (",", syntax.function_arguments_non_first),
                    (syntax.FOR, syntax.for_indices),
                ]
            ),
        ),
    ]


def function_arguments_non_first():
    """
    function_arguments_non_first =
        named_arguments
        / function_argument ("," function_arguments_non_first)?
    """
    return [
        syntax.named_arguments,
        (
            syntax.function_argument,
            Optional(",", syntax.function_arguments_non_first)
        ),
    ]


def named_arguments():
    """
    named_arguments = named_argument ("," named_arguments)?
    """
    return OneOrMore(syntax.named_argument, sep=",")


def array_arguments():
    """
    array_arguments =
        expression ("," array_arguments_non_first / FOR for_indices)?
    """
    return (
        syntax.expression,
        Optional(
            [
                (",", syntax.array_arguments_non_first),
                (syntax.FOR, syntax.for_indices),
            ]
        ),
    )


def array_arguments_non_first():
    """
    array_arguments_non_first =
        expression ("," array_arguments_non_first)?
    """
    return OneOrMore(syntax.expression, sep=",")


def named_argument():
    """
    named_argument = IDENT "=" function_argument
    """
    return syntax.IDENT, "=", syntax.function_argument


def function_argument():
    """
    function_argument =
        FUNCTION name "(" named_arguments? ")"
        / expression
    """
    return [
        (
            syntax.FUNCTION, syntax.name,
            "(", Optional(syntax.named_arguments), ")",
        ),
        expression,
    ]


def output_expression_list():
    """
    output_expression_list =
        expression? ("," expression?)*
    """
    return (
        Optional(syntax.expression),
        ZeroOrMore(",", Optional(syntax.expression)),
    )


def expression_list():
    """
    expression_list =
        expression ("," expression)*
    """
    return OneOrMore(syntax.expression, sep=",")


def array_subscripts():
    """
    array_subscripts =
        "[" subscript ("," subscript)* "]"
    """
    return "[", OneOrMore(syntax.subscript, sep=","), "]"


def subscript():
    """
    subscript =
        ":" / expression
    """
    return [":", syntax.expression]


def comment():
    """
    comment =
        string_comment annotation?
    """
    return (
        syntax.string_comment,
        Optional(syntax.annotation),
    )


def string_comment():
    """
    string_comment =
        (STRING ("+" STRING)*)?
    """
    return Optional(OneOrMore(syntax.STRING, sep="+"))


def annotation():
    """
    annotation =
        ANNOTATION class_modification
    """
    return syntax.ANNOTATION, syntax.class_modification
