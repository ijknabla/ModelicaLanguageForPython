from arpeggio import ParserPython, NoMatch
from contextlib import ExitStack
import pytest

from .parser import comment, grammar, Parser
from .syntax import v3_4


dialects = [
    "",
    """
IDENT |= r'\\$\\w*'
    """,
    """
file: stored-definition $EOF
    """,
]


@pytest.mark.parametrize("dialect", dialects)
def test_syntax(dialect: str) -> None:
    parser = ParserPython(grammar, comment)
    parser.parse(v3_4() + dialect)


@pytest.fixture
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


@pytest.fixture
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
