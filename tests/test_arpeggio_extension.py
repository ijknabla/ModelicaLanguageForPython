import pytest

from modelicalang import (
    ModelicaLangInternalWarning,
    ModelicaVersion,
    get_syntax_type,
)
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


@pytest.mark.filterwarnings("error")
@pytest.mark.parametrize("version", ModelicaVersion)
def test_arpeggio_extension_warning(version: ModelicaVersion) -> None:
    syntax_type = get_syntax_type(version)

    with pytest.raises(ModelicaLangInternalWarning):
        syntax_type.IDENT()

    with syntax_type:
        syntax_type.IDENT()

        with syntax_type:
            syntax_type.IDENT()

        syntax_type.IDENT()

    with pytest.raises(ModelicaLangInternalWarning):
        syntax_type.IDENT()
