---
phase: 02-tr-e-positioning-lock-and-claim-ledger
verified: 2026-06-17T11:00:51Z
status: passed
score: 14/14 must-haves verified
overrides_applied: 0
---

# Phase 2: TR-E Positioning Lock and Claim Ledger Verification Report

**Phase Goal:** Define the safe TR-E framing and complete the claim ledger before editing prose.
**Verified:** 2026-06-17T11:00:51Z
**Status:** passed
**Re-verification:** No - initial verification

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | `02_TR_E_POSITIONING_LOCK.md` states allowed TR-E framing and prohibited framing. | VERIFIED | Required sections found at lines 16, 29, 52, 75, 111, and 173; file includes allowed/prohibited framing tables and readiness boundary. |
| 2 | The manuscript has a locked TR-E logistics and operations positioning before prose edits begin. | VERIFIED | Positioning lock states this is a TR-E logistics and operations artifact and locks operational service-design evidence before manuscript rewriting. |
| 3 | Allowed framing is conditional, operational, and evidence-bounded. | VERIFIED | Allowed framing table uses `operational service-design evidence`, tested synthetic service-design conditions, trade-offs, and Phase 4 numerical gating. |
| 4 | Prohibited framing blocks policy-first, universal dominance, real-world validation, endogenous Gamma, co-optimization, and exact dynamic benchmark claims. | VERIFIED | Prohibited list explicitly blocks policy validation, universal dominance, real-world Beijing validation, endogenous Gamma/Pareto, co-optimization, and MILP/ALNS exactness claims. |
| 5 | Evidence roles separate primary evidence, diagnostics, robustness, equity/type heterogeneity, algorithm diagnostics, and limitations. | VERIFIED | Role labels appear across lock, ledger, and blocker docs; ledger contains all required role enums and row-level role usage. |
| 6 | `03_CLAIM_LEDGER.md` maps current and planned manuscript claims with required provenance fields. | VERIFIED | Ledger has 68 `C-###` rows; each row has 21 cells, no blank cells, and mandatory columns for source, script, command, formula, numerator, denominator, evidence role, allowed sentence, and prohibited sentence. |
| 7 | Every target manuscript file is represented in a coverage inventory. | VERIFIED | Coverage inventory includes `manuscript/main.tex` and all eight `manuscript/sections/*.tex` files with reviewed ranges and claim IDs. |
| 8 | Numerical/Table/Figure seed hits from the manuscript are represented in the ledger. | VERIFIED | Re-ran seed scan; `numeric_seed_hits=168`, `missing_seed_hits=0`. |
| 9 | Allowed replacement sentences defer unverified numerical content to Phase 4. | VERIFIED | `[PHASE4_VERIFIED_VALUE]`, `[PHASE4_VERIFIED_CI]`, `[PHASE4_VERIFIED_TABLE]`, `[PHASE4_VERIFIED_FIGURE]`, and `phase4_verify_number` are present; no old values appear in `allowed_sentence` cells. |
| 10 | `05_BLOCKERS_AND_SAFE_CLAIMS.md` distinguishes safe, qualified safe, downgraded, and blocker statuses. | VERIFIED | Claim status enum defines exactly `safe`, `safe_with_qualifier`, `downgrade_required`, and `blocker`; blocker table has 18 populated `B-###` rows. |
| 11 | Prohibited wording families have concrete scan-backed hit rows and owner-phase routing. | VERIFIED | Risk family rules cover old numbers, Part A/TR-A, policy, dominance, Gamma/Pareto, Beijing, MILP, legacy paths, readiness, diagnostics, and package consistency; concrete rows include owner phase and verification check. |
| 12 | Package-facing and figure-script risks are tracked without over-ledgering them as manuscript claims. | VERIFIED | Blocker rows B-005, B-007, B-009, B-011, B-016, and B-017 track README, CLAUDE, cover/response, and figure-script risks as package consistency or provenance risks. |
| 13 | Phase 2 did not edit manuscript, results, source, experiments, analysis, README, CLAUDE, or dependency files. | VERIFIED | `git diff --name-only -- manuscript results src experiments analysis README.md CLAUDE.md pyproject.toml` returned no paths; seven Phase 2 commits touched only the three planning artifacts. |
| 14 | Decision coverage, Phase 1 regression, and schema drift gates are satisfied. | VERIFIED | D-01 through D-49 are all present in Phase 2 plans; Phase 1 verification is `passed`; Phase 1 doc gate checks still pass; formal reports show `schema_drift: false`. |

**Score:** 14/14 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `.planning/milestones/tr_e_claim_ready/02_TR_E_POSITIONING_LOCK.md` | Allowed/prohibited TR-E framing, core contribution, journal-fit rationale, safe sentences, evidence-role boundaries, routing, readiness boundary. | VERIFIED | `gsd-sdk verify.artifacts` passed; required phrases and sections found. |
| `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` | Occurrence-level claim ledger and manuscript coverage inventory with provenance and denominator fields. | VERIFIED | 68 complete claim rows; 168/168 seed hits represented; formal sources cite `results/formal/phase06/`. |
| `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` | Claim-critical blockers, safe claims, downgraded claims, prohibited wording, package risks, verification checks. | VERIFIED | 18 complete blocker rows; required statuses and risk families present. |

### Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| `02_TR_E_POSITIONING_LOCK.md` | `02-CONTEXT.md` | D-08 through D-14 and D-23 through D-29 | WIRED | `gsd-sdk verify.key-links` found the required context pattern. |
| `02_TR_E_POSITIONING_LOCK.md` | `01_REPO_AND_EVIDENCE_AUDIT.md` | evidence-role boundary table | WIRED | Required role patterns found. |
| `03_CLAIM_LEDGER.md` | `manuscript/main.tex` and `manuscript/sections/*.tex` | `source_path` and `manuscript_location` | WIRED | Coverage inventory and row locations include all target manuscript files. |
| `03_CLAIM_LEDGER.md` | `results/formal/phase06/` | formal `source_path` fields | WIRED | Formal claim rows cite canonical Phase 6 paths. |
| `03_CLAIM_LEDGER.md` | `experiments/formal_validation.py` and `experiments/metrics.py` | metric formula/numerator/denominator fields | WIRED | Formula references include `served_share`, `vkm_per_served_trip`, and rejection-rate formulas. |
| `05_BLOCKERS_AND_SAFE_CLAIMS.md` | `03_CLAIM_LEDGER.md` | `claim_family_id` and `evidence_role` references | WIRED | Risk rows and family rules reference ledger families and evidence roles. |
| `05_BLOCKERS_AND_SAFE_CLAIMS.md` | README, CLAUDE, package files, figure scripts | package-consistency and provenance-risk rows | WIRED | Package-facing hit rows are present with owner phases. |

### Data-Flow Trace (Level 4)

| Artifact | Data Variable | Source | Produces Real Data | Status |
|----------|---------------|--------|--------------------|--------|
| Phase 2 planning docs | N/A | Documentation/governance artifacts only | N/A | SKIPPED - no dynamic data-rendering artifact. |

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
|----------|---------|--------|--------|
| Phase 2 artifact validation gates | V-02-01 through V-02-09 shell checks from `02-VALIDATION.md` | Required sections, schemas, provenance, placeholders, and protected-path diff passed. | PASS |
| Ledger seed-hit coverage | `rg -n "18\.3|29\.1|35\.0|0\.1216|%|vkm|Gini|percentage points|confidence|Table~|Figure~" manuscript/main.tex manuscript/sections` cross-checked against ledger | 168 hits, 0 missing. | PASS |
| Docs-only runtime behavior | No API, CLI, build, or mutable runtime entry point was produced by Phase 2. | Step 7b skipped as documentation-only. | SKIP |

### Probe Execution

| Probe | Command | Result | Status |
|-------|---------|--------|--------|
| N/A | Probe discovery in `scripts/**/probe-*.sh` and Phase 2 plan/summary references | No declared or conventional probes found for this documentation phase. | SKIP |

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|-------------|-------------|--------|----------|
| PLAN-04 | `02-03-PLAN.md` | `05_BLOCKERS_AND_SAFE_CLAIMS.md` identifies blockers, safe claims, downgraded claims, and prohibited wording. | SATISFIED | Blocker artifact has status enum, risk family rules, safe claim families, downgrade/blocker routing, 18 concrete rows, and Phase 5 checklist. |
| CLAI-01 | `02-01-PLAN.md` | `02_TR_E_POSITIONING_LOCK.md` states allowed framing, prohibited framing, core contribution, and journal-fit rationale. | SATISFIED | Positioning lock contains the required sections and exact safe mechanism/framing labels. |
| CLAI-02 | `02-02-PLAN.md` | `03_CLAIM_LEDGER.md` has mandatory provenance columns plus location/comparison/metric/reported value fields. | SATISFIED | Ledger header and 68 rows include the required schema and execution fields. |
| CLAI-03 | `02-02-PLAN.md` | Numerical claims in target manuscript sections appear in the claim ledger. | SATISFIED | Numeric/Table/Figure seed-hit coverage is 168/168 with 0 missing locations. |
| CLAI-04 | `02-01-PLAN.md`, `02-02-PLAN.md`, `02-03-PLAN.md` | Claims distinguish primary behavioral evidence, diagnostics, robustness/sensitivity, equity/type heterogeneity, algorithm diagnostics, and limitations. | SATISFIED | Role enums and row-level role usage are present in all three Phase 2 artifacts. |

No orphaned Phase 2 requirements were found: ROADMAP Phase 2 lists exactly PLAN-04 and CLAI-01 through CLAI-04, and all are covered by Phase 2 plans.

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| Phase 2 artifacts | N/A | `TODO`, `TBD`, `FIXME`, `XXX`, `HACK`, empty implementation, and hardcoded-empty scans | None | No debt-marker or stub patterns found. |
| Phase 2 artifacts | Multiple | `placeholder` / prohibited wording examples | Info | Intentional governance text: Phase 4 placeholder rules and prohibited-sentence examples, not incomplete implementation. |

### Human Verification Required

None. Phase 2 produced documentation and governance artifacts only; all required truths were checkable through file, schema, grep, commit-scope, and provenance checks.

### Gaps Summary

No blocking gaps found. Existing old numbers, Part A wording, policy-first wording, legacy result paths, and package-facing risks are intentionally captured as downstream blockers in `05_BLOCKERS_AND_SAFE_CLAIMS.md`; they are not Phase 2 failures because Phase 2 was required to identify and route them before prose edits.

---

_Verified: 2026-06-17T11:00:51Z_
_Verifier: the agent (gsd-verifier)_
