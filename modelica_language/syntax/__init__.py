__all__ = ("v3_4",)

from pkg_resources import resource_string


def v3_4() -> str:
    return resource_string(__name__, "v3-4.peg").decode("ascii")
