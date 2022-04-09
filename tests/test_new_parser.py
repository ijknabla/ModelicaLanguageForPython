from arpeggio import NoMatch
from contextlib import ExitStack
from io import BytesIO
from pathlib import PurePosixPath
import pytest
import re
from typing import Iterator, Tuple
from urllib import request
from zipfile import ZipFile

from new_feature.parser import Parser
from new_feature.syntax import v3_4


@pytest.fixture(scope="module")
def ident_parser() -> Parser:
    return Parser(
        v3_4()
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
        v3_4()
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
        v3_4()
        + """
file: stored-definition $EOF
        """,
        "file",
        memoization=True,
    )


def download_mo_from_zip(
    zip_url: str,
) -> Iterator[Tuple[PurePosixPath, str]]:
    with ExitStack() as stack:
        responce = stack.enter_context(request.urlopen(zip_url))
        zipFile = stack.enter_context(
            ZipFile(BytesIO(responce.read()), mode="r")
        )
        for path in map(PurePosixPath, zipFile.namelist()):
            if not path.suffix == ".mo":
                continue
            with zipFile.open(str(path)) as file:
                yield path, file.read().decode("utf-8-sig")


MODELICA_COMPLIENCE_URL = "https://github.com/modelica/Modelica-Compliance/archive/refs/heads/master.zip"  # noqa: E501


@pytest.mark.parametrize(
    "path, content",
    (*download_mo_from_zip(MODELICA_COMPLIENCE_URL),),
)
def test_modelica_parser(
    modelica_parser: Parser,
    path: PurePosixPath,
    content: str,
) -> None:
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
