<div align="center">

# SQLTyped - Type Safe SQL

*Craft type-safe SQL queries effortlessly*

[![GitHub](https://img.shields.io/github/license/tylerhillery/sqltyped)](https://github.com/tylerhillery/sqltyped/blob/main/LICENSE)
[![Development Status](https://img.shields.io/badge/Development%20Status-Concept-red)](https://github.com/tylerhillery/sqltyped)

</div>

___

> **Note:** SQLTyped is currently a POC. This project is primarily a learning exercise and hobby project for the author. It is not intended for production use now or in the future.

## What is SQLTyped?

SQLTyped is CLI tool that generates types for raw SQL queries. Give SQLTyped your queries, db connection and it'll handle the rest.

## Inspiration

SQLTyped draws inspiration from several libraries and tools:
- [TypedSQL by Prisma](https://www.prisma.io/blog/announcing-typedsql-make-your-raw-sql-queries-type-safe-with-prisma-orm): Type-Safe SQL queries in TypeScript
- [squirrel](https://github.com/giacomocavalieri/squirrel): Type-Safe SQL queries in Gleam
- [Yesql](https://github.com/krisajenkins/yesql): Raw SQL query management in Clojure
- [aiosql](https://github.com/nackjicholson/aiosql): Raw SQL query management in Python
- [sqlc](https://sqlc.dev/): Generates fully type-safe idiomatic Go code from SQL
- [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator/tree/main): Creates pydantic v1 and v2 model, dataclasses.dataclass, typing.TypedDict and msgspec.Struct from an openapi file and others.
