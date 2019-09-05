
__all__ = (
    "stored_definition",
)

from arpeggio import (
    Optional, ZeroOrMore
)
from .. import syntax


def stored_definition():
    """
    stored_definition =
        (WITHIN name? ";")?
        (FINAL? class_definition ";")*
    """
    return (
        Optional(syntax.WITHIN, Optional(syntax.name), ";"),
        ZeroOrMore(Optional(syntax.FINAL), syntax.class_definition, ";"),
    )
