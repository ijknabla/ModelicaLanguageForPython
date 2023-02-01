__all__ = (
    "ModelicaVersion",
    "ParsingExpressionLike",
    "enable_method_in_parser_python",
    "get_file_parser",
    "get_syntax_type",
    "returns_parsing_expression",
    "v3_4",
    "v3_5",
    "latest",
)

import enum
from functools import lru_cache
from typing import TYPE_CHECKING, Dict, Optional, Type, Union

from arpeggio import EOF, ParserPython
from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from arpeggio import _ParsingExpressionLike  # noqa: F401

from . import v3_4, v3_5
from ._backend import (
    enable_method_in_parser_python,
    returns_parsing_expression,
)

latest = v3_5
"""
:py:mod:`modelicalang.v3_5` (latest modelica standard)
"""

ParsingExpressionLike: TypeAlias = "_ParsingExpressionLike"
_AnySyntaxType = Union[Type[v3_4.Syntax], Type[v3_5.Syntax]]


class ModelicaVersion(enum.Enum):
    v3_4 = (3, 4)
    v3_5 = latest = (3, 5)


def get_file_parser(version: Optional[ModelicaVersion] = None) -> ParserPython:
    syntax_type = get_syntax_type(version)

    @returns_parsing_expression
    def file() -> ParsingExpressionLike:
        return syntax_type.stored_definition, EOF

    with enable_method_in_parser_python:
        return ParserPython(file, syntax_type.COMMENT)


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
