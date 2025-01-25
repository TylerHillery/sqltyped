import typer


def main() -> None:
    print("Hello World")


def sqltyped() -> None:
    """
    The main entrypoint for SQLTyped
    """
    typer.run(main)
