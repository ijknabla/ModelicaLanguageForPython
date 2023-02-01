from pathlib import Path

import pytest
from arpeggio import ParseTreeNode
from pkg_resources import resource_filename

from modelicalang import ModelicaVersion

from . import get_stored_definition_parser

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
@pytest.mark.parametrize("version", ModelicaVersion)
def test_modelica_parser(
    source_file: Path,
    version: ModelicaVersion,
) -> None:
    parseTree = get_stored_definition_parser(version).parse(
        source_file.read_text(encoding="utf-8-sig")
    )
    assert isinstance(parseTree, ParseTreeNode)
