---
phase: 09-paper-section-updates
verified: 2026-04-12T06:00:00Z
status: passed
score: 5/5
overrides_applied: 0
re_verification:
  previous_status: gaps_found
  previous_score: 4/5
  gaps_closed:
    - "experiments.tex tab:milp-gap now contains actual numeric values (no [FILL] placeholders); results/milp_gap.json exists with 6 rows of real data"
  gaps_remaining: []
  regressions: []
---

# Phase 9: Paper Section Updates — Verification Report

**Phase Goal:** All MAJOR and MINOR paper-level reviewer concerns are resolved: MILP benchmark scope is unambiguous, objective weights have policy-grounded VOT interpretation, and parameter values are benchmarked against literature.
**Verified:** 2026-04-12T06:00:00Z
**Status:** passed
**Re-verification:** Yes — after gap closure

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | algorithm.tex states explicitly that MILP solves deterministic routing of the realized accepted set from ALNS (ex-post benchmark) | VERIFIED | Lines 47-64: "Ex-post benchmark role" paragraph; z_r treated as fixed constant; gap formula defined |
| 2 | experiments.tex contains MILP vs ALNS optimality gap table (tab:milp-gap) with actual numeric values | VERIFIED | Label at line 106; n=20 row: 54.1 / 21.7 / 169.6±46.8%; n=30 row: 65.6 / 33.3 / 98.8±40.3%; no [FILL] placeholders; backed by results/milp_gap.json (6 rows) |
| 3 | policy.tex contains VOT mapping table (tab:vot-mapping) with alpha weight monetization using Chinese urban VOT values | VERIFIED | Label at line 195; 3 passenger types with computed VOT values; literature benchmark row citing shao2017 and li2020drt |
| 4 | experiments.tex contains weight sensitivity table (tab:weight-sensitivity) showing FullModel reduces vkm/served-trip vs DoorToDoor across 3 weight configs | VERIFIED | Label at line 333; actual numeric values present (30.8%, 31.4%, 30.5% reductions); backed by results/weight_sensitivity.json |
| 5 | model.tex contains footnote benchmarking implied VOT from beta parameters against Shao et al. 2017 and Li et al. 2020 | VERIFIED | Lines 284-302: footnote cites shao2017 and li2020drt; VOT_wait=0.80, VOT_IVT=0.40 CNY/min; cross-references tab:vot-mapping |

**Score:** 5/5 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `paper/sections/algorithm.tex` | Ex-post benchmark framing, z_r fixed | VERIFIED | "Ex-post benchmark role" paragraph at lines 47-64 |
| `paper/sections/experiments.tex` | tab:milp-gap and tab:weight-sensitivity with real values | VERIFIED | Both tables present with actual numeric data; no [FILL] tokens anywhere in file |
| `paper/sections/policy.tex` | tab:vot-mapping with VOT values | VERIFIED | Table at lines 192-212; shao2017/li2020drt cited |
| `paper/sections/model.tex` | Footnote with Shao et al. / Li et al. | VERIFIED | Footnote at lines 284-302 |
| `results/milp_gap.json` | MILP gap data for n=20, n=30 (6 rows) | VERIFIED | 6 rows present; values consistent with table (n=20 mean gap 169.6%, n=30 mean gap 98.8%) |
| `results/weight_sensitivity.json` | Weight sensitivity data (9 rows) | VERIFIED | 9 rows, 3 configs x 3 seeds |

### Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| algorithm.tex MILP section | ALNS accepted set | "z_r as known constant" text | VERIFIED | Lines 53-55 explicitly state z_r is fixed input from ALNS run |
| policy.tex tab:vot-mapping | model.tex beta parameters | VOT = beta_i/beta_4 derivation | VERIFIED | Equation eq:vot-formula in policy.tex; values match beta params in model.tex |
| experiments.tex tab:milp-gap | results/milp_gap.json | hardcoded table values | VERIFIED | Numeric values in table are consistent with JSON data (means and stds match) |
| experiments.tex tab:weight-sensitivity | results/weight_sensitivity.json | hardcoded table values | VERIFIED | Numeric values in table match JSON data |

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|------------|-------------|--------|----------|
| REV-09 | 09-01-PLAN.md | algorithm.tex states MILP is ex-post benchmark over realized z_r | SATISFIED | Lines 47-64 of algorithm.tex |
| REV-10 | 09-01-PLAN.md | experiments.tex contains tab:milp-gap with n=20 and n=30 gap values | SATISFIED | Table at lines 103-115 with real numeric values; results/milp_gap.json present |
| REV-11 | 09-02-PLAN.md | policy.tex contains tab:vot-mapping with VOT monetization | SATISFIED | Table at lines 192-212 of policy.tex |
| REV-12 | 09-03-PLAN.md | experiments.tex contains tab:weight-sensitivity across 3 weight configs | SATISFIED | Table at lines 327-342 of experiments.tex with actual values |
| REV-13 | 09-02-PLAN.md | model.tex footnote benchmarks beta VOT against Shao 2017 / Li 2020 | SATISFIED | Footnote at lines 284-302 of model.tex |

### Anti-Patterns Found

No blockers or warnings. The [FILL] placeholders and TODO comment previously flagged in experiments.tex (lines 111-119) have been removed and replaced with real values.

### Gaps Summary

No gaps. All five requirements are fully satisfied. The previously-blocking REV-10 gap is closed: `results/milp_gap.json` now exists with 6 rows of real data, and `tab:milp-gap` in experiments.tex contains actual numeric values consistent with that data. No `[FILL]` placeholders remain anywhere in `paper/sections/*.tex`.

---

_Verified: 2026-04-12T06:00:00Z_
_Verifier: Claude (gsd-verifier)_
