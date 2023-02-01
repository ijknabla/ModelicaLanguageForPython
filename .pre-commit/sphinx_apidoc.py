from pathlib import Path
from subprocess import run

import click

SPHINX_APIDOC_OPTIONS = ["--maxdepth=2", "--separate", "--module-first"]


@click.command()
@click.option(
    *("--module", "module_path"),
    required=True,
    type=click.types.Path(exists=True, path_type=Path),
)
@click.option(
    *("--output", "output_path"),
    required=True,
    type=click.types.Path(
        exists=True, file_okay=False, dir_okay=True, path_type=Path
    ),
)
def main(
    module_path: Path,
    output_path: Path,
) -> None:
    for rst in output_path.rglob("*.rst"):
        rst.unlink()
    run(
        [
            "sphinx-apidoc",
            *SPHINX_APIDOC_OPTIONS,
            f"{module_path}",
            "--output",
            f"{output_path}",
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
