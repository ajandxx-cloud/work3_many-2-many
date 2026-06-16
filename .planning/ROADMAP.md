# Roadmap: TR_E_Bidirectional_MeetingPoint_DRT_Experiment_Rebuild

**Milestone:** v1.0 Evidence-chain rebuild
**Mode:** standard

## Phase 0: Repository and Manuscript Audit

**Status:** Complete with caveats - 2026-06-15

**Goal:** Understand the current code, manuscript, data, experiment outputs, and claim provenance before running any new experiments.

**Requirements:** AUD-01, AUD-02, AUD-03

**Success Criteria:**
1. Every current result in the manuscript is mapped to a script/data artifact or marked not reproducible.
2. Every headline manuscript claim is classified by current evidence strength.
3. Existing code modules, experiment scripts, result files, and manuscript sections are indexed.
4. Review-note weaknesses are captured as explicit risks and gates.
5. No new experiments are run before this phase passes.

**Outputs:**
- `.planning/phases/00-repository-and-manuscript-audit/00_REPOSITORY_AUDIT.md`
- `.planning/phases/00-repository-and-manuscript-audit/00_MANUSCRIPT_CLAIM_AUDIT.md`
- `.planning/phases/00-repository-and-manuscript-audit/00_CURRENT_EXPERIMENT_MAP.md`
- `.planning/phases/00-repository-and-manuscript-audit/00-01-SUMMARY.md`
- `.planning/phases/00-repository-and-manuscript-audit/00-VERIFICATION.md`
- `.planning/STATE.md`

## Phase 1: Literature and Novelty Audit

**Status:** Complete - 2026-06-15

**Goal:** Prevent overclaiming and rebuild a defensible TR-E contribution.

**Requirements:** POS-01, POS-02, POS-03

**Success Criteria:**
1. DARP with meeting points, pickup/dropoff walking locations, choice-based DRT, rolling-horizon DRT, and ALNS literature are audited.
2. No "first" claim remains unless verified under a precise scope.
3. Contribution is reframed as integrated choice-aware dynamic service design.
4. Target journal and story positioning are resolved.

**Outputs:**
- `01_LITERATURE_AUDIT.md`
- `01_NOVELTY_POSITIONING.md`
- `01_REVISED_RESEARCH_QUESTIONS.md`
- updated `.planning/CLAIMS_AND_RISKS.md`

## Phase 2: Experimental Contract and Metric Standardization

**Goal:** Define fair comparisons and prevent metric ambiguity.

**Requirements:** EXP-01, EXP-02, EXP-03, EXP-04, MET-01, MET-02, MET-03

**Success Criteria:**
1. Method taxonomy separates service design, passenger response, routing algorithm, and diagnostic role.
2. Choice-based and deterministic experiment families are separated.
3. Coverage-confounding controls are specified.
4. Every metric has a formula, denominator, unit, and interpretation.

**Outputs:**
- `02_EXPERIMENT_CONTRACT.md`
- `02_BASELINE_TAXONOMY.md`
- `02_METRICS_DEFINITIONS.md`
- `02_COVERAGE_CONFOUNDING_PLAN.md`
- `02_STATISTICAL_PLAN.md`

## Phase 3: Passenger Choice Model Rebuild

**Status:** Complete - 2026-06-15

**Goal:** Make passenger response credible, interpretable, and sensitivity-tested.

**Requirements:** CHO-01, CHO-02, CHO-03, CHO-04

**Success Criteria:**
1. Utility model includes service ASC or equivalent attractiveness term.
2. Outside option and passenger-type parameters are documented.
3. Sensitivity grid covers walk, wait, IVT, fare, ASC, outside option, and type shares.
4. Utility-component logs explain acceptance results.

**Outputs:**
- `03_PARAMETER_CALIBRATION.md`
- `03_CHOICE_MODEL_CONTRACT.md`
- choice model tests
- utility logging artifacts

## Phase 4: Baseline and Algorithm Implementation Check

**Goal:** Ensure all baselines and algorithms are implemented consistently before pilot runs.

**Requirements:** ALG-01, ALG-02, ALG-03, ALG-04

**Success Criteria:**
1. All required baselines run on a small scenario.
2. Behavioral variants use consistent passenger-response assumptions.
3. Deterministic diagnostics are separate.
4. Feasibility, route commitment, ALNS, and MILP diagnostic scope are verified.
5. Output schema is identical across methods and records failure rows.

**Outputs:**
- `04_IMPLEMENTATION_AUDIT.md`
- `04_BASELINE_VALIDATION.md`
- `04_ALGORITHM_VALIDATION.md`
- unit or integration test logs

## Phase 5: Pilot Experiments

**Goal:** Run small experiments to detect bugs and sanity-check results without creating final claims.

**Requirements:** REP-03

**Success Criteria:**
1. All core methods run successfully on 3 to 5 pilot seeds.
2. Metrics are internally consistent and have no impossible values.
3. Matched-coverage and fixed accepted-set logic are smoke-tested.
4. Bugs are recorded and fixed before formal experiments.

**Outputs:**
- `05_PILOT_RESULTS.md`
- pilot CSV/JSON files
- pilot plots
- bug list
- updated `.planning/STATE.md`

## Phase 6: Formal Synthetic Experiments

**Goal:** Generate the main reproducible evidence base.

**Requirements:** EXP-05

**Success Criteria:**
1. At least 20 paired synthetic seeds are run, preferably 30 if runtime permits.
2. Baseline behavioral, deterministic routing, matched-coverage, utility sensitivity, walking/meeting-point density, fleet/demand, rolling-horizon, equity, and algorithm validation experiments are completed.
3. Raw results, processed results, configs, seeds, logs, and failure rows are saved.
4. Main tables include confidence intervals and paired differences.

**Outputs:**
- `06_FORMAL_SYNTHETIC_RESULTS.md`
- raw and processed result files
- main tables
- confidence intervals and statistical tests
- plots

## Phase 7: Semi-Real or Beijing-Inspired Case Study

**Status:** Complete - 2026-06-16

**Goal:** Provide external validity beyond controlled synthetic tests, without mislabeling synthetic data as real.

**Requirements:** CASE-01, CASE-02

**Success Criteria:**
1. Real/semi-real data availability is decided.
2. If real data are unavailable, the case remains explicitly Beijing-inspired synthetic.
3. Case-study claims match the data quality.
4. Qualitative patterns are compared against synthetic findings.

**Outputs:**
- `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07_DATA_AUDIT.md`
- `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07_CASE_STUDY_RESULTS.md`
- `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07_CASE_CLAIM_BOUNDARY.md`
- `.planning/phases/07-semi-real-or-beijing-inspired-case-study/07-VERIFICATION.md`
- Bounded limitation notes: current case material is Beijing-inspired synthetic, not real or semi-real Beijing evidence.

## Phase 8: Evidence Synthesis and Claim Gate

**Goal:** Decide what the paper can honestly claim.

**Requirements:** CLM-01, CLM-02, CLM-03, MET-04

**Success Criteria:**
1. Every manuscript claim links to formal evidence.
2. Claims are classified strong, moderate, exploratory, or unsupported.
3. Unsupported claims are removed or rewritten.
4. Coverage, acceptance, and equity trade-offs are explicit.

**Outputs:**
- `08_CLAIM_EVIDENCE_MATRIX.md`
- `08_SUPPORTED_CLAIMS.md`
- `08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md`
- revised abstract bullets
- revised conclusion bullets

## Phase 9: Manuscript Restructure for TR Part E

**Goal:** Turn the experiment into a high-quality TR-E manuscript structure.

**Requirements:** MS-01, MS-02

**Success Criteria:**
1. Manuscript story is conditional rather than "our method always wins."
2. Introduction, literature, method, experiment, policy, limitations, and conclusion sections reflect the claim gate.
3. Tables and figures report fair comparison families and correct metrics.
4. Policy implications are simulation-based managerial insights.

**Outputs:**
- `09_TR_E_MANUSCRIPT_STRUCTURE.md`
- `09_REVISED_ABSTRACT.md`
- `09_REVISED_INTRODUCTION_PLAN.md`
- `09_EXPERIMENT_SECTION_PLAN.md`
- `09_TABLE_FIGURE_PLAN.md`

## Phase 10: Reproducibility Package and Final Verification

**Goal:** Prepare the project for paper writing and peer review.

**Requirements:** REP-01, REP-02

**Success Criteria:**
1. Reviewer/coauthor can regenerate main tables and figures.
2. Config, data, result, and claim manifests are complete.
3. All final claims match artifacts.
4. Final artifact index is ready.

**Outputs:**
- `10_REPRODUCIBILITY.md`
- `10_RESULT_MANIFEST.md`
- `10_FINAL_VERIFICATION.md`
- final artifact index

---
*Roadmap created: 2026-06-15*
