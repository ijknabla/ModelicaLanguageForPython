import pytest

from modelicalang import ModelicaVersion, get_syntax_type
from modelicalang._backend import _isinstance__callable_as_function_is_enabled


def _assert_enabled() -> None:
    assert _isinstance__callable_as_function_is_enabled()


def _assert_disabled() -> None:
    assert not _isinstance__callable_as_function_is_enabled()


@pytest.mark.parametrize("version", ModelicaVersion)
def test_arpeggio_extension(version: ModelicaVersion) -> None:
    _assert_disabled()
    syntax_type = get_syntax_type(version)

    _assert_disabled()
    with syntax_type:
        _assert_enabled()
        with syntax_type:
            _assert_enabled()
        _assert_enabled()
    _assert_disabled()
