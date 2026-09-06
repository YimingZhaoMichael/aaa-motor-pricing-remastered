# Motor Pricing Remastered

A from-scratch learning project that builds a motor-insurance pricing platform while documenting how each component works.

The project is being developed incrementally: a file or dependency is added only when it solves the current problem. The finished scope is recorded in [ROADMAP.md](ROADMAP.md).

## Current state

The project currently:

1. Uses `download_data.py` to fetch the freMTPL2 policy-frequency dataset from OpenML.
2. Inspects its columns, types, missing values, duplicate IDs, and exposure range.
3. Saves the source data locally at `data/raw/fremtpl2_freq.csv`.
4. Defines an empty `policies` table in `sql/schema.sql` based on the inspected data.
5. Uses `create_database.py` to create `data/portfolio.db` and execute the schema.
6. Excludes the virtual environment and generated data from Git through `.gitignore`.

## Run the current project

From the repository root:

```powershell
.\.venv\Scripts\python.exe .\download_data.py
.\.venv\Scripts\python.exe .\create_database.py
```

The first command downloads and profiles the policy data. The second rebuilds the SQLite database from `sql/schema.sql`.

Database-build output:

```text
Created database at data\portfolio.db
```

## Current files

- `requirements.txt` records the external Python packages required so far.
- `download_data.py` downloads, profiles, and saves the policy dataset.
- `sql/schema.sql` defines the empty `policies` table.
- `create_database.py` creates the database and executes the schema.
- `.gitignore` prevents the virtual environment, generated data, and Python cache files from being committed.

## Next step

Write a loader that reads the saved policy CSV, performs only the necessary name and type conversions, and inserts the rows into the empty `policies` table.
