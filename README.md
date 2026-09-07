# Motor Pricing Remastered

A from-scratch learning project that builds a motor-insurance pricing platform while documenting how each component works.

The project is being developed incrementally: a file or dependency is added only when it solves the current problem. The finished scope is recorded in [ROADMAP.md](ROADMAP.md).

## Current state

The project currently:

1. Uses `download_data.py` to fetch the freMTPL2 policy-frequency dataset from OpenML.
2. Inspects its columns, types, missing values, duplicate IDs, fractional policy IDs, and exposure range.
3. Saves the source data locally at `data/raw/fremtpl2_freq.csv`.
4. Defines an empty `policies` table in `sql/schema.sql` based on the inspected data.
5. Uses `create_database.py` to create `data/portfolio.db` and execute the schema.
6. Uses `load_data.py` to read the saved CSV, match the SQL column names, convert policy IDs to integers, and insert the rows.
7. Prints the SQL row count after loading; the first import was independently verified at 678,013 rows.
8. Excludes the virtual environment and generated data from Git through `.gitignore`.

## Run the current project

From the repository root:

```powershell
.\.venv\Scripts\python.exe .\download_data.py
.\.venv\Scripts\python.exe .\create_database.py
.\.venv\Scripts\python.exe .\load_data.py
```

The first command downloads and profiles the policy data. The second executes `sql/schema.sql`, dropping and recreating the `policies` table. The third loads the saved CSV into that empty table.

If the CSV is already saved, skip the download and run the last two commands in order. Recreating the table removes its existing rows. Running the loader alone on an already populated table fails because the same primary-key IDs cannot be inserted twice. The loader currently expects the schema to have been created first; automatic validation and rebuild orchestration remain future work.

Database-build output:

```text
Created database at data\portfolio.db
Loaded policies into the database
Policies in database: 678013
```

## Current files

- `requirements.txt` records the external Python packages required so far.
- `download_data.py` downloads, profiles, and saves the policy dataset.
- `sql/schema.sql` defines the empty `policies` table.
- `create_database.py` creates the database and executes the schema.
- `load_data.py` reads the saved policy CSV, inserts it into SQLite, and reports the stored row count.
- `.gitignore` prevents the virtual environment, generated data, and Python cache files from being committed.

## Next step

Verify the complete create-then-load sequence, then continue toward loading claim data. Add validation and repeatable rebuild handling as the workflow develops. Original exposure values remain unchanged until the cleaning stage.
