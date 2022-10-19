import re
from pathlib import Path

import pytest
from arpeggio import NoMatch
from pkg_resources import resource_filename

from modelica_language import Parser, syntax


@pytest.fixture(scope="module")
def modelica_parser() -> Parser:
    return Parser(
        syntax.v3_4()
        + """
file: stored-definition $EOF
        """,
        "file",
        memoization=True,
    )


@pytest.mark.parametrize(
    "path",
    [
        *Path(
            resource_filename(
                __name__, "Modelica-Compliance/ModelicaCompliance/"
            )
        ).glob("**/*.mo")
    ],
)
def test_modelica_parser(
    modelica_parser: Parser,
    path: Path,
) -> None:
    content = path.read_text(encoding="utf-8-sig")

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
