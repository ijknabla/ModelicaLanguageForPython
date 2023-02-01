__all__ = (
    "ModelicaVersion",
    "get_syntax_type",
    "ParsingExpressionLike",
    "returns_parsing_expression",
    "v3_4",
    "v3_5",
    "latest",
)

import enum
from functools import lru_cache
from typing import TYPE_CHECKING, Dict, Optional, Type, Union

from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from arpeggio import _ParsingExpressionLike  # noqa: F401

from . import v3_4, v3_5
from ._backend import returns_parsing_expression

latest = v3_5
"""
:py:mod:`modelicalang.v3_5` (latest modelica standard)
"""

ParsingExpressionLike: TypeAlias = "_ParsingExpressionLike"
"""
Type-hint for objects valid as
`Arrpegio grammars written in Python <https://textx.github.io/Arpeggio/latest/grammars/#grammars-written-in-python>`_
"""  # noqa: E501
_AnySyntaxType = Union[Type[v3_4.Syntax], Type[v3_5.Syntax]]


class ModelicaVersion(enum.Enum):
    v3_4 = (3, 4)
    v3_5 = latest = (3, 5)


@lru_cache(1)
def _get_syntax_type_table() -> Dict[ModelicaVersion, _AnySyntaxType]:
    return {
        ModelicaVersion.v3_4: v3_4.Syntax,
        ModelicaVersion.v3_5: v3_5.Syntax,
    }


def get_syntax_type(
    version: Optional[ModelicaVersion] = None,
) -> _AnySyntaxType:
    version = version if version is not None else ModelicaVersion.latest
    return _get_syntax_type_table().get(version, latest.Syntax)
