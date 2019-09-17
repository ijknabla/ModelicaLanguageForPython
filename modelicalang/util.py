
__all__ = (
    "Forward",
    "replace_all",
)

from typing import Sequence, Tuple


class Forward:
    def __init__(self, value=None):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def implement(self, value):
        self.__value = value
        return value

    __lshift__ = implement

    def __enter__(self):
        return self.value

    def __exit__(
        self,
        exc_type, exc_value,
        traceback
    ):
        return False


def replace_all(
    string: str,
    old_new_pairs: Sequence[Tuple[str, str]]
):
    result = string
    for old, new in old_new_pairs:
        result = result.replace(old, new)
    return result
