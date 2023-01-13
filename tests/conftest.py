import pytest
from arpeggio import EOF, ParserPython, RegExMatch

from modelica_language import ModelicaVersion, get_file_parser
from modelica_language._backend import (
    ParsingExpressionLike,
    enable_method_in_parser_python,
    returns_parsing_expression,
)
from modelica_language.v3_4 import Syntax


@returns_parsing_expression
def ident() -> ParsingExpressionLike:
    return Syntax.IDENT, EOF


@returns_parsing_expression
def ident_dialect() -> ParsingExpressionLike:
    return [Syntax.IDENT, RegExMatch(r"\$\w+")], EOF


@pytest.fixture(scope="module")
def file_parser() -> ParserPython:
    return get_file_parser(ModelicaVersion.v3_4)


@pytest.fixture(scope="module")
@enable_method_in_parser_python
def ident_parser() -> ParserPython:
    return ParserPython(ident, Syntax.COMMENT)


@pytest.fixture(scope="module")
@enable_method_in_parser_python
def ident_dialect_parser() -> ParserPython:
    return ParserPython(ident_dialect, Syntax.COMMENT)
