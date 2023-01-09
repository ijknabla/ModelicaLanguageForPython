from typing import Callable, NewType, cast

import arpeggio
from typing_extensions import ParamSpec, TypeAlias

P = ParamSpec("P")

ParsingExpression = arpeggio.ParsingExpression
ParsingExpressionLike: TypeAlias = "arpeggio._ParsingExpressionLike"


def returns_parsing_expression(
    f: Callable[P, ParsingExpressionLike]
) -> Callable[P, ParsingExpression]:
    return cast(Callable[P, ParsingExpression], f)


Keyword = NewType("Keyword", str)
Regex = NewType("Regex", str)
Rule = NewType("Rule", str)
Text = NewType("Text", str)
