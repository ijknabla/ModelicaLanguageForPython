import argparse
import sys
from typing import TextIO


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o", "--output", type=argparse.FileType("w"), default=sys.stdout
    )

    args = parser.parse_args()
    output: TextIO = args.output

    print("# flake8: noqa", file=output)


if __name__ == "__main__":
    main()
