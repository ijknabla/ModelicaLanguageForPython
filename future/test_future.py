from pkg_resources import resource_string

from modelica_language import ParserPython

from ._peg_syntax import PEGSyntax


def get_peg_parser() -> ParserPython:
    return ParserPython(
        language_def=PEGSyntax.grammar,
        comment_def=PEGSyntax.COMMENT,
    )


def test_peg_syntax() -> None:
    parser = get_peg_parser()
    parser.parse(resource_string(__name__, "v3-4.peg").decode("ASCII"))
