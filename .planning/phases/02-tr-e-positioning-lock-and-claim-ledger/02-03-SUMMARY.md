---
phase: "02-tr-e-positioning-lock-and-claim-ledger"
plan: "02-03"
subsystem: "blockers-and-safe-claims"
tags: ["tr-e", "claim-boundaries", "blocker-routing", "package-consistency"]
requires: ["02-01", "02-02"]
provides: ["claim status rules", "scan-backed blocker table", "phase 5 verification checklist"]
affects: [".planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md"]
tech_stack:
  added: []
  patterns: ["Markdown blocker routing table", "scan-backed claim governance"]
key_files:
  created:
    - ".planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md"
    - ".planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-03-SUMMARY.md"
  modified:
    - ".planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md"
decisions:
  - "Claim statuses are limited to safe, safe_with_qualifier, downgrade_required, and blocker."
  - "Old values 18.3%, 29.1%, 35.0%, and 0.1216 are blockers until Phase 4 verifies provenance."
  - "Package-facing risks remain package_consistency or provenance-risk rows unless reused in submitted manuscript text."
metrics:
  duration: "9.8 minutes"
  completed_at_utc: "2026-06-17T10:51:54Z"
  tasks_completed: 2
  files_changed: 2
---

# Phase 02 Plan 03: Blockers And Safe Claims Summary

Built the Phase 2 blocker and safe-claim routing artifact that locks claim statuses, risk families, package-facing risk handling, concrete scan hits, and Phase 5 verification checks.

## Completed Tasks

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Define claim status and risk routing rules | `894ce21` | `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` |
| 2 | Populate concrete scan-backed blocker rows | `78ae18b` | `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` |

## What Changed

- Created `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md`.
- Defined the only allowed claim statuses: `safe`, `safe_with_qualifier`, `downgrade_required`, and `blocker`.
- Added risk-family rules for old numbers, TR-A/Part A targeting, policy-first framing, dominance/outperformance wording, Gamma/Pareto semantics, Beijing validation wording, MILP exactness, legacy result paths, premature readiness, diagnostic promotion, and package consistency.
- Added safe claim families and downgrade/blocker routing for Phase 3 rewriting, Phase 4 provenance validation, Phase 5 package checks, and future/v2 evidence gaps.
- Populated 18 scan-backed or scan-result rows, `B-001` through `B-018`, with owner phase, required action, allowed replacement, and verification check fields.
- Preserved Phase 2 scope: no manuscript, result, source, experiment, analysis, README, CLAUDE, or dependency files were changed.

## Verification

- Confirmed `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` exists.
- Confirmed all required blocker columns are present: `issue_id`, `location`, `matched_text_or_pattern`, `risk_family`, `status`, `evidence_role`, `owner_phase`, `required_action`, `allowed_replacement`, and `verification_check`.
- Confirmed required replacement patterns and routing terms appear, including `Beijing-inspired synthetic grid`, `post-hoc welfare or sensitivity accounting`, `simplified ex-post diagnostic over fixed accepted sets`, `conditional lower routing intensity`, `package_consistency`, and Phase 3/4/5 owner labels.
- Confirmed placeholder rows were removed by scanning for `B-TBD` and `pending Task 2`.
- Confirmed protected paths were untouched with `git diff --name-only -- manuscript results src experiments analysis README.md CLAUDE.md pyproject.toml`.

## Deviations from Plan

None. The plan was executed within the intended planning-artifact scope.

## Known Stubs

Intentional Phase 4 placeholders such as `[PHASE4_VERIFIED_VALUE]`, `[PHASE4_VERIFIED_CI]`, and `[PHASE4_VERIFIED_TABLE]` appear in allowed replacement rules. They are blocker controls for unverified numerical claims, not incomplete implementation.

## Threat Flags

None. The plan created documentation-only planning artifacts and introduced no new network endpoint, auth path, file-access boundary, or schema trust boundary.

## Self-Check: PASSED

- Found `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md`.
- Found task commits `894ce21` and `78ae18b`.
- Protected manuscript/result/source/dependency paths remained unchanged.
