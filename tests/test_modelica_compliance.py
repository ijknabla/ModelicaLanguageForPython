from pathlib import Path

import pytest
from arpeggio import ParseTreeNode
from pkg_resources import resource_filename

from modelica_language import ModelicaVersion, get_file_parser

SOURCE_DIRECTORY = Path(
    resource_filename(__name__, "Modelica-Compliance/ModelicaCompliance/")
)
SOURCE_FILES = tuple(SOURCE_DIRECTORY.rglob("*.mo"))


@pytest.mark.parametrize("version", ModelicaVersion)
@pytest.mark.parametrize(
    "source_file",
    SOURCE_FILES,
    ids=[
        f"{source_file.relative_to(SOURCE_DIRECTORY.parent)}"
        for source_file in SOURCE_FILES
    ],
)
def test_modelica_parser(
    version: ModelicaVersion,
    source_file: Path,
) -> None:
    parseTree = get_file_parser(version).parse(
        source_file.read_text(encoding="utf-8-sig")
    )
    assert isinstance(parseTree, ParseTreeNode)
