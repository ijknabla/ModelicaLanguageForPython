
__all__ = (
    # base type
    "PrimitiveModelicaObject",
    # concrete types
    "PrimitiveReal",
    "PrimitiveInteger",
    "PrimitiveBoolean",
    "PrimitiveString",
)

import numpy
import enum
from .. import util
from .abc import AbstractModelicaScalarClass

RealType = numpy.double
IntegerType = numpy.intc
StringType = str


class ScalarNumberMeta(
    AbstractModelicaScalarClass,
):
    def __new__(mtcls, name, bases, namespace):
        base_class_forward = util.Forward()
        def newfunc(cls, *args, **kwrds):
            with base_class_forward as base_class:
                self = super(base_class, cls).__new__(
                    cls, *args, **kwrds
                )
            
            if not isinstance(self, cls):
                raise ValueError(
                    f"{self}: {type(self)} is not instance of {cls}"
                )

            return self

        namespace["__new__"] = newfunc

        cls = base_class_forward << (
            super(ScalarNumberMeta, mtcls).__new__(
                mtcls,
                name,
                bases,
                namespace,
            )
        )

        return cls


class ModelicaEnumClassMeta(
    enum.EnumMeta,
    AbstractModelicaScalarClass,
):
    def __getitem__(cls, indices):
        if isinstance(indices, str):
            return enum.EnumMeta.__getitem__(
                cls, indices,
            )
        else:
            return AbstractModelicaScalarClass.__getitem__(
                cls, indices,
            )


class PrimitiveModelicaObject(
    metaclass=AbstractModelicaScalarClass,
):
    pass


@PrimitiveModelicaObject.register
class PrimitiveReal(
    RealType,
    metaclass=ScalarNumberMeta
):
    pass


@PrimitiveModelicaObject.register
class PrimitiveInteger(
    IntegerType,
    metaclass=ScalarNumberMeta,
):
    pass


class PrimitiveBooleanMeta(
    ModelicaEnumClassMeta,
):
    def __call__(cls, value):
        return super().__call__(bool(value))


@PrimitiveModelicaObject.register
class PrimitiveBoolean(
    enum.Enum,
    metaclass=PrimitiveBooleanMeta,
):
    true = True
    false = False

    def __bool__(self):
        return self.value
    
    def __eq__(self, other):
        return bool(self) == other
    
    def __repr__(self):
        return self.__str__()
    
    def __format__(self, format_spec):
        value = "true" if self else "false"
        return f"{value:{format_spec}}"


class PrimitiveString(
    str,
    PrimitiveModelicaObject,
):
    def __format__(self, format_spec):
        replaced = util.replace_all(
            self,
            [
                ("\\", r"\\"),
                ('\"', r'\"'),
                ("\a", r"\a"),
                ("\b", r"\b"),
                ("\f", r"\f"),
                ("\n", r"\n"),
                ("\t", r"\t"),
                ("\v", r"\v"),
            ],
        )

        double_quoted = f'"{replaced}"'
    
        return f"{double_quoted:{format_spec}}"
