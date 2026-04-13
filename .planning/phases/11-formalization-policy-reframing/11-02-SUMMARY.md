---
phase: 11-formalization-policy-reframing
plan: "02"
subsystem: paper/policy-reframing
tags: [policy, generalizability, reviewer-response, v3.0]
dependency_graph:
  requires: [11-01]
  provides: [PFRAM-01, PFRAM-02, PFRAM-03]
  affects: [paper/sections/policy.tex, paper/response_to_reviewers.tex]
tech_stack:
  added: []
  patterns: [pure-latex-insertion]
key_files:
  modified:
    - paper/sections/policy.tex
    - paper/response_to_reviewers.tex
decisions:
  - "Policy thresholds (1000m, 15-vehicle ratio) reframed as scenario-specific managerial insights, not universal prescriptions"
  - "v3.0 Revisions section documents all Phase 10+11 changes in one place for reviewer transparency"
metrics:
  duration: "~10 minutes"
  completed: "2026-04-13T02:13:53Z"
  tasks_completed: 3
  files_modified: 2
---

# Phase 11 Plan 02: Policy Reframing Caveats + Reviewer Response v3.0 Summary

Pure LaTeX insertions softening the 1000m walking threshold (R1) and 15-vehicle fleet ratio (R2) from universal prescriptions to scenario-specific findings, plus a v3.0 Revisions section in the reviewer response documenting all Phase 10-11 changes.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | PFRAM-01: R1 generalizability caveat | 80d8838 | paper/sections/policy.tex |
| 2 | PFRAM-02: R2 generalizability caveat | 80d8838 | paper/sections/policy.tex |
| 3 | PFRAM-03: v3.0 Revisions section | eda5a68 | paper/response_to_reviewers.tex |

## Changes Made

### policy.tex

Two `\paragraph{Generalizability caveat.}` blocks inserted:

- After R1 Policy implication: names synthetic 20x20km scenario, MNL calibration to Chinese suburban conditions, pedestrian infrastructure dependence, local survey recommendation, "scenario-specific managerial insight" framing.
- After R2 Policy implication: names uniform synthetic demand, "order-of-magnitude guideline" framing, demand clustering and temporal pattern dependence, sensitivity curve as calibration tool.

### response_to_reviewers.tex

`\section*{v3.0 Revisions (Second Round)}` inserted between the Summary of Changes closing sentence and the author affiliation block. Contains FIX-01 through FIX-05:

- FIX-01: vkm/trip denominator correction (15.1/21.3 corrected values)
- FIX-02: matched-coverage experiment (10.9/42.3, 74.3% improvement at equal coverage)
- FIX-03: timing/decision diagram (Table 5, Bernoulli sampling timing)
- FIX-04: ALNS online objective statement (surrogate objective formalization)
- FIX-05: policy thresholds reframed (R1 + R2 caveats summarized)

## Verification

```
policy.tex: PASSED (Generalizability caveat count=2)
order-of-magnitude guideline present: True
response_to_reviewers.tex: PASSED
v3.0 Revisions present: True
74.3 present: True
FIX-05 present: True
```

## Deviations from Plan

None — plan executed exactly as written.

## Self-Check: PASSED

- paper/sections/policy.tex: modified, committed at 80d8838
- paper/response_to_reviewers.tex: modified, committed at eda5a68
- Both commits verified in git log
