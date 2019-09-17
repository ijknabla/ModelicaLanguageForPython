
__all__ = (
    "NDArrayWrapper",
    "ArraySize",
    "array_sizes_from_indices",
)

import typing
import abc
import collections.abc
import functools
import numpy


# define NDArrayWrapper


def shape_of_sequence(
    sequence: typing.Sequence,
    ndims: int
) -> typing.Generator[int, None, None]:
    elem = sequence
    for idim in range(ndims):
        if not isinstance(elem, collections.abc.Sequence):
            raise TypeError(
                f"dimension {idim} must be Sequence got {elem}"
            )
        yield len(elem)
        elem = elem[0]


def fixed_dimensional_object_array(
    sequence: typing.Sequence,
    ndims: int,
) -> numpy.ndarray:
    shape = tuple(shape_of_sequence(sequence, ndims))
    object_array = numpy.empty(shape, dtype=object)
    object_array[...] = sequence
    return object_array


def cast_object_array(
    array: numpy.ndarray, typ: type
):
    vectorized_cast = numpy.vectorize(
        lambda elem : elem if isinstance(elem, typ) else typ(elem),
        otypes = [object],
    )
    return vectorized_cast(array[...])


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


class NDArrayWrapper(
    StrAsObjectNDArray,
):
    def __new__(cls, buffer, dtype: type, ndims: int):
        ndims_array = fixed_dimensional_object_array(buffer, ndims)

        return super(NDArrayWrapper, cls).__new__(
            cls,
            cast_object_array(ndims_array, dtype),
            dtype=dtype,
        )
    
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
