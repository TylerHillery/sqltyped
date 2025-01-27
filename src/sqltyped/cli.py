import logging
from pathlib import Path
from typing import Union

import typer
from rich import print
from typing_extensions import Annotated

from sqltyped import Adapter, OutputModelType, __version__
from sqltyped.logging import setup_logging

app = typer.Typer(rich_markup_mode="rich")

logger = logging.getLogger(__name__)


def version_callback(value: bool) -> None:
    if value:
        print(f"SQLTyped CLI version: [green]{__version__}[/green]")
        raise typer.Exit()


@app.callback()
def callback(
    version: Annotated[
        Union[bool, None],
        typer.Option(
            "--version", help="Show the version and exit.", callback=version_callback
        ),
    ] = None,
    verbose: Annotated[
        bool, typer.Option("--verbose/--silent", help="Enable verbose output")
    ] = False,
) -> None:
    """
    SQLTyped CLI - The [bold]sqlt[/bold] command line app.

    Generate types for your raw SQL queries. Give SQLTyped your queries, a db connection and it'll handle the rest.

    Read more in the docs: [link=][/link].
    """

    log_level = logging.DEBUG if verbose else logging.INFO

    setup_logging(level=log_level)


@app.command()
def generate(
    *,
    db_file: Annotated[
        Union[Path, None],
        typer.Option(
            help="The file path to the database",
            show_default=False,
            exists=True,
            dir_okay=False,
        ),
    ] = None,
    db_conn: Annotated[
        Union[str, None],
        typer.Option(
            help="Connection string to connect to database e.g. for Postgres this would be the DSN",
            show_default=False,
        ),
    ] = None,
    adapter: Annotated[
        Adapter,
        typer.Option(
            "--adapter",
            "-a",
            help="Provide the type of dataseb you're connecting to",
            show_default=False,
        ),
    ] = "sqlite",
    host: Annotated[
        Union[str, None],
        typer.Option("--host", "-h", help="The database host", show_default=False),
    ] = None,
    port: Annotated[
        Union[int, None],
        typer.Option(
            "--port", "-p", help="The port of the database", show_default=False
        ),
    ] = None,
    user: Annotated[
        Union[str, None],
        typer.Option("--user", "-U", help="The database user", show_default=False),
    ] = None,
    password: Annotated[
        Union[str, None],
        typer.Option(
            help="The database password",
            prompt=True,
            hide_input=True,
            show_default=False,
        ),
    ] = None,
    database: Annotated[
        Union[str, None],
        typer.Option("--database", "-d", help="The database name", show_default=False),
    ] = None,
    queries: Annotated[
        Union[Path, None],
        typer.Option(
            "--queries", "-q", help="Directory with SQL queries or single sql file"
        ),
    ] = "./queries",
    output: Annotated[
        Union[Path, None],
        typer.Option(
            "--output",
            "-o",
            help="Specify output directory for generated type models. Defaults to the queries directory if provided, otherwise uses current working directory.",
            show_default=False,
            dir_okay=False,
        ),
    ] = None,
    output_model_type: Annotated[
        Union[OutputModelType, None],
        typer.Option(
            "--output-model-type", "-m", help="The model type to generate the code as"
        ),
    ] = OutputModelType.PydanticV2BaseModel,
) -> None:
    """
    Generate type-safe models from raw SQL queries using the provided database connection and options.
    """


def main() -> None:
    app()


# Other ideas (--dry-run, --verbose, --silent, )
