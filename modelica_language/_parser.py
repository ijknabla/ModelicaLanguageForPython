__all__ = ("ParserPython",)

import builtins
import functools
import types
import typing
from typing import Any

import arpeggio

_builtins__isinstance = builtins.isinstance


@functools.wraps(_builtins__isinstance)
def _callable_is_instance_of_function(obj: Any, class_or_tuple: Any) -> bool:
    if class_or_tuple is types.FunctionType:  # noqa: E721
        class_or_tuple = typing.Callable
    return _builtins__isinstance(obj, class_or_tuple)


class ParserPython(arpeggio.ParserPython):
    @functools.wraps(arpeggio.ParserPython._from_python)
    def _from_python(self, *args: Any, **kwargs: Any) -> Any:
        try:
            builtins.isinstance = _callable_is_instance_of_function
            return super()._from_python(*args, **kwargs)
        finally:
            builtins.isinstance = _builtins__isinstance
