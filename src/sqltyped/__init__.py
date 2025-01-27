from __future__ import annotations

from enum import Enum

__version__ = "0.0.1"


class Adapter(str, Enum):
    sqlite = "sqlite"
    duckdb = "duckdb"
    postgres = "postgres"


class OutputModelType(str, Enum):
    PydanticV2BaseModel = "pydantic_v2.BaseModel"
