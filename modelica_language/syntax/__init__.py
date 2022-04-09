import functools
import pkg_resources


@functools.lru_cache(1)
def v3_4() -> str:
    return pkg_resources.resource_string(__name__, "v3-4.peg").decode("ASCII")
