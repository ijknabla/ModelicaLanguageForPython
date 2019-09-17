
__all__ = (
    "AbstractModelicaObject",
    "AbstractModelicaClass",
    "AbstractModelicaScalarClass",
    "AbstractModelicaArrayClass",
)

import typing
import abc
import functools
from .array import (
    NDArrayWrapper,
    ArraySize,
    array_sizes_from_indices
)


class AbstractModelicaObject(abc.ABC):
    pass


class AbstractModelicaClass(abc.ABCMeta):
    def __new__(mtcls, name, bases, namespace):
        cls = super(AbstractModelicaClass, mtcls).__new__(
            mtcls, name, bases, namespace
        )
        if not issubclass(cls, AbstractModelicaObject):
            AbstractModelicaObject.register(cls)
        return cls


class AbstractModelicaScalarClass(
    AbstractModelicaClass,
):
    def __getitem__(cls, indices):
        sizes = array_sizes_from_indices(indices)
        return array_class_factory(cls, sizes)


class AbstractModelicaArrayClass(
    AbstractModelicaClass,
):
    sizes: typing.Sequence[ArraySize]
    scalar_class: AbstractModelicaClass

    @property
    def ndims(cls):
        return len(cls.sizes)


class ModelicaArrayObject(
    NDArrayWrapper,
    metaclass=AbstractModelicaArrayClass,
):
    def __new__(cls, buffer):
        self = super(ModelicaArrayObject, cls).__new__(
            cls, buffer, dtype=cls.scalar_class, ndims=cls.ndims
        )

        if not cls.sizes == self.shape:
            raise ValueError(
                f"shape must be {tuple(map(str,cls.sizes))} "
                f"got {self.shape}"
            )

        return self


@functools.lru_cache(maxsize=None)  # cache all arguments
def array_class_factory(
    scalar_class: AbstractModelicaScalarClass,
    sizes
):
    sizes_str = [
        "flexible" if size_str == ":" else size_str
        for size_str in map(str, sizes)
    ]

    array_class_name = "{}_Array_{}".format(
        scalar_class.__name__,
        '_'.join(sizes_str),
    )

    array_class_meta_name = f"{array_class_name}_Meta"
    
    @property
    def sizes_property(cls):
        return sizes
    
    @property
    def scalar_class_property(cls):
        return scalar_class

    array_class_meta = type(
        array_class_meta_name,
        (AbstractModelicaArrayClass,),
        {
            "sizes": sizes_property,
            "scalar_class": scalar_class_property
        },
    )

    array_class = array_class_meta(
        array_class_name,
        (ModelicaArrayObject,),
        {},
    )

    return array_class
