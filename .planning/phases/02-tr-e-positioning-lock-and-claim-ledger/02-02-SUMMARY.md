---
phase: "02-tr-e-positioning-lock-and-claim-ledger"
plan: "02-02"
subsystem: "claim-ledger"
tags: ["claim-ledger", "tr-e", "evidence-provenance", "phase-4-handoff"]
requires: ["02-01"]
provides: ["occurrence-level claim ledger", "phase-4 provenance handoff"]
affects: [".planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md"]
tech_stack:
  added: []
  patterns: ["Markdown occurrence ledger", "Phase 6 formal evidence boundary"]
key_files:
  created:
    - ".planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md"
  modified:
    - ".planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md"
decisions:
  - "Ledger rows are occurrence-level and may share claim_family_id values for cross-section grouping."
  - "Formal numerical claims are Phase 4 placeholders until source, denominator, and wording are verified."
  - "Matched coverage and fixed accepted-set evidence are diagnostic, not primary headline evidence."
metrics:
  duration: "not_tracked_from_start"
  completed_at_utc: "2026-06-17T10:36:36Z"
  tasks_completed: 3
  files_changed: 1
---

# Phase 02 Plan 02: Claim Ledger Summary

Built an occurrence-level claim ledger for the current manuscript source, with formal Phase 6 provenance fields, denominator contracts, allowed replacement wording, and prohibited overclaim wording for Phase 3/4 handoff.

## Completed Tasks

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Create claim ledger schema | `2035796` | `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` |
| 2 | Populate manuscript claim rows | `54b70e7` | `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` |
| 3 | Lock provenance and denominator handoff | `4e85394` | `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` |

## What Changed

- Created `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` with the mandatory schema fields: `source_path`, `script_path`, `generation_command`, `metric_formula`, `numerator`, `denominator`, `evidence_role`, `allowed_sentence`, and `prohibited_sentence`.
- Added a manuscript coverage inventory for `manuscript/main.tex` and all current `manuscript/sections/*.tex` files.
- Logged 68 occurrence-level claim rows, `C-001` through `C-068`, spanning positioning, mechanism scope, routing intensity, coverage trade-offs, Gamma semantics, Beijing scenario wording, MILP diagnostics, robustness, equity/type heterogeneity, and limitations.
- Preserved Phase 2 scope: no manuscript, result, source, experiment, analysis, README, CLAUDE, or dependency files were changed.

## Verification

- Confirmed all nine manuscript target files are represented in the coverage inventory.
- Confirmed 168 numeric/table/figure/prohibited-wording seed hits are mapped to claim IDs or marked as reviewed non-claims.
- Confirmed required evidence roles and metric denominator formulas are present in the ledger.
- Confirmed all claim rows have stable Markdown table shape: 68 rows, correct pipe count.
- Confirmed protected paths were untouched with `git diff --name-only -- manuscript results src experiments analysis README.md CLAUDE.md pyproject.toml`.

## Deviations from Plan

None in implementation scope.

The plan's literal `rg ... manuscript/sections/*.tex` verification command was adapted to `rg ... manuscript/main.tex manuscript/sections` because PowerShell passed the glob literally and `rg` rejected it as an invalid Windows path. The adapted command scanned the same manuscript target set.

## Known Stubs

Intentional Phase 4 placeholders are defined in `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` for unverified numerical values, tables, figures, and confidence intervals. They are handoff controls, not incomplete implementation.

## Threat Flags

None. The plan created documentation-only planning artifacts and introduced no new network endpoint, auth path, file-access boundary, or schema trust boundary.

## Self-Check: PASSED

- Found `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md`.
- Found task commits `2035796`, `54b70e7`, and `4e85394`.
- Protected manuscript/result/source/dependency paths remained unchanged.
