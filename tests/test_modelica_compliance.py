from pathlib import Path

import pytest
from arpeggio import Parser, ParseTreeNode
from pkg_resources import resource_filename

SOURCE_DIRECTORY = Path(
    resource_filename(__name__, "Modelica-Compliance/ModelicaCompliance/")
)
SOURCE_FILES = tuple(SOURCE_DIRECTORY.rglob("*.mo"))


@pytest.mark.parametrize(
    "source_file",
    SOURCE_FILES,
    ids=[
        f"{source_file.relative_to(SOURCE_DIRECTORY.parent)}"
        for source_file in SOURCE_FILES
    ],
)
def test_modelica_parser(
    source_file: Path,
    file_parser: Parser,
) -> None:
    parseTree = file_parser.parse(source_file.read_text(encoding="utf-8-sig"))
    assert isinstance(parseTree, ParseTreeNode)
