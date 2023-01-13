import pytest
from arpeggio import EOF, ParserPython, RegExMatch

from modelica_language import ModelicaVersion, get_file_parser
from modelica_language._backend import (
    ParsingExpressionLike,
    enable_method_in_parser_python,
    returns_parsing_expression,
)
from modelica_language.v3_4 import Syntax


@pytest.fixture(scope="module")
def file_parser() -> ParserPython:
    return get_file_parser(ModelicaVersion.v3_4)


@pytest.fixture(scope="module")
@enable_method_in_parser_python
def ident_parser() -> ParserPython:
    @returns_parsing_expression
    def file() -> ParsingExpressionLike:
        return Syntax.IDENT, EOF

    return ParserPython(file, Syntax.COMMENT)


@pytest.fixture(scope="module")
@enable_method_in_parser_python
def ident_dialect_parser() -> ParserPython:
    @returns_parsing_expression
    def file() -> ParsingExpressionLike:
        return [Syntax.IDENT, RegExMatch(r"\$\w+")], EOF

    return ParserPython(file, Syntax.COMMENT)
