TODO
- [ ] fix sending params to execute when there aren't any
- [ ] Add parameters parsing for all valid python DB API Formats:
    - [ ] qmark
    - [ ] numeric
    - [ ] named
    - [ ] format
    - [ ] pyformat
- [ ] parameters with multiple return types
- [ ] Add database type --> target type conversion for following databases
    - [ ] SQLite
    - [ ] DuckDB
    - [ ] Postgres
    - [ ] MySQL
- [ ] Codegen for various models
    - [ ] pydantic_v2 BaseModel
    - [ ] dataclasses
    - [ ] typeddict
- [ ] Ability to auto update generated files as changes happen to db or queries
- [ ] Figure out how to implement all the cursor methods
    Priority
    - [ ] execute
    - [ ] fetchone
    - [ ] fetchall
    Later
    - [ ] executemany
