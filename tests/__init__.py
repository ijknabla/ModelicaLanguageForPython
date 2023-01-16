import enum
from functools import lru_cache
from typing import TYPE_CHECKING, Optional

from arpeggio import EOF, ParserPython

from modelica_language import (
    ModelicaVersion,
    ParsingExpressionLike,
    enable_method_in_parser_python,
    get_syntax_type,
    returns_parsing_expression,
)


class TargetLanguageDef(enum.Flag):
    NULL = 0
    IDENT = enum.auto()

    @lru_cache(None)
    @enable_method_in_parser_python
    def get_parser(
        self, version: Optional[ModelicaVersion] = None
    ) -> ParserPython:
        base_syntax_type = get_syntax_type(version)

        if TYPE_CHECKING:
            Syntax = base_syntax_type
        else:

            class Syntax(base_syntax_type):
                ...

        @returns_parsing_expression
        def file() -> ParsingExpressionLike:
            if self is TargetLanguageDef.IDENT:
                return Syntax.IDENT, EOF
            raise NotImplementedError()

        return ParserPython(file, base_syntax_type.COMMENT)
