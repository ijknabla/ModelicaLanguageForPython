import enum
from pathlib import Path
from typing import Any, Union

import pytest
from arpeggio import EndOfFile, ParserPython
from pkg_resources import resource_filename

from modelica_language import ParserPEG
from modelica_language.parsers import syntax
from modelica_language.syntax import v3_4


class ParserEnum(enum.Enum):
    py = enum.auto()
    peg = enum.auto()

    def select_parser(
        self, py: ParserPython, peg: ParserPEG
    ) -> Union[ParserPython, ParserPEG]:
        if self is ParserEnum.py:
            return py
        elif self is ParserEnum.peg:
            return peg
        else:
            raise NotImplementedError()


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
file: stored-definition $EOF
        """,
        "file",
        "$COMMENT",
    )


SOURCE_DIRECTORY = Path(
    resource_filename(__name__, "Modelica-Compliance/ModelicaCompliance/")
)
SOURCE_FILES = tuple(SOURCE_DIRECTORY.rglob("*.mo"))


@pytest.mark.parametrize(
    "parser_enum",
    ParserEnum,
)
@pytest.mark.parametrize(
    "source_file",
    SOURCE_FILES,
    ids=[
        f"{source_file.relative_to(SOURCE_DIRECTORY.parent)}"
        for source_file in SOURCE_FILES
    ],
)
def test_modelica_parser(
    parser_enum: ParserEnum,
    py_parser: ParserPython,
    peg_parser: ParserPEG,
    source_file: Path,
) -> None:
    parser_enum.select_parser(
        py_parser,
        peg_parser,
    ).parse(source_file.read_text(encoding="utf-8-sig"))
