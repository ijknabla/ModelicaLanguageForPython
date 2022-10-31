from typing import Any

import pytest
from arpeggio import EndOfFile, ParserPython

from modelica_language import ParserPEG
from modelica_language.parsers import syntax
from modelica_language.syntax import v3_4


@pytest.fixture(scope="module")
def ident_parser() -> ParserPEG:
    return ParserPEG(
        f"""
{v3_4()}
file: IDENT $EOF$
        """,
        "file",
    )


@pytest.fixture(scope="module")
def ident_dialect_parser() -> ParserPEG:
    return ParserPEG(
        f"""
{v3_4()}
IDENT |= r'\\$\\w*'
file: IDENT $EOF$
        """,
        "file",
    )


@pytest.fixture(scope="module")
def py_parser() -> ParserPython:
    def file() -> Any:
        return syntax.stored_definition, EndOfFile()

    return ParserPython(
        file,
        syntax.CPP_STYLE_COMMENT,
    )


@pytest.fixture(scope="module")
def peg_parser() -> ParserPEG:
    return ParserPEG(
        f"""
{v3_4()}
file: stored-definition $EOF$
        """,
        "file",
        "COMMENT",
    )
