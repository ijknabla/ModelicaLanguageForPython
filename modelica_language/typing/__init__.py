
__all__ = [
    "Real",
    "Integer",
    "Boolean",
]

from numbers import (
    Real,
    Integral as Integer,
)

from typing_extensions import Protocol


class Boolean(Protocol):
    def __bool__(self) -> bool:
        ...
