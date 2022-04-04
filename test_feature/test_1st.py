from .syntax import v3_4


def test_syntax():
    assert isinstance(v3_4(), str)
