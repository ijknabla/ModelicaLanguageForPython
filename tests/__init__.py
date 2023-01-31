import enum
from functools import lru_cache
from typing import Optional

from arpeggio import EOF, ParserPython, RegExMatch

from modelicalang import (
    ModelicaVersion,
    ParsingExpressionLike,
    enable_method_in_parser_python,
    get_syntax_type,
    returns_parsing_expression,
)


class TargetLanguageDef(enum.Flag):
    NULL = 0
    IDENT = enum.auto()
    IDENT_DIALECT = enum.auto()
    Q_IDENT = enum.auto()
    NONDIGIT = enum.auto()
    S_CHAR = enum.auto()
    Q_CHAR = enum.auto()
    S_ESCAPE = enum.auto()
    DIGIT = enum.auto()
    UNSIGNED_INTEGER = enum.auto()

    @lru_cache(None)
    @enable_method_in_parser_python
    def get_parser(
        self, version: Optional[ModelicaVersion] = None
    ) -> ParserPython:
        Syntax = get_syntax_type(version)

        if self is TargetLanguageDef.IDENT_DIALECT:

            class Syntax(_DialectMixin, Syntax):  # type: ignore
                ...

        @returns_parsing_expression
        def file() -> ParsingExpressionLike:
            if (
                self is TargetLanguageDef.IDENT
                or self is TargetLanguageDef.IDENT_DIALECT
            ):
                return Syntax.IDENT, EOF
            elif self is TargetLanguageDef.Q_IDENT:
                return Syntax.Q_IDENT, EOF
            elif self is TargetLanguageDef.NONDIGIT:
                return Syntax.NONDIGIT, EOF
            elif self is TargetLanguageDef.S_CHAR:
                return Syntax.S_CHAR, EOF
            elif self is TargetLanguageDef.Q_CHAR:
                return Syntax.Q_CHAR, EOF
            elif self is TargetLanguageDef.S_ESCAPE:
                return Syntax.S_ESCAPE, EOF
            elif self is TargetLanguageDef.DIGIT:
                return Syntax.DIGIT, EOF
            elif self is TargetLanguageDef.UNSIGNED_INTEGER:
                return Syntax.UNSIGNED_INTEGER, EOF
            raise NotImplementedError()

        return ParserPython(file, Syntax.COMMENT)


class _DialectMixin:
    @classmethod
    @returns_parsing_expression
    def IDENT(cls) -> ParsingExpressionLike:
        return [
            super().IDENT(),  # type: ignore
            RegExMatch(r"\$\w+"),
        ]
