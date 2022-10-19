import re
from pathlib import Path

import pytest
from arpeggio import NoMatch
from pkg_resources import resource_filename

from modelica_language import Parser, syntax


@pytest.fixture(scope="module")
def modelica_parser() -> Parser:
    return Parser(
        f"""
{syntax.v3_4()}
file: stored-definition $EOF
        """,
        "file",
        memoization=True,
    )


SOURCE_DIRECTORY = Path(
    resource_filename(__name__, "Modelica-Compliance/ModelicaCompliance/")
)
SOURCE_FILES = tuple(SOURCE_DIRECTORY.rglob("*.mo"))


@pytest.mark.parametrize(
    "source_file",
    SOURCE_FILES,
    ids=[
        f"{source_file.relative_to(SOURCE_DIRECTORY)}"
        for source_file in SOURCE_FILES
    ],
)
def test_modelica_parser(
    modelica_parser: Parser,
    source_file: Path,
) -> None:
    content = source_file.read_text(encoding="utf-8-sig")

    annotations = list(
        re.finditer(r"shouldPass\s*=\s*(?P<shouldPass>true|false)", content)
    )
    if not annotations:
        shouldPass = True
    else:
        (annotation,) = annotations
        shouldPass = eval(annotation.group("shouldPass").capitalize())

    try:
        modelica_parser.parse(content)
    except NoMatch:
        if not shouldPass:
            raise
