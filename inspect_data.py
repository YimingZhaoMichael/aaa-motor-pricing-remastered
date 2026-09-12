import sqlite3

connection = sqlite3.connect("data/portfolio.db")

counts = connection.execute("""
    SELECT COUNT(*), COUNT(DISTINCT claims.policy_id)
    FROM claims
    LEFT JOIN policies
        ON claims.policy_id = policies.policy_id
    WHERE policies.policy_id IS NULL
""").fetchone()

print(f"There are {counts[0]} claims without a matching policy from {counts[1]} distinct policy IDs.")

mismatches = connection.execute("""
    SELECT policies.policy_id, policies.claim_nb, COUNT(claims.claim_id)
    FROM policies
    LEFT JOIN claims
        ON policies.policy_id = claims.policy_id
    GROUP BY policies.policy_id, policies.claim_nb
    HAVING policies.claim_nb != COUNT(claims.claim_id)
""").fetchall()

more_claims = 0
less_claims = 0
zero_actual_claims = 0

for policy, reported, actual in mismatches:
    if actual > reported:
        more_claims += 1
    else:
        less_claims += 1

    if actual == 0:
        zero_actual_claims += 1

print(f"There are {len(mismatches)} policies with mismatching claim count and reported number of claims; out of which {more_claims} have more claims than reported, {less_claims} have less.")
print(f"Out of those policies with mismatching number of claims, {zero_actual_claims} of them had ZERO claim records.")

connection.close()