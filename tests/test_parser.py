import re
from contextlib import ExitStack
from itertools import permutations
from typing import Callable

import pytest
from arpeggio import NoMatch, OrderedChoice, Parser, ParsingExpression

from modelica_language import ParserPEG
from tests.utils import assert_injective, find, flatten


@pytest.mark.parametrize(
    "text, match",
    [
        ("abc", True),
        (" abc ", True),
        ("ab c", False),
        ("model", False),
        ("modelica", True),
        ("modelA", True),
        ("model0", True),
        ("model:", False),
        ("'model'", True),
        ("$identifier", False),
    ],
)
def test_ident_parser(
    ident_parser: ParserPEG,
    text: str,
    match: bool,
) -> None:
    with ExitStack() as stack:
        if not match:
            stack.enter_context(pytest.raises(NoMatch))
        ident_parser.parse(text)


@pytest.mark.parametrize(
    "text, match",
    [
        ("abc", True),
        (" abc ", True),
        ("ab c", False),
        ("model", False),
        ("modelica", True),
        ("modelA", True),
        ("model0", True),
        ("model:", False),
        ("'model'", True),
        ("$identifier", True),
    ],
)
def test_ident_dialect_parser(
    ident_dialect_parser: ParserPEG,
    text: str,
    match: bool,
) -> None:
    with ExitStack() as stack:
        if not match:
            stack.enter_context(pytest.raises(NoMatch))
        ident_dialect_parser.parse(text)


ruleNames = [
    "ALGORITHM",
    "AND",
    "ANNOTATION",
    "BLOCK",
    "BREAK",
    "CLASS",
    "CONNECT",
    "CONNECTOR",
    "CONSTANT",
    "CONSTRAINEDBY",
    "DER",
    "DISCRETE",
    "EACH",
    "ELSE",
    "ELSEIF",
    "ELSEWHEN",
    "ENCAPSULATED",
    "END",
    "ENUMERATION",
    "EOF",
    "EQUATION",
    "EXPANDABLE",
    "EXTENDS",
    "EXTERNAL",
    "FALSE",
    "FINAL",
    "FLOW",
    "FOR",
    "FUNCTION",
    "IDENT",
    "IF",
    "IMPORT",
    "IMPURE",
    "IN",
    "INITIAL",
    "INNER",
    "INPUT",
    "KEYWORD",
    "LOOP",
    "MODEL",
    "NOT",
    "OPERATOR",
    "OR",
    "OUTER",
    "OUTPUT",
    "PACKAGE",
    "PARAMETER",
    "PARTIAL",
    "PROTECTED",
    "PUBLIC",
    "PURE",
    "RECORD",
    "REDECLARE",
    "REPLACEABLE",
    "RETURN",
    "STREAM",
    "STRING",
    "THEN",
    "TRUE",
    "TYPE",
    "UNSIGNED_NUMBER",
    "WHEN",
    "WHILE",
    "WITHIN",
    "add_operator",
    "algorithm_section",
    "annotation_comment",
    "argument",
    "argument_list",
    "arithmetic_expression",
    "array_arguments",
    "array_arguments_non_first",
    "array_subscripts",
    "base_prefix",
    "class_definition",
    "class_modification",
    "class_prefixes",
    "class_specifier",
    "comment",
    "component_clause",
    "component_clause1",
    "component_declaration",
    "component_declaration1",
    "component_list",
    "component_reference",
    "composition",
    "condition_attribute",
    "connect_clause",
    "constraining_clause",
    "declaration",
    "der_class_specifier",
    "element",
    "element_list",
    "element_modification",
    "element_modification_or_replaceable",
    "element_redeclaration",
    "element_replaceable",
    "enum_list",
    "enumeration_literal",
    "equation",
    "equation_section",
    "expression",
    "expression_list",
    "extends_clause",
    "external_function_call",
    "factor",
    "file",
    "for_equation",
    "for_index",
    "for_indices",
    "for_statement",
    "function_argument",
    "function_arguments",
    "function_arguments_non_first",
    "function_call_args",
    "if_equation",
    "if_statement",
    "import_clause",
    "import_list",
    "language_specification",
    "logical_expression",
    "logical_factor",
    "logical_term",
    "long_class_specifier",
    "modification",
    "mul_operator",
    "name",
    "named_argument",
    "named_arguments",
    "output_expression_list",
    "primary",
    "relation",
    "relational_operator",
    "short_class_definition",
    "short_class_specifier",
    "simple_expression",
    "statement",
    "stored_definition",
    "string_comment",
    "subscript",
    "term",
    "type_prefix",
    "type_specifier",
    "when_equation",
    "when_statement",
    "while_statement",
]


def test_file_parser(file_parser: Parser) -> None:
    unify = assert_injective(unify_rule_name)

    assert file_parser.parser_model.root
    assert unify(file_parser.parser_model.rule_name) == "file"

    assert file_parser.comments_model is not None
    assert file_parser.comments_model.root
    assert unify(file_parser.comments_model.rule_name) == "COMMENT"

    assert set(map(unify, flatten(file_parser.parser_model).keys())) == set(
        ruleNames
    )


@pytest.mark.parametrize(argnames="ruleName", argvalues=ruleNames)
def test_compare_parsers(
    ruleName: str,
    peg_file_parser: Parser,
    py_file_parser: Parser,
) -> None:
    peg = find(peg_file_parser.parser_model, ruleName, unify_rule_name)
    py = find(py_file_parser.parser_model, ruleName, unify_rule_name)

    compare_parsing_expression(peg, py, unify_rule_name, unify_rule_name)


def unify_rule_name(s: str) -> str:
    if re.match(r"_[a-zA-Z]+_", s):
        s = s[1:-1].upper()
    return {
        "annotation": "annotation_comment",
        "ANY_KEYWORD": "KEYWORD",
        "CPP_STYLE_COMMENT": "COMMENT",
    }.get(s, s)


def compare_parsing_expression(
    a: ParsingExpression,
    b: ParsingExpression,
    unify_a: Callable[[str], str] = str,
    unify_b: Callable[[str], str] = str,
) -> None:
    if type(a) is not type(b):
        raise TypeError(type(a), type(b))
    if unify_a(a.rule_name) != unify_b(b.rule_name):
        raise ValueError(a.rule_name, b.rule_name)
    if len(a.nodes) != len(b.nodes):
        raise ValueError(len(a.nodes), len(b.nodes))

    exceptions = []
    for b_nodes in (
        permutations(b.nodes)
        if isinstance(b, OrderedChoice)
        else [(*b.nodes,)]
    ):
        for a_, b_ in zip(a.nodes, b_nodes):
            try:
                compare_parsing_expression(a_, b_, unify_a, unify_b)
            except Exception as e:
                exceptions.append(e)
                break
        return

    raise exceptions[0]
