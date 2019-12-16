
from typing import Type
from .size import Sizes
from .abc import ModelicaScalarClass, ModelicaArrayClass
import numpy
from functools import singledispatch


def get_dtype(typ: Type) -> numpy.dtype:
    if issubclass(typ, str):
        return numpy.dtype(object)
    else:
        return numpy.dtype(typ)


class NDArrayWrapper(
    metaclass=ModelicaArrayClass,
):
    buffer: numpy.ndarray

    def __init__(
        self,
        data,
    ):
        @singledispatch
        def get_buffer(data) -> numpy.ndarray:
            return numpy.array(data, dtype=get_dtype(type(self).scalar))

        @get_buffer.register(numpy.ndarray)
        def _(data) -> numpy.ndarray:
            return data

        @get_buffer.register(NDArrayWrapper)
        def _(data) -> numpy.ndarray:
            return data.buffer

        buffer = get_buffer(data)

        if Shape.fromIndices(buffer.shape) != 

    def __iter__(self):
        return iter(self.buffer)

    def __getitem__(self, indices) -> numpy.ndarray:
        return self.buffer[indices]

    def __setitem__(self, indices, value) -> None:
        self.buffer[indices] = value


class PyObjectScalarClass(
    ModelicaScalarClass,
):
    pass


def defaultArrayClassFactory(
    scalarClass: ModelicaScalarClass,
    sizes: Sizes,
):
    name = scalarClass.__name__

    suffixes = "_".join(
        size.asSuffix()
        for size in sizes
    )

    nameOfArrayClass = f"{name}_Array_{suffixes}"
    nameOfArrayClassMeta = f"{name}_ArrayMeta_{suffixes}"

    def get_sizes(cls):
        return sizes

    def get_scalar(cls):
        return scalarClass

    ArrayClassMeta = type(
        nameOfArrayClassMeta,
        (ModelicaArrayClass,),
        {
            "scalar": property(fget=get_scalar),
            "sizes": property(fget=get_sizes),
        }
    )

    if isinstance(scalarClass, str):
        dtype = object
    else:
        dtype = scalarClass

    def init_func(self, buffer, *args, **kwrds):
        super(type(self), self).__init__(arr)
        if Sizes.fromIndices(self[...].shape) != sizes:
            raise ValueError(
                "[{shape}] not equals [{sizes}]".format(
                    shape=", ".join(map(str, self[...].shape)),
                    sizes=", ".join(map(str, sizes)),
                )
            )

    ArrayClass = ArrayClassMeta(
        nameOfArrayClass,
        (NDArrayWrapper,),
        {
            "__init__": init_func
        }
    )

    return ArrayClass


class NumericScalarClass(
    ModelicaScalarClass,
):
    arrayClassFactory = defaultArrayClassFactory


class PrimitiveReal(
    numpy.double,
    metaclass=NumericScalarClass,
):
    pass


class PrimitiveInteger(
    numpy.intc,
    metaclass=NumericScalarClass,
):
    pass


class PrimitiveBoolean(
    numpy.bool_,
    metaclass=NumericScalarClass,
):
    pass


class PrimitiveString(
    str,
    metaclass=NumericScalarClass,
):
    pass
