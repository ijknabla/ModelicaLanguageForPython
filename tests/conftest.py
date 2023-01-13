import pytest
from arpeggio import EndOfFile, RegExMatch

from modelica_language import ParserPython
from modelica_language._backend import (
    ParsingExpressionLike,
    returns_parsing_expression,
)
from modelica_language.v3_4 import Syntax


@returns_parsing_expression
def file() -> ParsingExpressionLike:
    return Syntax.stored_definition, EndOfFile()


@returns_parsing_expression
def ident() -> ParsingExpressionLike:
    return Syntax.IDENT, EndOfFile()


@returns_parsing_expression
def ident_dialect() -> ParsingExpressionLike:
    return [Syntax.IDENT, RegExMatch(r"\$\w+")], EndOfFile()


@pytest.fixture(scope="module")
def file_parser() -> ParserPython:
    return ParserPython(
        file,
        Syntax.COMMENT,
    )


@pytest.fixture(scope="module")
def ident_parser() -> ParserPython:
    return ParserPython(ident, Syntax.COMMENT)


@pytest.fixture(scope="module")
def ident_dialect_parser() -> ParserPython:
    return ParserPython(ident_dialect, Syntax.COMMENT)
