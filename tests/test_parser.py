from arpeggio import NoMatch
from contextlib import ExitStack
from pathlib import Path
from pkg_resources import resource_filename
import pytest
import re

from modelica_language import Parser, syntax


@pytest.fixture(scope="module")
def ident_parser() -> Parser:
    return Parser(
        syntax.v3_4()
        + """
file: IDENT $EOF
        """,
        "file",
    )


@pytest.mark.parametrize(
    "text, match",
    [
        ("abc", True),
        (" abc ", True),
        ("ab c", False),
        ("model", False),
        ("modelica", True),
        ("modelA", True),
        ("model0", True),
        ("model:", False),
        ("'model'", True),
        ("$identifier", False),
    ],
)
def test_ident_parser(
    ident_parser: Parser,
    text: str,
    match: bool,
) -> None:
    with ExitStack() as stack:
        if not match:
            stack.enter_context(pytest.raises(NoMatch))
        ident_parser.parse(text)


@pytest.fixture(scope="module")
def ident_dialect_parser() -> Parser:
    return Parser(
        syntax.v3_4()
        + """
IDENT |= r'\\$\\w*'
file: IDENT $EOF
        """,
        "file",
    )


@pytest.mark.parametrize(
    "text, match",
    [
        ("abc", True),
        (" abc ", True),
        ("ab c", False),
        ("model", False),
        ("modelica", True),
        ("modelA", True),
        ("model0", True),
        ("model:", False),
        ("'model'", True),
        ("$identifier", True),
    ],
)
def test_ident_dialect_parser(
    ident_dialect_parser: Parser,
    text: str,
    match: bool,
) -> None:
    with ExitStack() as stack:
        if not match:
            stack.enter_context(pytest.raises(NoMatch))
        ident_dialect_parser.parse(text)


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
