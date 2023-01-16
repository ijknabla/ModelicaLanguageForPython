from contextlib import ExitStack
from typing import List, Tuple

import pytest
from arpeggio import NoMatch, ParserPython

from . import TargetLanguageDef

text_and_target: List[Tuple[str, TargetLanguageDef]] = [
    ("abc", TargetLanguageDef.IDENT),
    (" abc ", TargetLanguageDef.IDENT),
    ("ab c", TargetLanguageDef.NULL),
    ("model", TargetLanguageDef.NULL),
    ("modelica", TargetLanguageDef.IDENT),
    ("modelA", TargetLanguageDef.IDENT),
    ("model0", TargetLanguageDef.IDENT),
    ("model:", TargetLanguageDef.NULL),
    ("'model'", TargetLanguageDef.IDENT),
    ("$identifier", TargetLanguageDef.NULL),
]


@pytest.mark.parametrize("text, target", text_and_target)
def test_ident_parser(
    ident_parser: ParserPython,
    text: str,
    target: bool,
) -> None:
    with ExitStack() as stack:
        if not target & TargetLanguageDef.IDENT:
            stack.enter_context(pytest.raises(NoMatch))
        ident_parser.parse(text)


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
    ident_dialect_parser: ParserPython,
    text: str,
    match: bool,
) -> None:
    with ExitStack() as stack:
        if not match:
            stack.enter_context(pytest.raises(NoMatch))
        ident_dialect_parser.parse(text)
