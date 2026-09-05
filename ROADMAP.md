# Motor Pricing Remastered — Roadmap

This project recreates a complete motor-insurance pricing platform from scratch. Each component will be understood, written, run, and checked before the next component is added. Future implementation files and folders will be created only when their milestone begins.

## Final objective

Build a reproducible project that downloads genuine motor-insurance data, stores and cleans it, analyses insurance experience, constructs technical premiums, compares pricing models, communicates results through reports and a dashboard, and can be rebuilt through one tested command.

## Milestones

### 1. Database foundation

- [x] Create a local SQLite database from Python.
- [x] Create the `regions` table.
- [ ] Add the `policies` table.
- [ ] Add the `claims` table.
- [ ] Add relationships and useful indexes.
- [ ] Inspect and verify the database structure.

### 2. Source data

- [ ] Download the freMTPL2 policy-frequency dataset from OpenML.
- [ ] Download the freMTPL2 claim-severity dataset.
- [ ] Save the original CSV files locally without committing them.
- [ ] Record the Python packages required to reproduce the download.

### 3. Load data into SQL

- [ ] Read the CSV files with Python.
- [ ] Transform column names and data types.
- [ ] Insert regions, policies, and claims into SQLite.
- [ ] Verify row counts and table relationships.
- [ ] Make rebuilding the database safe and repeatable.

### 4. SQL exploration

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
- [ ] Reconcile policy claim counts with individual claim records.
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

- freMTPL2 contains approximately 678,000 policies.
- Policies and claims are connected by policy ID.
- Exposure can incorrectly exceed one.
- Policy claim counts can disagree with individual claim records.
- Claim amounts are highly skewed and contain outliers.
- Some dataset versions may contain duplicate policy IDs.
- The dataset does not contain an observed premium column.

## Working method

For each milestone:

1. Understand the problem.
2. Decide what new file is genuinely required.
3. Write the smallest working version.
4. Run it and inspect the output.
5. Explain what every relevant line does.
6. Update the README and this roadmap.
7. Commit and push the completed milestone.
