
__all__ = (
    "NDArrayWrapper",
    "ArraySize",
    "array_sizes_from_indices",
)

import abc
import collections.abc
import functools
import numpy


# define NDArrayWrapper

class InheritableNDArray(numpy.ndarray):
    def __new__(cls, buffer, dtype=None):
        arr = numpy.array(buffer, dtype=dtype)

        return super(InheritableNDArray, cls).__new__(
            cls, arr.shape, buffer=arr, dtype=arr.dtype
        )


class StrAsObjectNDArray(InheritableNDArray):
    def __new__(cls, buffer, dtype=None):
        if isinstance(dtype, type) and issubclass(dtype, str):
            dtype = object

        return super(StrAsObjectNDArray, cls).__new__(
            cls, buffer=buffer, dtype=dtype
        )


class AutoCastNDArray(StrAsObjectNDArray):
    def __new__(cls, buffer, dtype=None):
        self = super(AutoCastNDArray, cls).__new__(
            cls, buffer, dtype
        )
        if dtype is not None and self.dtype == object:
            isinstance_mask = self.isinstance(dtype)
            if not isinstance_mask.all():
                self[~isinstance_mask] = list(
                    map(dtype, self[~isinstance_mask])
                )
        return self

    def isinstance(self, class_or_tuple):
        @functools.partial(numpy.vectorize, otypes=(bool,))
        def vectorized_isinstance(elem):
            return isinstance(elem, class_or_tuple)
        return vectorized_isinstance(self)


class NDArrayWrapper(AutoCastNDArray):
    def __format__(self, format_spec):
        return "{{{}}}".format(
            ", ".join(
                f"{{:{format_spec}}}".format(subarray)
                for subarray in self
            )
        )


# define ArraySize, array_sizes_from_indices()

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
    
    def __eq__(self, other):
        if isinstance(other, int):
            return True
        else:
            return super().__eq__(other)


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
