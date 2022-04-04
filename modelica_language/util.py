__all__ = ("replace_all",)

from typing import Sequence, Tuple


def replace_all(string: str, old_new_pairs: Sequence[Tuple[str, str]]):
    result = string
    for old, new in old_new_pairs:
        result = result.replace(old, new)
    return result
