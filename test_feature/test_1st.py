from arpeggio import ParserPython
import pytest

from .parser import comment, grammar
from .syntax import v3_4


def test_syntax() -> None:
    assert isinstance(v3_4(), str)


dialects = [
    "",
    """
IDENT |= r"\\$\\w*"
    """,
    """
file: stored-definition @EOF@
    """,
]


@pytest.mark.parametrize("dialect", dialects)
def test_parser(dialect: str) -> None:
    parser = ParserPython(grammar, comment)
    parser.parse(v3_4() + dialect)
