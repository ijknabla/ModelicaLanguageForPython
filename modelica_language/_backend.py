__all__ = (
    "ParsingExpression",
    "ParsingExpressionLike",
)

import arpeggio
from typing_extensions import TypeAlias

ParsingExpression = arpeggio.ParsingExpression
ParsingExpressionLike: TypeAlias = "arpeggio._ParsingExpressionLike"
