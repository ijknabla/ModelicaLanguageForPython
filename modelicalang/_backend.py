from __future__ import annotations

__all__ = (
    "ClassVar",
    "Optional",
    "ParsingExpressionLike",
    "RegExMatch",
    "SyntaxMeta",
    "Tuple",
    "ZeroOrMore",
    "not_start_with_keyword",
)

import builtins
import types
from functools import wraps
from types import TracebackType
from typing import TYPE_CHECKING, Any, Callable, ClassVar
from typing import Optional as NoneOr
from typing import Tuple, Type, TypeVar
from warnings import warn

from arpeggio import Not, Optional, ParsingExpression, RegExMatch, ZeroOrMore

if TYPE_CHECKING:
    from typing_extensions import ParamSpec, Protocol

from .exceptions import ModelicaLangInternalWarning

if TYPE_CHECKING:
    from . import ParsingExpressionLike

    P = ParamSpec("P")
else:
    ParsingExpressionLike = ...
    P = ...

T = TypeVar("T")
T_keywords = TypeVar("T_keywords", bound="SupportsKeywords")


if TYPE_CHECKING:

    class SupportsKeywords(Protocol):
        _keywords_: ClassVar[Tuple[str, ...]]


def not_start_with_keyword(
    f: Callable[[Type[T_keywords]], ParsingExpression]
) -> Callable[[Type[T_keywords]], ParsingExpression]:
    @wraps(f)
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


_isinstance__builtins = builtins.isinstance


def _isinstance__callable_as_function(obj: Any, class_or_tuple: Any) -> bool:
    if class_or_tuple is types.FunctionType:  # noqa: E721
        return _isinstance__builtins(obj, Callable)  # type: ignore
    else:
        return _isinstance__builtins(obj, class_or_tuple)


def _isinstance__callable_as_function_is_enabled() -> bool:
    return builtins.isinstance is _isinstance__callable_as_function


_syntax_meta_enter_count = 0


class SyntaxMeta(type):
    def __enter__(cls) -> "SyntaxMeta":
        global _syntax_meta_enter_count
        if _syntax_meta_enter_count < 1:
            builtins.isinstance = _isinstance__callable_as_function
        _syntax_meta_enter_count += 1
        return cls

    def __exit__(
        cls,
        typ: NoneOr[Type[BaseException]],
        value: NoneOr[BaseException],
        traceback: NoneOr[TracebackType],
    ) -> NoneOr[bool]:
        global _syntax_meta_enter_count
        _syntax_meta_enter_count -= 1
        if _syntax_meta_enter_count < 1:
            builtins.isinstance = _isinstance__builtins
        return None

    def __getattribute__(cls, name: str) -> Any:
        obj = super().__getattribute__(name)
        if isinstance(obj, Callable):  # type: ignore

            @wraps(obj)
            def wrapped(*args: Any, **kwargs: Any) -> Any:
                if not _isinstance__callable_as_function_is_enabled():
                    warning_message = f"""\
Extension for `arpeggio` was not activated \
before using the grammar definition in {cls}.\
Please enable the extension with the following code.

```python3
with {cls.__module__}.{cls.__name__}:
    # Place original code here!
```"""
                    warn(ModelicaLangInternalWarning(warning_message))
                return obj(*args, **kwargs)

            return wrapped
        else:
            return obj
