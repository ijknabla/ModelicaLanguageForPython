
__all__ = (
    "AbstractModelicaObject",
    "AbstractModelicaClass",
)

import abc


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
