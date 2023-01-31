__all__ = (
    "ParsingExpressionLike",
    "returns_parsing_expression",
)

from typing import Callable, cast

import arpeggio
from typing_extensions import ParamSpec, TypeAlias

P = ParamSpec("P")

ParsingExpressionLike: TypeAlias = "arpeggio._ParsingExpressionLike"
""


def returns_parsing_expression(
    f: Callable[P, ParsingExpressionLike]
) -> Callable[P, arpeggio.ParsingExpression]:
    return cast(Callable[P, arpeggio.ParsingExpression], f)
