---
phase: 01
slug: evidence-foundation-and-milestone-setup
status: complete
created: 2026-06-16
pattern_mode: inline-codex
---

# Phase 1 Pattern Map

## Planned Files

| Planned file | Role | Closest existing analogs |
|--------------|------|--------------------------|
| `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md` | Hard-gate milestone execution plan | `.planning/ROADMAP.md`, `.planning/PROJECT.md`, `.planning/STATE.md` |
| `.planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md` | Canonical-first evidence and risk audit | `.planning/codebase/CONCERNS.md`, `results/formal/phase06/phase06_result_manifest.json`, `results/formal/phase06/phase06_verification_report.json` |
| `.planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md` | Manuscript section and evidence-role action plan | `.planning/phases/01-evidence-foundation-and-milestone-setup/01-CONTEXT.md`, `.planning/REQUIREMENTS.md`, `manuscript/sections/*.tex` |

## Existing Patterns To Reuse

### Canonical path inventory

Use complete relative paths, matching the context file and codebase maps. Avoid
informal references like "the formal results" when a downstream claim ledger
needs a reusable `source_path`.

### Status and gate language

Use hard-gate wording from `.planning/ROADMAP.md` and `.planning/REQUIREMENTS.md`:
requirements, success criteria, phase order, and readiness gates should be
observable and auditable.

### Risk taxonomy

Use `.planning/codebase/CONCERNS.md` as the nearest analog for risk entries:
each risk should have a description, affected paths, impact, and safe handling.
For Phase 1, classify by manuscript impact:

- claim-critical blocker
- verification risk
- reproducibility hardening
- manuscript/package consistency risk
- claim-impact conditional risk
- future model/evidence

### Evidence-role separation

Use `results/formal/phase06/phase06_result_manifest.json` as the authoritative
package inventory. Preserve its evidence roles and validation status, then add
allowed/prohibited manuscript-use language in the audit.

### Command-level placeholders

Use concrete commands where the repository exposes them, but label later-phase
commands as gates rather than running them in Phase 1. Good examples:

- `$env:PYTHONPATH='src'; python -m experiments.formal_statistics --validate --results-dir results/formal/phase06`
- `$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --results-dir results/formal/phase06/main_behavioral`
- `$env:PYTHONPATH='src'; python -m experiments.phase06_coverage_controls --validate --package all`
- `$env:PYTHONPATH='src'; python -m experiments.phase06_robustness --validate --package all`
- `$env:PYTHONPATH='src'; pytest tests`
- `pdflatex main`, `bibtex main`, `pdflatex main`, `pdflatex main`

## Data Flow For Phase 1 Artifacts

`.planning/PROJECT.md`, `.planning/REQUIREMENTS.md`, `.planning/ROADMAP.md`,
`.planning/STATE.md`, `.planning/codebase/CONCERNS.md`, and formal Phase 6
validation reports feed the milestone plan and audit.

The audit feeds the manuscript action plan. The manuscript action plan feeds
Phase 2 claim-ledger work, Phase 3 non-numeric manuscript repositioning, Phase 4
table/figure provenance, and Phase 5 readiness closeout.

## Landmines

- Do not promote `results/formal/phase06/smoke/` into formal evidence.
- Do not copy root legacy values into the audit as current claims.
- Do not create safe-claims or claim-ledger tables in Phase 1; Phase 2 owns
  those artifacts.
- Do not edit manuscript prose in Phase 1.
- Do not run full formal experiments by default.
- Do not say `TR-E submission-ready` in Phase 1 deliverables except as a
  future readiness label that is blocked until Phase 5 gates pass.

