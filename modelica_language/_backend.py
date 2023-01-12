__all__ = (
    "ParsingExpression",
    "ParsingExpressionLike",
    "not_start_with_keyword",
    "returns_parsing_expression",
)

from functools import wraps
from typing import Callable, ClassVar, Tuple, Type, TypeVar, cast

import arpeggio
from typing_extensions import ParamSpec, Protocol, TypeAlias

P = ParamSpec("P")
T_keywords = TypeVar("T_keywords", bound="SupportsKeywords")

ParsingExpression = arpeggio.ParsingExpression
ParsingExpressionLike: TypeAlias = "arpeggio._ParsingExpressionLike"


class SupportsKeywords(Protocol):
    _keywords_: ClassVar[Tuple[str, ...]]


def not_start_with_keyword(
    f: Callable[[Type[T_keywords]], ParsingExpression]
) -> Callable[[Type[T_keywords]], ParsingExpression]:
    @wraps(f)
    @returns_parsing_expression
    def wrapped(cls: Type[T_keywords]) -> ParsingExpressionLike:
        return (
            arpeggio.Not(
                arpeggio.RegExMatch(
                    r"(" + r"|".join(cls._keywords_) + r")(?![0-9A-Z_a-z])"
                )
            ),
            f(cls),
        )

    return wrapped


def returns_parsing_expression(
    f: Callable[P, ParsingExpressionLike]
) -> Callable[P, ParsingExpression]:
    return cast(Callable[P, ParsingExpression], f)
