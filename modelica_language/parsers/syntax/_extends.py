__all__ = (
    "extends_clause",
    "constraining_clause",
)

from arpeggio import Optional

from .. import syntax
from ._future import Syntax


def extends_clause():  # type: ignore
    """
    extends_clause =
        EXTENDS type_specifier class_modification? annotation?
    """
    return (
        Syntax.EXTENDS,
        syntax.type_specifier,
        Optional(syntax.class_modification),
        Optional(syntax.annotation),
    )


def constraining_clause():  # type: ignore
    """
    constraining_clause =
        CONSTRAINEDBY type_specifier class_modification?
    """
    return (
        Syntax.CONSTRAINEDBY,
        syntax.type_specifier,
        Optional(syntax.class_modification),
    )
