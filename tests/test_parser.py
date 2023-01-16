from contextlib import ExitStack
from typing import List, Tuple

import pytest
from arpeggio import NoMatch, ParserPython

from . import TargetLanguageDef

text_and_matching_target: List[Tuple[str, TargetLanguageDef]] = [
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


@pytest.mark.parametrize("target", [TargetLanguageDef.IDENT])
@pytest.mark.parametrize("text, matching_target", text_and_matching_target)
def test_parser(
    target: TargetLanguageDef,
    text: str,
    matching_target: TargetLanguageDef,
) -> None:
    with ExitStack() as stack:
        if not matching_target & target:
            stack.enter_context(pytest.raises(NoMatch))
        target.get_parser().parse(text)


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
