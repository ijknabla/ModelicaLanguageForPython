import argparse
import sys
from ast import Module
from typing import TextIO

from arpeggio import ParserPython, visit_parse_tree

from ._backport import unparse
from ._peg_syntax import PEGSyntax
from ._peg_visitor import ModuleVisitor


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("peg", type=argparse.FileType("r"))
    parser.add_argument("--class-name", default="Syntax")
    parser.add_argument(
        "-o", "--output", type=argparse.FileType("w"), default=sys.stdout
    )

    args = parser.parse_args()
    peg: TextIO = args.peg
    class_name: str = args.class_name
    output: TextIO = args.output

    with PEGSyntax:
        peg_parser = ParserPython(
            language_def=PEGSyntax.grammar,
            comment_def=PEGSyntax.COMMENT,
        )

    peg_source = peg.read()
    parse_tree = peg_parser.parse(peg_source)
    module: Module = visit_parse_tree(
        parse_tree=parse_tree,
        visitor=ModuleVisitor(class_name=class_name, source=peg_source),
    )

    print(unparse(module), file=output)


if __name__ == "__main__":
    main()
