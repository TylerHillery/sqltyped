<div align="center">

# SQLTyped - Type Safe SQL in Python

*Craft type-safe SQL queries effortlessly in Python*

[![Test](https://github.com/tylerhillery/sqltyped/workflows/Test/badge.svg)](https://github.com/tylerhillery/sqltyped/actions?query=workflow%3ATest)
[![Coverage](https://coverage-badge.samuelcolvin.workers.dev/tylerhillery/sqltyped.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/tylerhillery/sqltyped)
[![GitHub](https://img.shields.io/github/license/tylerhillery/sqltyped)](https://github.com/tylerhillery/sqltyped/blob/main/LICENSE)
[![Development Status](https://img.shields.io/badge/Development%20Status-Concept-red)](https://github.com/tylerhillery/sqltyped)

</div>

___

> **Note:** SQLTyped is currently in the conceptual stage. This project is primarily a learning exercise and hobby project for the author. It is not intended for production use now or in the future.

## What is SQLTyped?

SQLTyped is a Python library that provides type safety for raw SQL queries.

**SQLTyped** is based on Python typed annotations, and powered by [Pydantic](https://docs.pydantic.dev/latest/) and [SQLAlchemy](https://www.sqlalchemy.org/)

## Inspiration

SQLTyped draws inspiration from several libraries and tools:
- [TypedSQL by Prisma](https://www.prisma.io/blog/announcing-typedsql-make-your-raw-sql-queries-type-safe-with-prisma-orm): Type-Safe SQL queries in TypeScript
- [squirrel](https://github.com/giacomocavalieri/squirrel): Type-Safe SQL queries in Gleam
- [Yesql](https://github.com/krisajenkins/yesql): Raw SQL query management in Clojure
- [aiosql](https://github.com/nackjicholson/aiosql): Raw SQL query management in Python
- [SQLModel](https://github.com/fastapi/sqlmodel): Showcasing the integration of SQLAlchemy with Pydantic
