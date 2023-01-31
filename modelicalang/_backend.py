__all__ = (
    "ClassVar",
    "Optional",
    "ParsingExpressionLike",
    "RegExMatch",
    "Tuple",
    "ZeroOrMore",
    "enable_method_in_parser_python",
    "not_start_with_keyword",
    "returns_parsing_expression",
)

import builtins
import enum
import types
from functools import wraps
from types import TracebackType
from typing import Any, Callable, ClassVar
from typing import Optional as NoneOr
from typing import Tuple, Type, TypeVar

from arpeggio import (
    Not,
    Optional,
    ParserPython,
    ParsingExpression,
    RegExMatch,
    ZeroOrMore,
)
from typing_extensions import ParamSpec, Protocol

from .arpeggio_annotation import (
    ParsingExpressionLike,
    returns_parsing_expression,
)

P = ParamSpec("P")
T = TypeVar("T")
T_keywords = TypeVar("T_keywords", bound="SupportsKeywords")


_isinstance__builtins = builtins.isinstance


def _isinstance__callable_as_function(obj: Any, class_or_tuple: Any) -> bool:
    if class_or_tuple is types.FunctionType:  # noqa: E721
        return _isinstance__builtins(obj, Callable)  # type: ignore
    else:
        return _isinstance__builtins(obj, class_or_tuple)


class EnableMethodInParserPython(enum.Enum):
    instance = enum.auto()

    def __call__(self, f: Callable[P, T]) -> Callable[P, T]:
        @wraps(f)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> T:
            with self:
                return f(*args, **kwargs)

        return wrapped

    def __enter__(self) -> Type[ParserPython]:
        builtins.isinstance = _isinstance__callable_as_function
        return ParserPython

    def __exit__(
        self,
        typ: NoneOr[Type[BaseException]],
        value: NoneOr[BaseException],
        traceback: NoneOr[TracebackType],
    ) -> NoneOr[bool]:
        builtins.isinstance = _isinstance__builtins
        return None


enable_method_in_parser_python = EnableMethodInParserPython.instance


class SupportsKeywords(Protocol):
    _keywords_: ClassVar[Tuple[str, ...]]


def not_start_with_keyword(
    f: Callable[[Type[T_keywords]], ParsingExpression]
) -> Callable[[Type[T_keywords]], ParsingExpression]:
    @wraps(f)
    @returns_parsing_expression
    def wrapped(cls: Type[T_keywords]) -> ParsingExpressionLike:
        return (
            Not(
                RegExMatch(
                    r"(" + r"|".join(cls._keywords_) + r")(?![0-9A-Z_a-z])"
                )
            ),
            f(cls),
        )

    return wrapped
