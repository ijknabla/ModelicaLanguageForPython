import enum
from pathlib import Path
from typing import Union

import pytest
from arpeggio import ParserPython, ParseTreeNode
from pkg_resources import resource_filename

from modelica_language import ParserPEG


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
    py_file_parser: ParserPython,
    file_parser: ParserPEG,
    source_file: Path,
) -> None:
    parser = parser_enum.select_parser(
        py_file_parser,
        file_parser,
    )

    assert parser.parser_model.root
    assert parser.parser_model.rule_name == "file"

    assert parser.comments_model is not None
    assert parser.comments_model.root
    assert parser.comments_model.rule_name in ("COMMENT", "CPP_STYLE_COMMENT")

    parseTree = parser.parse(source_file.read_text(encoding="utf-8-sig"))

    assert isinstance(parseTree, ParseTreeNode)
