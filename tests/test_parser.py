import re
from contextlib import ExitStack

import pytest
from arpeggio import NoMatch

from modelica_language import ParserPEG, syntax
from tests.utils import assert_injective


@pytest.fixture(scope="module")
def ident_parser() -> ParserPEG:
    return ParserPEG(
        f"""
{syntax.v3_4()}
file: IDENT $EOF$
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
    ident_parser: ParserPEG,
    text: str,
    match: bool,
) -> None:
    with ExitStack() as stack:
        if not match:
            stack.enter_context(pytest.raises(NoMatch))
        ident_parser.parse(text)


@pytest.fixture(scope="module")
def ident_dialect_parser() -> ParserPEG:
    return ParserPEG(
        f"""
{syntax.v3_4()}
IDENT |= r'\\$\\w*'
file: IDENT $EOF$
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
    ident_dialect_parser: ParserPEG,
    text: str,
    match: bool,
) -> None:
    with ExitStack() as stack:
        if not match:
            stack.enter_context(pytest.raises(NoMatch))
        ident_dialect_parser.parse(text)


@assert_injective
def unify(s: str) -> str:
    if re.match(r"_[a-z]+_", s):
        s = s[1:-1].upper()
    return {"annotation": "annotation_comment", "ANY_KEYWORD": "KEYWORD"}.get(
        s, s
    )
