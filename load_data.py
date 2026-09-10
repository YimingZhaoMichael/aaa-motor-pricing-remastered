import pandas as pd
import sqlite3


policies = pd.read_csv("data/raw/fremtpl2_freq.csv")

policies = policies.rename(columns={
    "IDpol": "policy_id",
    "ClaimNb": "claim_nb",
    "Exposure": "exposure",
    "Area": "area",
    "VehPower": "veh_power",
    "VehAge": "veh_age",
    "DrivAge": "driv_age",
    "BonusMalus": "bonus_malus",
    "VehBrand": "veh_brand",
    "VehGas": "veh_gas",
    "Density": "density",
    "Region": "region",
})
policies["policy_id"] = policies["policy_id"].astype("int64")

print(policies.head())

claims = pd.read_csv("data/raw/fremtpl2_sev.csv")

claims = claims.rename(columns={
    "IDpol": "policy_id",
    "ClaimAmount": "claim_amount",
})

print(claims.head())

with sqlite3.connect("data/portfolio.db") as connection:
    connection.execute("DELETE FROM policies")
    policies.to_sql("policies", connection, if_exists="append", index=False)
    print("Loaded policies into the database")

    row_count = connection.execute("SELECT COUNT(*) FROM policies").fetchone()[0]
    print(f"Policies in database: {row_count}")

    connection.execute("DELETE FROM claims")
    claims.to_sql("claims", connection, if_exists="append", index=False)
    print("Loaded claims into the database")

    row_count = connection.execute("SELECT COUNT(*) FROM claims").fetchone()[0]
    print(f"Claims in database: {row_count}")