from contextlib import ExitStack
from typing import List, Tuple

import pytest
from arpeggio import NoMatch, ParserPython

from . import TargetLanguageDef

text_and_matching_target: List[Tuple[str, TargetLanguageDef]] = [
    *(
        (text, TargetLanguageDef.IDENT | TargetLanguageDef.Q_IDENT)
        for text in ["'model'"]
    ),
    *(
        (
            text,
            TargetLanguageDef.S_ESCAPE,
        )
        for text in [r"\'", r"\"", r"\\"]
    ),
    *(
        (
            text,
            TargetLanguageDef.DIGIT
            | TargetLanguageDef.S_CHAR
            | TargetLanguageDef.Q_CHAR
            | TargetLanguageDef.UNSIGNED_INTEGER,
        )
        for text in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ),
    *(
        (text, TargetLanguageDef.UNSIGNED_INTEGER)
        for text in ["00", "111", "2222", "33333"]
    ),
    ("α", TargetLanguageDef.S_CHAR),
    (
        "_",
        TargetLanguageDef.IDENT
        | TargetLanguageDef.NONDIGIT
        | TargetLanguageDef.S_CHAR
        | TargetLanguageDef.Q_CHAR,
    ),
    *(
        (text, TargetLanguageDef.IDENT)
        for text in ("abc", " abc ", "modelica", "modelA", "model0")
    ),
    *(
        (text, TargetLanguageDef.NULL)
        for text in ("ab c", "model", "model:", "$identifier")
    ),
]


@pytest.mark.parametrize("target", filter(None, TargetLanguageDef))
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
