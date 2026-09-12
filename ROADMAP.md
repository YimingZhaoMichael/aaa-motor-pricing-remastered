# Motor Pricing Remastered — Roadmap

This project recreates a complete motor-insurance pricing platform from scratch. Each component will be understood, written, run, and checked before the next component is added. Future implementation files and folders will be created only when their milestone begins.

## Final objective

Build a reproducible project that downloads genuine motor-insurance data, stores and cleans it, analyses insurance experience, constructs technical premiums, compares pricing models, communicates results through reports and a dashboard, and can be rebuilt through one tested command.

## Milestones

### 1. Database foundation

- [x] Create a local SQLite database from Python.
- [x] Inspect the source policy columns before designing their table.
- [x] Add the empty `policies` table.
- [x] Load policy rows and verify the resulting table (678,013 rows).
- [x] Add the `claims` table with an automatically generated `claim_id` primary key and repeatable policy IDs.
- [x] Assess a separate `regions` table: deferred because existing policy region codes suffice and no enrichment source is currently needed.
- [ ] Add relationships and useful indexes when the queries justify them.
- [ ] Inspect and verify the database structure.

### 2. Source data

- [x] Download the freMTPL2 policy-frequency dataset from OpenML.
- [x] Download the freMTPL2 claim-severity dataset.
- [x] Inspect claim column types, missing values, and repeated policy IDs; save the original claim CSV locally.
- [x] Save the original policy CSV locally without committing it.
- [x] Record the Python packages required to reproduce the download.
- [x] Profile the policy data's shape, types, missing values, duplicate IDs, and exposure range.

### 3. Load data into SQL

- [x] Read the saved policy CSV with Python.
- [x] Match policy column names to SQL and convert whole-number policy IDs to integers.
- [x] Insert policies into SQLite and verify the policy row count.
- [x] Make successful policy reloads repeatable by deleting existing rows before inserting the saved CSV, preserving the table definition.
- [x] Read and rename the claim CSV columns, then insert claims into SQLite with generated claim IDs.
- [x] Replace existing claim rows before loading and verify 26,639 stored rows against the CSV.
- [ ] Load regions only if a separate table is justified.
- [x] Check claim policy IDs against policies: found 195 unmatched claim records across 6 absent policy IDs.
- [ ] Decide on foreign-key enforcement after handling unmatched claims in the analysis workflow.
- [ ] Make rebuilding the database safe and repeatable.

### 4. SQL exploration

- [x] Use `LEFT JOIN`, `IS NULL`, `COUNT`, `COUNT(DISTINCT ...)`, `GROUP BY`, and `HAVING` in `inspect_data.py` to inspect table relationships and claim-count differences.
- [ ] Calculate policy count, exposure, and claim count.
- [ ] Calculate claim frequency by driver age.
- [ ] Calculate claim severity by region.
- [ ] Compare vehicle and portfolio segments.
- [ ] Learn and apply joins, grouping, filtering, case expressions, and window functions.
- [ ] Save the analysis queries in the repository.

### 5. Extract and clean analysis data

- [ ] Produce one analysis row per policy.
- [ ] Join total claim amounts to policies.
- [ ] Cap exposure values above one.
- [ ] Investigate duplicate policy IDs.
- [x] Measure policy claim-count mismatches and separate zero-record cases from partial-record cases.
- [ ] Implement and document the analytical treatment of mismatching claim counts; inspection alone does not resolve them.
- [ ] Investigate zero, tiny, and extreme claim amounts.
- [ ] Record how many rows each cleaning decision affects.

### 6. Insurance experience study

- [ ] Calculate claim frequency: claims divided by exposure.
- [ ] Calculate claim severity: claim amount divided by claim count.
- [ ] Calculate pure premium: claim amount divided by exposure.
- [ ] Produce results by age, region, vehicle, fuel type, and area.
- [ ] Flag segments with insufficient exposure.
- [ ] Confirm that pure premium equals frequency multiplied by severity.

Metrics must be calculated from summed numerators and denominators, not by averaging individual policy ratios.

### 7. Technical premium and profitability

The source data contains no observed premium, so the project must construct one transparently.

- [ ] Add explicit expense and profit assumptions.
- [ ] Calculate technical premium.
- [ ] Calculate loss ratios.
- [ ] Identify the most and least profitable segments.
- [ ] Clearly document that premium is constructed rather than observed.

### 8. Pricing models

- [ ] Build a Poisson GLM for claim frequency with a log-exposure offset.
- [ ] Interpret model coefficients as pricing relativities.
- [ ] Build a severity model for claim amounts.
- [ ] Combine frequency and severity predictions.
- [ ] Build a Tweedie model if appropriate.
- [ ] Build an XGBoost benchmark.

### 9. Model validation

- [ ] Separate training and test data.
- [ ] Compare models using Poisson deviance.
- [ ] Produce lift or Gini analysis.
- [ ] Check predicted-versus-actual calibration.
- [ ] Compare predictive performance with interpretability.
- [ ] Document limitations and possible data leakage.

### 10. Reporting and dashboard

- [ ] Generate a deterministic management summary.
- [ ] Optionally generate an AI-assisted summary using only supplied metrics.
- [ ] Build an executive dashboard view.
- [ ] Build an actuarial risk-analysis view.
- [ ] Build a model-comparison view.
- [ ] Explain the same results to technical and non-technical audiences.

### 11. Automation and engineering quality

- [ ] Make one command rebuild the complete project.
- [ ] Add useful logging.
- [ ] Add unit tests using small hand-calculated examples.
- [ ] Add automated tests and code checks on GitHub.
- [ ] Write a data dictionary.
- [ ] Write model-validation documentation.
- [ ] Expand the README with results, instructions, and screenshots.

## Important data facts

- The downloaded policy-frequency data contains 678,013 rows and 12 columns.
- The claim-severity CSV and database table both contain 26,639 claim rows. Source columns are `IDpol` and `ClaimAmount`, with no missing values in the inspected data.
- Claim policy IDs have 1,689 repeated occurrences after the first. Repeated policy IDs can represent multiple claims and are not, by themselves, duplicate claim records.
- SQLite supplies `claims.claim_id` because it is declared `INTEGER PRIMARY KEY` and omitted from the inserted DataFrame. All loaded claim policy IDs were verified as stored integers.
- No policy fields are missing and no policy IDs are duplicated in this OpenML version.
- The policy-ID fractional-part check returned zero before integer conversion.
- The first policy import was verified at 678,013 database rows. The loader now deletes existing policy rows before inserting the saved CSV, so successful reloads replace the contents without duplicating IDs or recreating the table. The first-build order remains `create_database.py`, then `load_data.py`; subsequent policy reloads need only `load_data.py`.
- 1,224 policies have exposure above one; the original values are being preserved until the cleaning stage.
- Relationship inspection found 195 claim records across 6 IDs absent from policies: 2262511, 2277846, 2282134, 2286775, 2220367, and 2227533. No foreign key is defined yet.
- 9,117 distinct policies have fewer matching claim records than their reported `claim_nb`: 9,116 have zero matching records and 1 has a positive but lower matching count. No policy has more matching records than reported in this inspection.
- Exposure can incorrectly exceed one.
- Policy claim counts can disagree with individual claim records.
- Claim amounts are highly skewed and contain outliers.
- Some dataset versions may contain duplicate policy IDs.
- The dataset does not contain an observed premium column.

## Next session: analysis preparation

Relationship inspection was completed on 13 September 2026. The discrepancies do not establish whether policy counts are overstated, claim records are incomplete, or source inclusion rules differ. No source rows or counts have been corrected or excluded.

Proposed approach, not yet implemented:

1. Preserve the original policy and claim tables.
2. Build one analysis row per policy containing the reported count, matched claim-record count, total recorded claim amount, and mismatch flag. Aggregate claims by policy before joining so multiple claim rows do not multiply policy exposure.
3. Keep the 195 unmatched claims in the source table, but exclude them from policy-based pricing analysis because their policy characteristics and exposure are unavailable. Record their total amount as well as their count; the amount has not yet been measured.
4. Consider using reported policy counts for frequency and available claim records for severity, explicitly documenting source assumptions and possible missing records. Do not assume that combining estimates from differently selected populations is unbiased.
5. Do not treat missing claim amounts as zero cost for policies reporting claims. For an initial analysis requiring counts and amounts to agree, consider using policies with agreeing counts, while reporting exclusions and possible selection bias. Agreement alone does not prove the data is complete.
6. Inspect claim-amount ranges and decide on cleaning rules before modelling. Record the effect of each implemented decision.

The next coding step is the policy-level analysis dataset, one small query at a time. Automated validation, failure recovery, and full rebuild orchestration remain separate unfinished work.

## Working method

For each milestone:

1. Understand the problem.
2. Decide what new file is genuinely required.
3. Write the smallest working version.
4. Run it and inspect the output.
5. Explain what every relevant line does.
6. Update the README and this roadmap.
7. Commit and push the completed milestone.
