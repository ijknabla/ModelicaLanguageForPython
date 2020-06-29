
__all__ = [
    "SupportsReal",
    "SupportsInteger",
    "SupportsBoolean",
    "PrimitiveReal",
    "PrimitiveInteger",
    "PrimitiveBoolean",
]


from typing_extensions import Protocol
import numpy  # type: ignore

from numbers import (
    Real as SupportsReal,
    Integral as SupportsInteger,
)


class Boolean(Protocol):
    def __bool__(self) -> bool:
        ...


PrimitiveReal = numpy.double
PrimitiveInteger = numpy.intc
PrimitiveBoolean = numpy.bool
