from pathlib import Path
from sklearn.datasets import fetch_openml


policies = fetch_openml(data_id=41214, as_frame=True).frame

print("Policies preview:")
print(policies.head())

print("\nDataset size:")
print(policies.shape)

print("\nColumn types:")
print(policies.dtypes)

print("\nMissing values count:")
print(policies.isna().sum())

print("\nDuplicate IDs:")
print(policies["IDpol"].duplicated().sum())

print("\nIDs that are decimals:")
print((policies["IDpol"] % 1 != 0).sum())

print("\nExposure range:")
print(policies["Exposure"].min(), policies["Exposure"].max())

print("\nPolicies with exposure above 1:")
print((policies["Exposure"] > 1).sum())

raw_data_directory = Path("data/raw")
raw_data_directory.mkdir(parents=True, exist_ok=True)

policies.to_csv(
    raw_data_directory / "fremtpl2_freq.csv",
    index=False,
)

claims = fetch_openml(data_id=41215, as_frame=True).frame

print("\nClaims preview:")
print(claims.head())

print("\nColumn types:")
print(claims.dtypes)

print("\nMissing values count:")
print(claims.isna().sum())

print("\nDuplicate IDs:")
print(claims["IDpol"].duplicated().sum())

claims.to_csv(
    raw_data_directory / "fremtpl2_sev.csv",
    index=False,
)