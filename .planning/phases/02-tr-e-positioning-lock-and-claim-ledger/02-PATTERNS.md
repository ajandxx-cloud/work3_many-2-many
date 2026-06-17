# Phase 2: TR-E Positioning Lock and Claim Ledger - Pattern Map

**Mapped:** 2026-06-17
**Files analyzed:** 3
**Analogs found:** 3 / 3

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md` | planning governance artifact | transform | `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md` | role-match |
| `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` | provenance ledger / claim model | traceability transform + file-I/O scan inventory | `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md` plus `experiments/formal_statistics.py` | role-match |
| `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` | risk register / blocker config | batch scan classification | `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md` plus `.planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md` | role-match |

## Pattern Assignments

### `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md` (planning governance artifact, transform)

**Analog:** `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md`

**Header and objective pattern** (lines 1-12):
```markdown
# TR-E Claim-Ready Milestone Plan

## Milestone Objective

Turn the current Work 3 DRT experiment repository into a Transportation
Research Part E manuscript package whose claims, tables, figures, and journal
positioning are traceable to formal Phase 6 evidence or explicitly labeled as
diagnostic, exploratory, or limited.

This milestone is claim-led. It does not tune parameters, fabricate numbers,
manually edit evidence, or promote non-canonical outputs into formal claims.
```

Copy this pattern for the positioning lock: short purpose first, then explicit "this is / this is not" boundary language. Replace milestone-wide scope with Phase 2 framing scope: allowed TR-E positioning, prohibited framing, core contribution sentence, and journal-fit rationale.

**Canonical evidence boundary pattern** (lines 13-31):
```markdown
## Canonical Evidence Boundary

Formal manuscript claims must trace to `results/formal/phase06/`.

Canonical formal evidence families:

| Evidence role | Canonical paths | Allowed use | Prohibited use |
|---------------|-----------------|-------------|----------------|
| Primary behavioral evidence | `results/formal/phase06/main_behavioral/raw_results.csv`, `results/formal/phase06/main_behavioral/processed_results.csv`, `results/formal/phase06/main_behavioral/metrics_table.csv`, `results/formal/phase06/tables/main_behavioral_table.csv`, `results/formal/phase06/tables/paired_differences.csv`, `results/formal/phase06/tables/paired_bootstrap_ci.csv` | Main conditional operational-efficiency and coverage-tradeoff claims after Phase 4 provenance checks. | Universal dominance, real-world validation, or final numerical claims before Phase 4. |
```

For `02_TR_E_POSITIONING_LOCK.md`, copy the same table shape but use framing families instead of raw evidence families:

| Framing family | Allowed wording | Prohibited wording | Downstream owner |
|----------------|-----------------|--------------------|------------------|
| TR-E contribution | `operational service-design evidence` and `passenger-response-aware simulation framework` | TR Part A policy validation, deployable decision tool, or optimization-method supremacy | Phase 3 |
| Passenger choice | service-design evaluation mechanism | empirically calibrated behavior or endogenous routing-control mechanism | Phase 3 |
| Beijing scenario | Beijing-inspired or semi-realistic synthetic grid | real-world Beijing validation | Phase 3/4 |
| Gamma | post-hoc welfare/sensitivity accounting | behavioral policy control or endogenous Pareto optimization | Phase 3/4 |
| MILP | simplified ex-post routing diagnostic | exact dynamic benchmark or ALNS near-optimality proof | Phase 3/4 |

**Gate language pattern** (lines 43-60):
```markdown
## Do Not Before Gate Rules

- Do not make major manuscript claim edits before Phase 2 creates the claim
  ledger and blockers/safe-claims table.
- Do not inject final percentages, improvement values, confidence intervals,
  significance language, or table/figure numbers before Phase 4 provenance
  checks.
- Do not use root legacy CSVs, smoke outputs, archive outputs, or ad hoc outputs
  as formal manuscript evidence unless a later phase explicitly audits and
  labels them.
```

The positioning lock should include a `Do Not Say` or `Prohibited Framing` section using the same imperative style. Include the specific prohibited families from Phase 2 decisions: co-optimization, policy-first contribution, universal dominance, real-world Beijing validation, endogenous Gamma/Pareto, full exact dynamic benchmark, and premature readiness.

**Failure routing and risk-class pattern** (lines 99-118):
```markdown
## Failure Routing

| Failure | Route |
|---------|-------|
| Missing canonical evidence path | Return to Phase 1 audit or Phase 4 provenance, depending on discovery point. |
| Unmapped or unsafe manuscript claim | Return to Phase 2 claim ledger and blockers/safe-claims table. |
| Manuscript prose needs TR-E repositioning without new numbers | Route to Phase 3. |

## Risk Classification

| Risk class | Meaning | Phase handling |
|------------|---------|----------------|
| Claim-critical blocker | Can invalidate a manuscript claim if unresolved. | Blocks related claim until downgraded, fixed, or documented. |
```

Copy this pattern for positioning-rule routing. The planner should create sections such as:

- `Allowed Core Contribution`
- `Prohibited Framing`
- `Evidence Role Boundaries`
- `Downstream Routing`
- `Safe Sentences Phase 3 May Use`

**Readiness-label boundary pattern** (lines 144-153):
```markdown
## Readiness Label Rules

The final report may say `TR-E submission-ready` only if all Phase 5 hard
readiness gates pass. Otherwise the readiness label must be one of:

- `TR-E near-ready with minor blockers`
- `not ready due to specific blockers`

Failures may be documented as non-impacting only when the report gives exact
commands, outputs, source paths, and manuscript-impact reasoning.
```

Apply this exact standard to any Phase 2 allowed-sentence language: do not let `02_TR_E_POSITIONING_LOCK.md` itself certify readiness.

**Supporting analog:** `.planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md`

**Evidence-role separation pattern** (lines 27-37):
```markdown
## Axis 2: Evidence Role

| Evidence role | How later phases use it | Boundary |
|---------------|-------------------------|----------|
| primary behavioral evidence | Phase 2 ledger maps main conditional claims; Phase 4 injects verified final values from `results/formal/phase06/main_behavioral/` and `results/formal/phase06/tables/`. | Must preserve coverage and passenger-response trade-offs. |
| matched-coverage diagnostic | Phase 2/3 label as diagnostic coverage-confounding check; Phase 4 verifies values if mentioned. | Not the primary headline estimate. |
| fixed-accepted-set diagnostic | Phase 2/3 label as fixed accepted set decomposition. | Not a complete dynamic benchmark. |
```

Use this table structure directly in `02_TR_E_POSITIONING_LOCK.md` if the planner wants an evidence-role section. Keep role names aligned with the Phase 2 enum: `positioning`, `mechanism_scope`, `primary_behavioral`, `diagnostic_matched_coverage`, `diagnostic_fixed_accepted_set`, `robustness_sensitivity`, `equity_type_heterogeneity`, `algorithm_diagnostic`, `limitation`, and `package_consistency`.

---

### `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` (provenance ledger / claim model, traceability transform + file-I/O scan inventory)

**Analog:** `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md`

**Claim-source inventory pattern** (lines 9-27):
```markdown
## Canonical Manuscript Sources

| Manuscript area | Path | Phase use |
|-----------------|------|-----------|
| Master document and journal metadata | `manuscript/main.tex` | Phase 3 updates TR-E metadata and includes; Phase 5 compiles. |
| Abstract | `manuscript/sections/abstract.tex` | Phase 3 rewrites non-numeric framing; Phase 4 injects verified final numbers. |
| Introduction and contributions | `manuscript/sections/intro.tex` | Phase 3 repositions contribution claims; Phase 4 injects verified final numbers. |
| Experiments | `manuscript/sections/experiments.tex` | Phase 3 separates evidence roles; Phase 4 verifies tables, figures, and numbers. |
| Implications | `manuscript/sections/policy.tex` | Phase 3 reframes as managerial/operational implications. |
| Conclusion | `manuscript/sections/conclusion.tex` | Phase 3 states conditional contribution; Phase 4 injects verified final numbers. |
```

For the claim ledger, convert this source inventory into occurrence rows. Use `manuscript_location` values like `manuscript/sections/abstract.tex:15` or `manuscript/sections/experiments.tex:170`.

**Evidence-role map pattern** (lines 40-48):
```markdown
| Evidence role | Source paths | Validation source | Allowed use | Prohibited use |
|---------------|--------------|-------------------|-------------|----------------|
| Primary behavioral evidence | `results/formal/phase06/main_behavioral/raw_results.csv`, `results/formal/phase06/main_behavioral/processed_results.csv`, `results/formal/phase06/main_behavioral/metrics_table.csv`, `results/formal/phase06/tables/main_behavioral_table.csv`, `results/formal/phase06/tables/paired_differences.csv`, `results/formal/phase06/tables/paired_bootstrap_ci.csv` | `results/formal/phase06/main_behavioral/validation_report.json` | Main conditional efficiency, coverage, acceptance, rejection, and denominator claims after Phase 4 provenance checks. | Universal dominance, equal-coverage dominance, or final numerical claims before Phase 4. |
| Matched-coverage diagnostic | `results/formal/phase06/coverage_controls/matched_coverage/raw_results.csv`, `results/formal/phase06/coverage_controls/matched_coverage/processed_results.csv`, `results/formal/phase06/tables/matched_coverage_paired_differences.csv` | `results/formal/phase06/coverage_controls/matched_coverage/validation_report.json` | Diagnostic explanation of coverage confounding and sensitivity to served-share matching. | Main headline estimate or proof of equal-service efficiency. |
| Fixed-accepted-set diagnostic | `results/formal/phase06/coverage_controls/fixed_accepted_set/raw_results.csv`, `results/formal/phase06/coverage_controls/fixed_accepted_set/processed_results.csv`, `results/formal/phase06/tables/fixed_accepted_set_paired_differences.csv` | `results/formal/phase06/coverage_controls/fixed_accepted_set/validation_report.json` | Diagnostic decomposition over fixed accepted sets. | Complete online behavioral benchmark or dynamic routing optimum. |
```

Each ledger row should copy this mapping into `source_path`, `evidence_role`, `allowed_sentence`, and `prohibited_sentence`. Do not cite root legacy files as `source_path` for formal claims.

**Generation and validation script map pattern** (lines 91-110):
```markdown
## Generation And Validation Scripts

| Script | Role |
|--------|------|
| `experiments/phase06_formal.py` | Formal main behavioral runner, manifests, aliases, and validation. |
| `experiments/formal_validation.py` | Main formal output validation helpers and denominator checks. |
| `experiments/formal_statistics.py` | Formal tables, plots, manifests, verification reports, synthesis validation, and markdown reports. |
| `experiments/phase06_coverage_controls.py` | Matched-coverage and fixed-accepted-set controls and validators. |
| `experiments/phase06_robustness.py` | Utility, density/radius, fleet stress, equity/type, and algorithm diagnostics packages. |
```

Use this table to populate `script_path` and `generation_command`. For manual positioning or limitation claims, use `script_path=not_applicable_manual_text` and `generation_command=not_applicable_manual_text`.

**Ledger header pattern to create**
```markdown
| claim_id | claim_family_id | manuscript_location | current_sentence | claim_type | comparison | metric | reported_value | source_path | supporting_source_path | script_path | generation_command | metric_formula | numerator | denominator | evidence_role | phase4_status | action | allowed_sentence | prohibited_sentence | notes |
```

Required columns from project constraints are included verbatim: `source_path`, `script_path`, `generation_command`, `metric_formula`, `numerator`, `denominator`, `evidence_role`, `allowed_sentence`, and `prohibited_sentence`.

**Durable ledger column pattern:** `experiments/formal_validation.py` lines 56-67:
```python
RERUN_LEDGER_COLUMNS = [
    "run_id",
    "config_id",
    "seed",
    "scale",
    "method",
    "status",
    "error",
    "reason",
    "fix",
    "rerun_result",
]
```

Do not copy this schema literally for claim rows, but copy the style: stable IDs first, context fields second, status/action fields last.

**Ledger write / de-duplication pattern:** `experiments/formal_validation.py` lines 204-253:
```python
def ensure_rerun_ledger(path: str | Path) -> Path:
    ledger_path = Path(path)
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    if not ledger_path.exists():
        with ledger_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=RERUN_LEDGER_COLUMNS)
            writer.writeheader()
    return ledger_path

def append_unresolved_failures_to_ledger(raw: pd.DataFrame, path: str | Path) -> Path:
    """Append failed/timeout main rows to the durable rerun ledger."""
    ledger_path = ensure_rerun_ledger(path)
    existing = _existing_ledger_keys(ledger_path)
    unresolved = raw[raw["status"].isin({"failed", "timeout"})]
```

The Markdown claim ledger is hand-authored, but the planner should use the same idea: stable unique claim keys and no silent duplicate rows. For occurrence rows, key by `claim_id`; group related rows with `claim_family_id`.

**Formal table generation pattern:** `experiments/formal_statistics.py` lines 280-385:
```python
def write_paired_differences(input_path: Path, output_dir: Path) -> Path:
    raw = _read_csv(input_path)
    frame = paired_difference_frame(raw, metrics=MAIN_METRICS)
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "paired_differences.csv"
    frame.to_csv(path, index=False)
    return path

def write_paired_bootstrap_ci(
    input_path: Path,
    output_dir: Path,
    *,
    seed: int = BOOTSTRAP_SEED,
    n_resamples: int = BOOTSTRAP_RESAMPLES,
) -> Path:
    raw = _read_csv(input_path)
    frame = _bootstrap_frame(raw, metrics=MAIN_METRICS, seed=seed, n_resamples=n_resamples)
```

Ledger rows for paired-difference or CI claims should cite:

- `source_path=results/formal/phase06/tables/paired_differences.csv` or `paired_bootstrap_ci.csv`
- `script_path=experiments/formal_statistics.py`
- `generation_command=$env:PYTHONPATH='src'; python -m experiments.formal_statistics --closeout --results-dir results/formal/phase06`

**Formal package manifest pattern:** `experiments/formal_statistics.py` lines 514-650:
```python
def package_manifest(results_dir: Path) -> list[dict]:
    specs = [
        {
            "package_id": "06-02_main_behavioral",
            "directory": results_dir / "main_behavioral",
            "raw": "raw_results.csv",
            "processed": "processed_results.csv",
            "config": "config_manifest.json",
            "seed": "seed_manifest.json",
            "run": "run_manifest.json",
            "validation": "validation_report.json",
            "evidence_role": "main_evidence",
        },
        {
            "package_id": "06-03_matched_coverage",
            "directory": results_dir / "coverage_controls/matched_coverage",
            "raw": "raw_results.csv",
            "processed": "processed_results.csv",
            "validation": "validation_report.json",
            "evidence_role": "main_evidence_control",
        },
```

Use this manifest as the authoritative source for `source_path` family selection. Convert its code-side labels into Phase 2 claim-ledger labels:

| Code-side role | Phase 2 ledger role |
|----------------|---------------------|
| `main_evidence` | `primary_behavioral` |
| `main_evidence_control` | `diagnostic_matched_coverage` |
| `diagnostic_evidence` with fixed accepted-set path | `diagnostic_fixed_accepted_set` |
| `diagnostic_evidence` with robustness path | `robustness_sensitivity` |
| `exploratory_limited_evidence` | `equity_type_heterogeneity` |
| `diagnostic_evidence` with algorithm path | `algorithm_diagnostic` |

**Metric denominator pattern:** `experiments/formal_validation.py` lines 153-190:
```python
n_requests = pd.to_numeric(completed["n_requests"], errors="coerce")
n_served = pd.to_numeric(completed["n_served"], errors="coerce")
vehicle_km = pd.to_numeric(completed["vehicle_km"], errors="coerce")
safe_requests = n_requests.where(n_requests > 0)
safe_served = n_served.where(n_served > 0)

expected_served_share = (n_served / safe_requests).fillna(0.0)
expected_vkm_original = (vehicle_km / safe_requests).fillna(0.0)
expected_vkm_served = (vehicle_km / safe_served).fillna(0.0)
expected_behavioral_acceptance = (
    1.0 - pd.to_numeric(completed["choice_rejection_rate"], errors="coerce")
)
rejection_sum = (
    pd.to_numeric(completed["served_share"], errors="coerce")
    + pd.to_numeric(completed["choice_rejection_rate"], errors="coerce")
    + pd.to_numeric(completed["feasibility_rejection_rate"], errors="coerce")
)
```

Copy these formulas into ledger `metric_formula`, `numerator`, and `denominator` fields for numerical claim rows. For non-numeric positioning rows, use `not_applicable`.

**Runtime metric formula pattern:** `experiments/metrics.py` lines 146-164:
```python
if records:
    acceptance_rate = len(accepted) / len(records)
    served_share = len(accepted) / len(records)
    choice_rejection_rate = len(choice_rejected) / len(records)
    feasibility_rejection_rate = len(feasibility_rejected) / len(records)
    behavioral_acceptance_rate = 1.0 - choice_rejection_rate
    vkm_per_original_request = result.total_vehicle_km / len(records)
else:
    acceptance_rate = 0.0
    served_share = 0.0
    behavioral_acceptance_rate = 0.0
    choice_rejection_rate = 0.0
    feasibility_rejection_rate = 0.0
    vkm_per_original_request = 0.0

vehicle_km = result.total_vehicle_km
vkm_per_served_trip = vehicle_km / len(accepted) if accepted else 0.0
```

**Accepted-trip denominator helper:** `experiments/metrics.py` lines 226-241:
```python
def vkm_per_trip(vehicle_km: float, n_requests: int, acceptance_rate: float) -> float:
    """Compute vehicle-km per accepted trip.

    Correct denominator: n_requests * acceptance_rate = accepted trip count.
    This is dimensionally consistent: km / trip.
    """
    accepted_trips = n_requests * acceptance_rate
```

This is the denominator source for any vkm per accepted/served trip claim. If the manuscript sentence says "per trip", the ledger should identify whether the denominator is served/accepted trips or original requests.

**Validation-result shape:** `experiments/formal_validation.py` lines 70-80:
```python
def _empty_result(results_dir: Path) -> dict:
    return {
        "passed": True,
        "schema_drift": False,
        "denominator_checks": {},
        "errors": [],
        "warnings": [],
        "row_counts": {},
        "checked_files": [],
        "results_dir": str(results_dir),
        "ledger_path": "",
    }
```

Use the same fields in ledger notes when citing validation support: `passed`, `schema_drift`, `denominator_checks`, `row_counts`, and `checked_files`.

**Formal closeout command pattern:** `experiments/formal_statistics.py` lines 1312-1320:
```python
commands = commands_run or [
    "$env:PYTHONPATH='src'; python -m experiments.formal_statistics --closeout --results-dir results/formal/phase06",
    "$env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06",
    "$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py tests/test_phase06_coverage_controls.py tests/test_phase06_robustness.py -q",
]
tables = generate_tables(results_dir, table_dir)
plots = write_plots(table_dir, plot_dir)
write_result_manifest(results_dir, phase_dir)
```

Ledger `generation_command` should use the exact command that creates or validates the artifact, not a vague script path.

**Synthesis validation pattern:** `experiments/formal_statistics.py` lines 1343-1366:
```python
def validate_synthesis(results_dir: Path = DEFAULT_RESULTS_DIR) -> dict:
    required = [
        results_dir / "tables/main_behavioral_table.csv",
        results_dir / "tables/paired_differences.csv",
        results_dir / "tables/paired_bootstrap_ci.csv",
        results_dir / "tables/supplementary_summary.csv",
        results_dir / "tables/critical_conflicts.csv",
        PHASE_DIR / "06_FORMAL_SYNTHETIC_RESULTS.md",
        results_dir / "phase06_result_manifest.json",
        results_dir / "phase06_verification_report.json",
    ]
    missing = [str(path) for path in required if not path.exists()]
    report = {
        "main_matrix_passed": _read_json(results_dir / "main_behavioral/validation_report.json").get("passed") is True,
        "paired_ci_present": (results_dir / "tables/paired_bootstrap_ci.csv").exists(),
        "supplementary_gates_present": (results_dir / "tables/supplementary_summary.csv").exists(),
        "missing_required_files": missing,
        "passed": not missing,
    }
```

For Phase 2, do not run synthesis as a gate unless the plan explicitly calls for it. Use this structure as a pattern for artifact completeness checks if the planner adds a lightweight schema check.

---

### `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` (risk register / blocker config, batch scan classification)

**Analog:** `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md`

**Risk appendix pattern** (lines 124-141):
```markdown
## Risk Appendix

| Risk | Impact class | Tracking notes |
|------|--------------|----------------|
| Part A framing in `README.md`, `CLAUDE.md`, `manuscript/main.tex`, `manuscript/references.bib`, cover/response letters, and figure-script comments | manuscript/package consistency risk | Route to Phase 3 for TR-E repositioning and Phase 5 package consistency checks. |
| Policy-first language in abstract, introduction, experiments, policy section, model, conclusion, and generated `results/policy_recommendations.md` | manuscript/package consistency risk | Reframe as managerial and operational implications; avoid policy-overreach. |
| Old values `18.3%`, `29.1%`, `35.0%`, and `0.1216` in manuscript text and legacy outputs | claim-critical blocker until Phase 4 | Track as high-priority values; do not replace or retain until Phase 4 verifies formal provenance. |
| Beijing wording could imply real-world validation | claim-critical blocker | Use Beijing-inspired or semi-realistic synthetic grid unless future public-data ingestion exists. |
```

Copy this table style, but expand it into two layers:

1. Rule table: one row per risk family.
2. Concrete hit table: one row per scanned hit or cluster, with `issue_id`, `location`, `matched_text_or_pattern`, `risk_family`, `status`, `evidence_role`, `owner_phase`, `required_action`, `allowed_replacement`, and `verification_check`.

**Wording-family scan list pattern:** `.planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md` lines 39-54:
```markdown
## Section-Level Wording Families For Scans

Later phases should scan for and replace or qualify these wording families:

- `Transportation Research Part A`
- `policy-first`
- `Policy Implications` when the section should become managerial or operational
- `real-world Beijing`
- `Beijing validation`
- `universal dominance`
- `dominates`
- `exact dynamic benchmark`
- `near-optimal`
- `endogenous Gamma`
- `Pareto frontier` when it implies behavior rather than post-hoc accounting
- `TR-E submission-ready` outside the Phase 5 final readiness report
```

Use this list as the blocker scan backbone. Add Phase 2 risk families from CONTEXT.md: old values, broad `outperforms`/`superior`/`improvement` wording, legacy result paths, and readiness wording.

**Concrete current-hit examples to record**
```text
manuscript/sections/abstract.tex:15-17
FullModel 18.3% vs. DoorToDoor 61.0% served share; 15.1 vkm/trip versus 21.3 vkm/trip; 29.1% improvement.

manuscript/sections/intro.tex:83-87
Empirical demonstration of a 29.1% per-trip vehicle-km gain; matched-coverage diagnostic indicating a 35.0% gain.

manuscript/sections/experiments.tex:170-187
Primary headline uses FullModel 18.3%, DoorToDoor 61.0%, 15.1 vs. 21.3 vkm/trip, 29.1% lower vkm/trip, and matched-coverage 35.0% diagnostic.

manuscript/sections/policy.tex:1-4
Section is named "Policy Implications".

manuscript/sections/policy.tex:209
Figure is described as a practical decision tool for Chinese city DRT deployment.
```

These hits should be blockers or downgrade-required items until Phase 3/4 routes them.

**Figure-script package consistency examples**
```text
manuscript/figures/scripts/fig04_baseline_comparison.py:1-4
FIG-04 script still says TR Part A format.

manuscript/figures/scripts/fig04_baseline_comparison.py:75-82
Script annotates an unverified efficiency-gain percentage.

manuscript/figures/scripts/fig07_pareto.py:1-7
Script titles output as a Pareto Frontier and reads a Gamma sweep.

manuscript/figures/scripts/fig07_pareto.py:21-29
Script reads root `results/pareto_gamma_sweep.csv`, not `results/formal/phase06/`.
```

Because figure scripts are package-facing risk sources in Phase 2, include these in `05_BLOCKERS_AND_SAFE_CLAIMS.md`, not the full occurrence-level `03_CLAIM_LEDGER.md`, unless a figure title/caption is reused in the manuscript.

**Diagnostic-control boundary pattern:** `experiments/phase06_coverage_controls.py` lines 1-12:
```python
"""Phase 6 coverage-confounding formal controls.

This module runs the two 06-03 control packages requested after the formal
06-02 main behavioral matrix:

* matched_coverage: cap each behavioral method to the same attainable served
  count within every seed x scale cell.
* fixed_accepted_set: route the same retained request set for every method as a
  diagnostic-only operating-efficiency comparison.

Outputs are intentionally isolated from 06-02 main evidence.
"""
```

Blocker rows about matched coverage or fixed accepted sets must carry the diagnostic qualifier in `allowed_replacement`.

**Matched-coverage row metadata pattern:** `experiments/phase06_coverage_controls.py` lines 558-586:
```python
return {
    "package_id": MATCHED_PACKAGE,
    "run_id": f"matched_coverage:synthetic_n{scale}_s{seed}:{method_label}",
    "config_id": f"matched_coverage:scale_{scale}:seed_{seed}",
    "choice_model": "binary_logit_with_matched_coverage_cap",
    "evidence_family": "supplementary_control",
    "diagnostic_role": "matched_coverage_control",
    "status": status,
    "detailed_reason": reason,
```

Use `diagnostic_matched_coverage` as Phase 2 `evidence_role`; do not use `primary_behavioral`.

**Fixed-accepted-set row metadata pattern:** `experiments/phase06_coverage_controls.py` lines 917-943:
```python
return {
    "package_id": FIXED_PACKAGE,
    "run_id": f"fixed_accepted_set:synthetic_n{scale}_s{seed}:{method_label}",
    "choice_model": "fixed_accepted_set",
    "evidence_family": "algorithm_diagnostic",
    "evidence_role": "diagnostic_only",
    "diagnostic_role": "fixed_accepted_set_routing",
    "status": status,
```

Use this for blocker wording around fixed accepted sets: "diagnostic decomposition over fixed accepted sets", not "benchmark" or "dynamic optimum".

**Robustness diagnostic boundary pattern:** `experiments/phase06_robustness.py` lines 1-6:
```python
"""Phase 6 Plan 06-04 robustness, sensitivity, and equity diagnostics.

The 06-04 packages are formal diagnostics, not headline evidence.  They reuse
the Phase 6 paired-seed conventions while keeping outputs isolated from the
06-02 main matrix and 06-03 coverage controls.
"""
```

Use this language in safe replacements for robustness, sensitivity, equity, and algorithm claims.

**Algorithm diagnostic validation pattern:** `experiments/phase06_robustness.py` lines 1251-1307:
```python
report = {
    "package_id": ALGORITHM_PACKAGE,
    "passed": True,
    "schema_drift": False,
    "denominator_checks": {"status": "not_applicable_algorithm_diagnostic"},
    "errors": [],
    "warnings": [],
    "row_counts": {},
    "checked_files": [],
}
```

For MILP/ALNS blocker rows, set `metric_formula`, `numerator`, and `denominator` to `not_applicable` unless the row cites a concrete gap metric. Set `evidence_role=algorithm_diagnostic`.

**Gate-result row pattern:** `experiments/phase06_robustness.py` lines 1452-1470:
```python
rows.append(
    {
        "package_id": package_id,
        "status": "passed" if report["passed"] else "blocked",
        "passed": report["passed"],
        "role": "formal_diagnostic",
        "output_path": str(root / package_id),
        "blocks_phase8": not report["passed"] or bool(report.get("warnings")),
        "evidence_family": (
            "algorithm_diagnostic"
            if package_id == ALGORITHM_PACKAGE
            else "formal_robustness_diagnostic"
        ),
        "summary": "; ".join(report.get("errors", []) or report.get("warnings", []) or ["structural validation passed"]),
    }
)
```

Use the same field semantics in `05_BLOCKERS_AND_SAFE_CLAIMS.md`: status, owner gate, required action, and verification check should be explicit.

## Shared Patterns

### Evidence Role Separation

**Source:** `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md` lines 19-27

Apply to all three Phase 2 files.

```markdown
| Evidence role | Canonical paths | Allowed use | Prohibited use |
|---------------|-----------------|-------------|----------------|
| Primary behavioral evidence | `results/formal/phase06/main_behavioral/raw_results.csv`, `results/formal/phase06/main_behavioral/processed_results.csv`, `results/formal/phase06/main_behavioral/metrics_table.csv`, `results/formal/phase06/tables/main_behavioral_table.csv`, `results/formal/phase06/tables/paired_differences.csv`, `results/formal/phase06/tables/paired_bootstrap_ci.csv` | Main conditional operational-efficiency and coverage-tradeoff claims after Phase 4 provenance checks. | Universal dominance, real-world validation, or final numerical claims before Phase 4. |
| Matched-coverage diagnostic | `results/formal/phase06/coverage_controls/matched_coverage/`, `results/formal/phase06/tables/matched_coverage_paired_differences.csv` | Diagnostic interpretation of coverage confounding. | Primary headline estimate or equal-coverage dominance claim. |
| Fixed-accepted-set diagnostic | `results/formal/phase06/coverage_controls/fixed_accepted_set/`, `results/formal/phase06/tables/fixed_accepted_set_paired_differences.csv` | Diagnostic routing/meeting-point decomposition for fixed accepted sets. | Complete dynamic benchmark claim. |
```

### Non-Canonical Source Handling

**Source:** `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md` lines 113-122

Apply to `03_CLAIM_LEDGER.md` and `05_BLOCKERS_AND_SAFE_CLAIMS.md`.

```markdown
| Source family | Paths/examples | Default status | Allowed handling |
|---------------|----------------|----------------|------------------|
| Smoke package | `results/formal/phase06/smoke/` | Excluded from formal evidence. | Mention only as non-canonical smoke/package sanity output. |
| Pilot outputs | `results/pilot/phase05/` | Non-canonical for formal claims. | Historical/pilot context only. |
| Root legacy outputs | `results/synthetic_results.csv`, `results/beijing_results.csv`, `results/metrics_table.csv`, `results/equity_table.csv`, `results/policy_recommendations.md`, `results/milp_gap.json` | Non-canonical by default. | Later audit can label historical or diagnostic; do not use as formal claims. |
```

### Validation Commands

**Source:** `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md` lines 72-77

Apply to `generation_command` and `verification_check` fields.

```powershell
$env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06
$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --results-dir results/formal/phase06/main_behavioral
$env:PYTHONPATH='src'; python -m experiments.phase06_coverage_controls --validate --package all
$env:PYTHONPATH='src'; python -m experiments.phase06_robustness --validate --package all
```

### Formal Manifest Fields

**Source:** `results/formal/phase06/phase06_result_manifest.json` lines 1-23

Use these fields when deciding whether a formal package is valid enough to cite.

```json
{
  "formal_smoke_excluded": true,
  "generated_at_utc": "2026-06-16T09:53:00.529202+00:00",
  "git_commit": "8e6c618",
  "packages": [
    {
      "completion_count": 320,
      "config_manifest": "results/formal/phase06/main_behavioral/config_manifest.json",
      "denominator_validation": "passed",
      "directory_path": "results/formal/phase06/main_behavioral",
      "evidence_role": "main_evidence",
      "package_id": "06-02_main_behavioral",
      "raw_result_file": "results/formal/phase06/main_behavioral/raw_results.csv",
      "validation_report": "results/formal/phase06/main_behavioral/validation_report.json",
      "validator_passed": true
    }
  ]
}
```

### Verification Report Fields

**Source:** `results/formal/phase06/phase06_verification_report.json` lines 43-66

Use these checks in ledger notes and blocker verification checks.

```json
{
  "check_id": "schema_drift_false_across_packages",
  "evidence": "schema_drift false in main, coverage, and robustness validation reports",
  "passed": true
},
{
  "check_id": "denominator_checks_passed",
  "evidence": "all non-algorithm denominator checks passed",
  "passed": true
},
{
  "check_id": "pilot_smoke_not_used_as_formal_evidence",
  "evidence": "manifest excludes smoke package",
  "passed": true
}
```

### Phase 2 Scan Commands

Apply to `05_BLOCKERS_AND_SAFE_CLAIMS.md` `verification_check` and `generation_command` fields for scan-derived rows.

```powershell
rg -n "18\.3|29\.1|35\.0|0\.1216" manuscript README.md CLAUDE.md
rg -n "Transportation Research Part A|TR Part A|TR-A|Part A" manuscript README.md CLAUDE.md
rg -n "policy|Policy Implications|decision tool|recommendation" manuscript README.md CLAUDE.md
rg -n "Gamma|gamma|Pareto|welfare" manuscript README.md CLAUDE.md manuscript/figures/scripts
rg -n "Beijing|real-world|validation|semi-realistic" manuscript README.md CLAUDE.md
rg -n "MILP|exact|near-optimal|optimality gap|benchmark" manuscript README.md CLAUDE.md
rg -n "dominates|dominance|outperform|outperforms|superior|improvement|gain" manuscript README.md CLAUDE.md
```

### Status And Action Enums

Apply to `03_CLAIM_LEDGER.md` and `05_BLOCKERS_AND_SAFE_CLAIMS.md`.

```text
status: safe | safe_with_qualifier | downgrade_required | blocker
action: retain_with_verification | replace_non_numeric | delete | downgrade_to_diagnostic | move_to_limitation | phase4_verify_number
owner_phase: Phase 3 | Phase 4 | Phase 5 | future/v2
```

### Safe Placeholder Pattern

Apply to every Phase 2 safe replacement sentence with evidence-dependent values.

```text
[PHASE4_VERIFIED_VALUE]
[PHASE4_VERIFIED_CI]
[PHASE4_VERIFIED_TABLE]
[PHASE4_VERIFIED_FIGURE]
```

Do not write final percentages, confidence intervals, significance claims, table numbers, or figure numbers in Phase 2 replacement sentences.

## No Analog Found

No Phase 2 file is completely without analog. There is no existing occurrence-level manuscript claim ledger, so `03_CLAIM_LEDGER.md` must combine these role-match analogs:

| Needed Pattern | Source |
|----------------|--------|
| Manuscript source map | `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md` |
| Evidence-role boundaries | `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md` and `01_REPO_AND_EVIDENCE_AUDIT.md` |
| Ledger identity/status style | `experiments/formal_validation.py` rerun ledger helpers |
| Metric formulas and denominators | `experiments/metrics.py` and `experiments/formal_validation.py` |
| Formal table provenance | `experiments/formal_statistics.py` and `results/formal/phase06/tables/*.csv` |

## Metadata

**Analog search scope:** `.planning/milestones/tr_e_claim_ready/`, `.planning/phases/`, `experiments/`, `results/formal/phase06/`, `manuscript/sections/`, `manuscript/figures/scripts/`, `README.md`, `CLAUDE.md`

**Files scanned:** 30+ planning, code, manuscript, figure-script, CSV, and JSON artifacts.

**Project skills:** No repo-local `.codex/skills/` or `.agents/skills/` directories were found.

**Pattern extraction date:** 2026-06-17
