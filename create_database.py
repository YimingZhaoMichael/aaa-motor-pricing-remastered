from pathlib import Path
import sqlite3


data_directory = Path("data")
data_directory.mkdir(exist_ok=True)

schema = Path("sql/schema.sql").read_text(encoding="utf-8")
database = data_directory / "portfolio.db"

with sqlite3.connect(database) as connection:
    connection.executescript(schema)

print(f"Created database at {database}")
connection.close()