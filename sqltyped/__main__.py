import argparse
from pathlib import Path
from typing import Dict


def get_queries(dir: Path) -> list[Dict[str, Path]]:
    queries = [{path.stem.replace(" ", "_"): path} for path in dir.rglob("*.sql")]
    if not queries:
        raise ValueError(f"No queries found in {dir}")
    return queries


def generate_output_file(output_file: Path) -> None:
    with open(Path(__file__).parent / "queries_template.py", "r") as template_file:
        template_content = template_file.read()

    with open(output_file, "w") as file:
        file.write(template_content)
        for query in get_queries(output_file.parent):
            for name, path in query.items():
                # TODO: Add some sort ability to get typed params, like Prisma TypedSQL does
                file.write(f"""
    def {name}(self, **params) -> Any:
        return self.execute(QUERIES_DIR / "{path.name}", **params)
""")

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
