__all__ = (
    "ParsingExpressionLike",
    "enable_method_in_parser_python",
    "get_file_parser",
    "get_syntax_type",
    "returns_parsing_expression",
    "v3_4",
)

import enum
from typing import Optional, Type, cast

from arpeggio import EOF, ParserPython

from . import v3_4
from ._backend import (
    ParsingExpressionLike,
    enable_method_in_parser_python,
    returns_parsing_expression,
)

latest = v3_4


class ModelicaVersion(enum.Enum):
    latest = v3_4 = enum.auto()


_SYNTAXES = {ModelicaVersion.v3_4: v3_4.Syntax}


def get_file_parser(version: Optional[ModelicaVersion] = None) -> ParserPython:
    syntax_type = get_syntax_type(version)

    @returns_parsing_expression
    def file() -> ParsingExpressionLike:
        return syntax_type.stored_definition, EOF

    with enable_method_in_parser_python:
        return ParserPython(file, syntax_type.COMMENT)


def get_syntax_type(
    version: Optional[ModelicaVersion] = None,
) -> Type[v3_4.Syntax]:
    return _SYNTAXES.get(
        cast(ModelicaVersion, version),
        latest.Syntax,
    )
