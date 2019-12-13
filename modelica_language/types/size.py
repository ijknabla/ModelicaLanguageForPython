
__all__ = (
    "SizeBase",
    "Sizes",
)

from typing import Any, Iterable, Union
import abc
import enum


class SizeBase(
    abc.ABC
):
    @abc.abstractmethod
    def __hash__(self) -> int:
        return NotImplemented

    @abc.abstractmethod
    def __index__(self):
        return NotImplemented

    @abc.abstractmethod
    def __eq__(self, other) -> bool:
        return NotImplemented

    @abc.abstractmethod
    def asSuffix(self) -> str:
        return NotImplemented


class FixedSize(
    int, SizeBase
):
    def __new__(cls, *args):
        self = super(cls, cls).__new__(cls, *args)
        if not self > 0:
            raise ValueError(f"Must be positive integer")
        return self

    def __hash__(self):
        return super().__hash__()

    def __index__(self):
        return super().__index__()

    def __eq__(self, other):
        if isinstance(other, int):
            return super().__eq__(other)
        elif isinstance(other, SizeBase):
            return other == self
        else:
            return False

    def __repr__(self):
        repr_ = super().__repr__()
        return f"{type(self).__name__}({repr_})"

    def asSuffix(self):
        return str(self)


_COLON = slice(None, None, None)


@SizeBase.register
class FlexibleSize(enum.Enum):

    flexible = _COLON

    def __hash__(self):
        return hash(-1)

    def __index__(self):
        return self.value

    def __eq__(self, other):
        return isinstance(other, SizeBase)

    def __str__(self):
        return ":"

    def asSuffix(self):
        return "flexible"


FLEXIBLE = FlexibleSize.flexible

Size = Union[SizeBase, FlexibleSize]


def index2size(obj: Any) -> Size:
    if isinstance(obj, SizeBase):
        return obj
    elif isinstance(obj, int):
        return FixedSize(obj)
    elif isinstance(obj, slice):
        return FlexibleSize(obj)
    else:
        raise TypeError(
            f"Index must be slice or int. got {obj!r}"
        )


class Sizes(tuple):
    def __new__(cls, sizes: Iterable[Size]):
        return super(cls, cls).__new__(cls, sizes)

    @classmethod
    def fromIndices(cls, indices):
        if not isinstance(indices, tuple):
            indices = (indices,)
        return cls(map(index2size, indices))

    def __index__(self):
        return tuple(size.__index__() for size in self)
