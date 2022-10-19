from contextlib import ExitStack

import pytest
from arpeggio import NoMatch

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
