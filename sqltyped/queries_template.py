import os
from pathlib import Path
from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel

QUERIES_DIR = Path(os.path.abspath(__file__)).parent

T = TypeVar("T", bound="SqlTypedModel")


class SqlTypedModel(BaseModel):
    @classmethod
    def from_tuple(cls: Type[T], tup: tuple) -> T:
        return cls(**{col: val for col, val in zip(cls.model_fields.keys(), tup)})


# hardcoding some models until I can auto generate them
class GetUsers(SqlTypedModel):
    id: int
    name: str
    age: int


class GetUserByName(SqlTypedModel):
    id: int
    name: str
    age: int


def model_factory(model: Type[T]):
    # cursor factory expects this function signature but we dont need it
    # because our model will already have the fields parsed and in the same order
    # as the row result
    def factory(cursor, row):
        return model.from_tuple(row)

    return factory


class Queries:
    def __init__(self, cursor) -> None:
        self.cursor = cursor

    def execute(
        self,
        sql_file: Path,
        model: Type[T],
        size: Union[int, None] = None,
        params: Union[Dict[str, Any], None] = None,
    ) -> Union[List[T], None]:
        with open(sql_file, "r") as f:
            sql = f.read()

        # handle when none type is returned as it currently errors out
        # object has no attribute from tuple
        self.cursor.row_factory = model_factory(model)
        if params:
            cursor = self.cursor.execute(sql, params)
        else:
            cursor = self.cursor.execute(sql)
        return cursor.fetchmany(size) if size else cursor.fetchall()
