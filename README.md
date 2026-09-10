# Motor Pricing Remastered

A from-scratch learning project that builds a motor-insurance pricing platform while documenting how each component works.

The project is being developed incrementally: a file or dependency is added only when it solves the current problem. The finished scope is recorded in [ROADMAP.md](ROADMAP.md).

## Current state

The project currently:

1. Uses `download_data.py` to fetch the freMTPL2 policy-frequency (41214) and claim-severity (41215) datasets from OpenML.
2. Inspects its columns, types, missing values, duplicate IDs, fractional policy IDs, and exposure range.
3. Inspects claim column types, missing values, and repeated policy IDs, and saves both datasets at `data/raw/fremtpl2_freq.csv` and `data/raw/fremtpl2_sev.csv`.
4. Defines `policies` and `claims` tables in `sql/schema.sql` based on the inspected data. SQLite generates each claim row's `claim_id`; claim `policy_id` values may repeat.
5. Uses `create_database.py` to create `data/portfolio.db` and execute the schema.
6. Uses `load_data.py` to read both saved CSVs, match the SQL column names, convert policy-dataset IDs to integers, and replace existing rows in both tables while preserving their definitions.
7. Prints SQL row counts after loading; both counts were independently verified against the CSVs: 678,013 policies and 26,639 claims.
8. Excludes the virtual environment and generated data from Git through `.gitignore`.

## Run the current project

From the repository root:

```powershell
.\.venv\Scripts\python.exe .\download_data.py
.\.venv\Scripts\python.exe .\create_database.py
.\.venv\Scripts\python.exe .\load_data.py
```

The first command downloads, profiles, and saves both datasets. The second executes `sql/schema.sql`, dropping and recreating both tables. The third loads the saved CSVs into those tables.

For the first build, create the tables before running the loader. Once both CSVs and tables exist, rerun just `load_data.py` to reload them. For each table it executes `DELETE FROM` to remove existing rows, then uses `to_sql(..., if_exists="append", index=False)` to insert the CSV rows. This preserves primary keys and other SQL constraints and prevents rows from accumulating across successful runs. The claims DataFrame omits `claim_id`, which SQLite supplies automatically; this is a local row identifier, not a source claim number.

Running `create_database.py` again drops and recreates both tables, so follow it with the loader to restore the data. Automatic input validation, failure-recovery guarantees, and complete rebuild orchestration remain future work.

Database-build output:

```text
Created database at data\portfolio.db
Loaded policies into the database
Policies in database: 678013
Loaded claims into the database
Claims in database: 26639
```

## Current files

- `requirements.txt` records the external Python packages required so far.
- `download_data.py` downloads, profiles, and saves the policy and claim datasets.
- `sql/schema.sql` defines the empty `policies` and `claims` tables.
- `create_database.py` creates the database and executes the schema.
- `load_data.py` reads both saved CSVs, replaces the rows in their existing SQLite tables, and reports each stored row count.
- `.gitignore` prevents the virtual environment, generated data, and Python cache files from being committed.

## Next step

Use SQL to check whether every claim policy ID exists in `policies`, then compare claim-record counts with each policy's `claim_nb`. These relationships have not yet been verified or enforced with a foreign key. Inspect claim amounts and reconcile the datasets before constructing one analysis row per policy and applying documented cleaning rules. Original values remain unchanged until that stage.

A separate `regions` table is deferred: policies already contain region codes, and no additional region data or validation need currently justifies another table.
