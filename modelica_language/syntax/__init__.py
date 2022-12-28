__all__ = ("v3_4_peg",)

from pkg_resources import resource_string


def v3_4_peg() -> str:
    return resource_string(__name__, "v3-4.peg").decode("ascii")
