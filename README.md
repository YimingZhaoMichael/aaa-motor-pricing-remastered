# Motor Pricing Remastered

A from-scratch learning project that builds a motor-insurance pricing platform while documenting how each component works.

The project is being developed incrementally: a file or dependency is added only when it solves the current problem. The finished scope is recorded in [ROADMAP.md](ROADMAP.md).

## Current state

The project currently:

1. Defines a `regions` table in `sql/schema.sql`.
2. Uses `create_database.py` to read and execute that SQL.
3. Creates a local SQLite database at `data/portfolio.db`.
4. Excludes the generated database from Git through `.gitignore`.

## Run the current project

From the repository root:

```powershell
py -3.11 create_database.py
```

Expected output:

```text
Created database at data\portfolio.db
```

## Current files

- `sql/schema.sql` defines the database structure.
- `create_database.py` creates the database and executes the schema.
- `.gitignore` prevents generated data and Python cache files from being committed.

## Next step

Add the `policies` and `claims` tables, their relationships, and useful indexes to `sql/schema.sql`; then rebuild and inspect the database.

