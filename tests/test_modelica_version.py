from typing import Optional

import pytest

from modelicalang import ModelicaVersion, get_syntax_type, latest, v3_5


@pytest.mark.parametrize("version", ModelicaVersion)
def test_modelica_version_names(
    version: ModelicaVersion,
) -> None:
    assert version.name == "v" + "_".join(map(str, version.value))

    syntax = get_syntax_type(version)
    *_, syntax_module_name = syntax.__module__.split(".")
    assert version.name == syntax_module_name


@pytest.mark.parametrize("version", [None, ModelicaVersion.latest])
def test_latest_modelica_version(version: Optional[ModelicaVersion]) -> None:
    assert get_syntax_type(version) == latest.Syntax == v3_5.Syntax
