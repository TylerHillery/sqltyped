import argparse
import re
from pathlib import Path
from typing import List, NamedTuple


class QueryParam(NamedTuple):
    name: str
    t: str


class QueryMetadata(NamedTuple):
    file_name: str
    query_name: str
    description: str
    model: str
    params: List[QueryParam]


def parse_sql_file(file_path: Path) -> QueryMetadata:
    with open(file_path, "r") as f:
        content = f.read()
    # TODO: verify all this regex
    desc_match = re.search(r"--\s*description:\s*(.+)", content)
    # TODO: this doesn't account for having multiple parameters i.e. int | float
    # TODO: need to handle all the valid dbapi 2.0 formats
    #       only one is required per DB-API
    #           - qmark, numeric, named, format, pyformat
    param_matches = re.findall(r"--\s*param:\s*(\w+)\s*\((\w+)\)", content)

    description = desc_match.group(1) if desc_match else "No description in sql file"
    params = [QueryParam(name=name, t=t) for name, t in param_matches]
    query_name = file_path.stem.replace(" ", "_")

    return QueryMetadata(
        file_name=file_path.name,
        query_name=query_name,
        description=description,
        model=query_name.title().replace("_", ""),
        params=params,
    )


def get_queries(dir: Path) -> list[QueryMetadata]:
    queries = [parse_sql_file(path) for path in dir.rglob("*.sql")]
    if not queries:
        raise ValueError(f"No queries found in {dir}")
    return queries


def generate_method(metadata: QueryMetadata) -> str:
    param_str = ", ".join(f"{param.name}: {param.t}" for param in metadata.params)
    param_dict = ", ".join(f'"{param.name}": {param.name}' for param in metadata.params)

    # TODO: not a big fan of this, need to better account for params an no params
    required_params = (
        "self, *, size: Union[int, None] = None, "
        if param_str
        else "self, *, size: Union[int, None] = None"
    )
    params_arg = f", {{{param_dict}}}" if param_dict else ""

    return f'''
    def {metadata.query_name}({required_params}{param_str}) -> Union[List[{metadata.model}], None]:
        """
        {metadata.description}
        """
        return self.execute(QUERIES_DIR / "{metadata.file_name}", {metadata.model}, size{params_arg})
    '''


def generate_output_file(output_file: Path) -> None:
    with open(Path(__file__).parent / "queries_template.py", "r") as template_file:
        template_content = template_file.read()

    with open(output_file, "w") as file:
        file.write(template_content)
        for query in get_queries(output_file.parent):
            file.write(generate_method(query))

    init_file = output_file.parent / "__init__.py"
    if not init_file.exists():
        with open(init_file, "w") as file:
            file.write(f"from .{output_file.stem} import Queries\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate SQL Queries Class")
    parser.add_argument(
        "--directory", "-d", default="./sql", help="Directory to search for SQL files"
    )
    parser.add_argument("--output", "-o", default="queries.py", help="Output file name")
    args = parser.parse_args()

    # TODO: Add checks to see if directory exists and is valid
    # TODO: Add checks that the output is a .py file and not named sql
    dir = Path(args.directory).resolve()
    output_file = dir / args.output
    generate_output_file(output_file)


if __name__ == "__main__":
    main()
