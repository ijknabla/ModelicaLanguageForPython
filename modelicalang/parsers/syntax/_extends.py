
__all__ = (
    "extends_clause",
    "constraining_clause",
)

from arpeggio import Optional
from .. import syntax


def extends_clause():
    """
    extends_clause =
        EXTENDS type_specifier class_modification? annotation?
    """
    return (
        syntax.EXTENDS,
        syntax.type_specifier,
        Optional(syntax.class_modification),
        Optional(syntax.annotation),
    )


def constraining_clause():
    """
    constraining_clause =
        CONSTRAINEDBY type_specifier class_modification?
    """
    return (
        syntax.CONSTRAINEDBY,
        syntax.type_specifier,
        Optional(syntax.class_modification)
    )
