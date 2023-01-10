from ast import Module, unparse
from typing import Protocol, Type

from arpeggio import visit_parse_tree
from pkg_resources import resource_string

from modelica_language import ParserPython

from ._peg_syntax import PEGSyntax
from ._peg_visitor import ModuleVisitor


class SupportsSyntax(Protocol):
    def __init__(self) -> None:
        ...


Syntax: Type[SupportsSyntax]


def get_peg_parser() -> ParserPython:
    return ParserPython(
        language_def=PEGSyntax.grammar,
        comment_def=PEGSyntax.COMMENT,
    )


def test_peg_syntax() -> None:
    parser = get_peg_parser()
    parse_tree = parser.parse(
        resource_string(__name__, "v3-4.peg").decode("ASCII")
    )
    module: Module = visit_parse_tree(
        parse_tree=parse_tree, visitor=ModuleVisitor(class_name="Syntax")
    )
    exec(unparse(module), globals())
    Syntax()  # noqa: F821
