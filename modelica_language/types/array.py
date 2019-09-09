
__all__ = (
    "array_sizes_from_indices",
)

import abc
import collections.abc

class ArraySize(collections.abc.Hashable):
    @abc.abstractclassmethod
    def __index__(self):
        return NotImplemented


COLON = slice(None, None, None)


class FlexibleArraySize(ArraySize):
    def __new__(cls):
        return __instance

    def __index__(self):
        return COLON

    def __hash__(self):
        return 0
    
    def __str__(self):
        return ":"


_FlexibleArraySize__instance = object.__new__(FlexibleArraySize)


class ArraySizeInteger(ArraySize, int):
    def __index__(self):
        return self
    
    def __hash__(self):
        return int.__hash__(self)


def array_size_from_index(index):
    if isinstance(index, ArraySize):
        return index
    if isinstance(index, int):
        return ArraySizeInteger(index)
    elif isinstance(index, slice):
        if not index == slice(None, None, None):
            raise ValueError(
                f"slice index must be {COLON} (known as ':') "
                f"got {index!r}"
            )
        return FlexibleArraySize()
    else:
        raise TypeError(
            f"index must be int or slice got {index!r}"
        )

def array_sizes_from_indices(indices):
    if not isinstance(indices, tuple):
        return array_sizes_from_indices( (indices,) )
    return tuple(map(array_size_from_index, indices))
