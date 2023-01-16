import pytest
from arpeggio import ParserPython

from modelica_language import ModelicaVersion, get_file_parser


@pytest.fixture(scope="module")
def file_parser() -> ParserPython:
    return get_file_parser(ModelicaVersion.v3_4)
