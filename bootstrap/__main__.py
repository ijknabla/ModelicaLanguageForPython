import argparse
import sys
from typing import TextIO

from modelica_language import ParserPython

from ._peg_syntax import PEGSyntax


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("peg", type=argparse.FileType("r"))
    parser.add_argument(
        "-o", "--output", type=argparse.FileType("w"), default=sys.stdout
    )

    args = parser.parse_args()
    peg: TextIO = args.peg
    output: TextIO = args.output

    peg_parser = ParserPython(
        language_def=PEGSyntax.grammar,
        comment_def=PEGSyntax.COMMENT,
    )
    peg_parser.parse(peg.read())

    print("# flake8: noqa", file=output)


if __name__ == "__main__":
    main()
