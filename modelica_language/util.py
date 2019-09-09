
__all__ = (
    "Forward",
)


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
