from contextlib import ExitStack
from typing import List, Tuple

import pytest
from arpeggio import NoMatch

from . import TargetLanguageDef

ACCEPT_IDENT = TargetLanguageDef.IDENT | TargetLanguageDef.IDENT_DIALECT
ACCEPT_Q_CHAR = TargetLanguageDef.Q_CHAR | TargetLanguageDef.S_CHAR
ACCEPT_Q_IDENT = TargetLanguageDef.Q_IDENT | ACCEPT_IDENT
ACCEPT_DIGIT_CHAR = (
    TargetLanguageDef.DIGIT
    | TargetLanguageDef.UNSIGNED_INTEGER
    | ACCEPT_Q_CHAR
)
ACCEPT_NONDIGIT_CHAR = (
    TargetLanguageDef.NONDIGIT | ACCEPT_IDENT | ACCEPT_Q_CHAR
)


text_and_matching_target: List[Tuple[str, TargetLanguageDef]] = [
    # Character tests
    *(
        (text, ACCEPT_DIGIT_CHAR)
        for text in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ),
    ("_", ACCEPT_NONDIGIT_CHAR),
    ("α", TargetLanguageDef.S_CHAR),
    *((text, TargetLanguageDef.S_ESCAPE) for text in [r"\'", r"\"", r"\\"]),
    # Word tests
    *(
        (text, TargetLanguageDef.UNSIGNED_INTEGER)
        for text in ["00", "111", "2222", "33333"]
    ),
    # Ident tests
    *((text, ACCEPT_Q_IDENT) for text in ["'model'"]),
    *(
        (text, ACCEPT_IDENT)
        for text in ("abc", " abc ", "modelica", "modelA", "model0")
    ),
    *((text, TargetLanguageDef.IDENT_DIALECT) for text in ["$identifier"]),
    # Other tests
    *((text, TargetLanguageDef.NULL) for text in ("ab c", "model", "model:")),
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
