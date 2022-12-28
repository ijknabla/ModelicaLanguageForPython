__all__ = ("stored_definition",)

from arpeggio import Optional, ZeroOrMore

from .. import syntax
from ._future import Syntax


def stored_definition():  # type: ignore
    """
    stored_definition =
        (WITHIN name? ";")?
        (FINAL? class_definition ";")*
    """
    return (
        Optional(Syntax.WITHIN, Optional(syntax.name), ";"),
        ZeroOrMore(Optional(Syntax.FINAL), syntax.class_definition, ";"),
    )
