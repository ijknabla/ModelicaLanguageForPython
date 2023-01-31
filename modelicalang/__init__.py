__all__ = (
    "ParsingExpressionLike",
    "enable_method_in_parser_python",
    "get_file_parser",
    "get_syntax_type",
    "latest",
    "returns_parsing_expression",
    "v3_4",
    "v3_5",
)

import enum
from typing import Dict, Optional, Type, Union, cast

from arpeggio import EOF, ParserPython

from . import v3_4, v3_5
from ._backend import (
    ParsingExpressionLike,
    enable_method_in_parser_python,
    returns_parsing_expression,
)

latest = v3_5


class ModelicaVersion(enum.Enum):
    v3_4 = enum.auto()
    v3_5 = latest = enum.auto()


_AnySyntaxType = Union[Type[v3_4.Syntax], Type[v3_5.Syntax]]
_SYNTAXES: Dict[ModelicaVersion, _AnySyntaxType] = {
    ModelicaVersion.v3_4: v3_4.Syntax,
    ModelicaVersion.v3_5: v3_5.Syntax,
}


def get_file_parser(version: Optional[ModelicaVersion] = None) -> ParserPython:
    syntax_type = get_syntax_type(version)

    @returns_parsing_expression
    def file() -> ParsingExpressionLike:
        return syntax_type.stored_definition, EOF

    with enable_method_in_parser_python:
        return ParserPython(file, syntax_type.COMMENT)


def get_syntax_type(
    version: Optional[ModelicaVersion] = None,
) -> _AnySyntaxType:
    return _SYNTAXES.get(
        cast(ModelicaVersion, version),
        latest.Syntax,
    )
