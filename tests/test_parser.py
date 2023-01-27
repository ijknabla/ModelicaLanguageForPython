from contextlib import ExitStack
from functools import lru_cache
from typing import Iterator, Tuple

import pytest
from arpeggio import NoMatch

from . import TargetLanguageDef


@lru_cache()
def _accept_DIGIT() -> TargetLanguageDef:
    return (
        TargetLanguageDef.DIGIT
        | TargetLanguageDef.UNSIGNED_INTEGER
        | _accept_Q_CHAR()
    )


@lru_cache()
def _accept_NONDIGIT() -> TargetLanguageDef:
    return TargetLanguageDef.NONDIGIT | _accept_IDENT() | _accept_Q_CHAR()


@lru_cache()
def _accept_IDENT() -> TargetLanguageDef:
    return TargetLanguageDef.IDENT | TargetLanguageDef.IDENT_DIALECT


@lru_cache()
def _accept_Q_IDENT() -> TargetLanguageDef:
    return TargetLanguageDef.Q_IDENT | _accept_IDENT()


@lru_cache()
def _accept_Q_CHAR() -> TargetLanguageDef:
    return TargetLanguageDef.Q_CHAR | TargetLanguageDef.S_CHAR


def iter_text_and_matching_target() -> Iterator[Tuple[str, TargetLanguageDef]]:
    # Character tests
    for text in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        yield text, _accept_DIGIT()
    for text in ["_"]:
        yield text, _accept_NONDIGIT()
    for text in ["α"]:
        yield text, TargetLanguageDef.S_CHAR
    # Escape tests
    for text in [r"\'", r"\"", r"\\"]:
        yield text, TargetLanguageDef.S_ESCAPE
    # Word tests
    for text in ["00", "111", "2222", "33333"]:
        yield text, TargetLanguageDef.UNSIGNED_INTEGER
    # Ident tests
    for text in ["abc", " abc ", "modelica", "modelA", "model0"]:
        yield text, _accept_IDENT()
    for text in ["'model'"]:
        yield text, _accept_Q_IDENT()
    for text in ["$identifier"]:
        yield text, TargetLanguageDef.IDENT_DIALECT
    # Other tests
    for text in ["ab c", "model", "model:"]:
        yield text, TargetLanguageDef.NULL


@pytest.mark.parametrize("target", filter(None, TargetLanguageDef))
@pytest.mark.parametrize(
    "text, matching_target", iter_text_and_matching_target()
)
def test_parser(
    target: TargetLanguageDef,
    text: str,
    matching_target: TargetLanguageDef,
) -> None:
    with ExitStack() as stack:
        if not matching_target & target:
            stack.enter_context(pytest.raises(NoMatch))
        target.get_parser().parse(text)
