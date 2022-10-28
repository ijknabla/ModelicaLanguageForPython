from functools import wraps
from typing import Callable, Dict, TypeVar

T_1 = TypeVar("T_1")
T_2 = TypeVar("T_2")


def assert_injective(f: Callable[[T_1], T_2]) -> Callable[[T_1], T_2]:
    ys: Dict[T_2, T_1] = {}

    @wraps(f)
    def wrapped(x: T_1) -> T_2:
        y = f(x)
        assert y not in ys or x == ys[y]
        ys[y] = x
        return y

    return wrapped
