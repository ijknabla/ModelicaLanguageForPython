import enum
from functools import lru_cache
from typing import Optional

from arpeggio import EOF, Not, ParserPython, RegExMatch

from modelicalang import (
    ModelicaVersion,
    ParsingExpressionLike,
    get_syntax_type,
    returns_parsing_expression,
    v3_5,
)


def get_stored_definition_parser(
    version: Optional[ModelicaVersion] = None,
) -> ParserPython:
    syntax_type = get_syntax_type(version)

    @returns_parsing_expression
    def file() -> ParsingExpressionLike:
        return syntax_type.stored_definition, EOF

    with syntax_type:
        return ParserPython(file, syntax_type.COMMENT)


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
    UNSIGNED_REAL = enum.auto()

    @lru_cache(None)
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
            elif self is TargetLanguageDef.UNSIGNED_REAL:
                if issubclass(Syntax, v3_5.Syntax):
                    return Syntax.UNSIGNED_REAL, EOF
                else:
                    return (
                        Not(Syntax.UNSIGNED_INTEGER),
                        Syntax.UNSIGNED_NUMBER,
                        EOF,
                    )
            raise NotImplementedError()

        with Syntax:
            return ParserPython(file, Syntax.COMMENT)


class _DialectMixin:
    @classmethod
    @returns_parsing_expression
    def IDENT(cls) -> ParsingExpressionLike:
        return [
            super().IDENT(),  # type: ignore
            RegExMatch(r"\$\w+"),
        ]
