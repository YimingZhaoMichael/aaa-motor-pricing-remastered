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
6. Uses `load_data.py` to read the saved CSV, match the SQL column names, convert policy IDs to integers, and replace the existing policy rows while preserving the table definition.
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

For the first build, create the table before running the loader. Once the CSV and table exist, rerun just `load_data.py` to reload policies. It executes `DELETE FROM policies` to remove the existing rows, then uses `to_sql(..., if_exists="append", index=False)` to insert the CSV rows. This preserves the primary key and other SQL constraints and prevents duplicate rows from accumulating across successful runs.

Running `create_database.py` again drops and recreates the `policies` table, so follow it with the loader to restore the data. Automatic input validation, failure-recovery guarantees, and complete rebuild orchestration remain future work.

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
- `load_data.py` reads the saved policy CSV, replaces the rows in the existing SQLite table, and reports the stored row count.
- `.gitignore` prevents the virtual environment, generated data, and Python cache files from being committed.

## Next step

Download and inspect the claim-severity dataset before designing its SQL table and extending the loader. Original policy exposure values remain unchanged until the cleaning stage.
