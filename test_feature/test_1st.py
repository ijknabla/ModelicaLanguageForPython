from .syntax import v3_4


def test_syntax() -> None:
    assert isinstance(v3_4(), str)
