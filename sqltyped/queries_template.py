import os
from sqlalchemy import Engine, text
from pathlib import Path
from typing import Any

QUERIES_DIR = Path(os.path.abspath(__file__)).parent


class Queries:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def execute(self, sql_file: Path, **params: Any) -> Any:
        with open(sql_file, "r") as f:
            sql = f.read()
        with self.engine.connect().execution_options(
            isolation_level="AUTOCOMMIT"
        ) as conn:
            result = conn.execute(text(sql), params)
        return result

    # The following will be filled in programmatically:
    # def method_name(self, **params: Any) -> Any:
    #     return self.execute(QUERIES_DIR / "file_name.sql", **params)
