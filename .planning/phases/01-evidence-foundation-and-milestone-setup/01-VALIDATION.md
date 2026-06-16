---
phase: 01
slug: evidence-foundation-and-milestone-setup
status: draft
nyquist_compliant: true
wave_0_complete: true
created: 2026-06-16
---

# Phase 01 - Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | PowerShell file checks, `rg`, git diff boundary checks |
| **Config file** | None for planning-doc validation |
| **Quick run command** | `Test-Path .planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md` |
| **Full suite command** | `rg -n "results/formal/phase06|Phase 4|prohibited wording" .planning/milestones/tr_e_claim_ready/*.md` |
| **Estimated runtime** | <10 seconds |

## Sampling Rate

- **After every task commit:** Run the task-specific `Test-Path` and `rg`
  assertions from the PLAN task.
- **After every plan wave:** Run the full suite command above plus the boundary
  check below.
- **Before `$gsd-verify-work`:** All three milestone files must exist and the
  boundary check must report no changed manuscript/source/result files.
- **Max feedback latency:** 10 seconds.

Boundary check:

`git diff --name-only -- manuscript results src experiments analysis README.md pyproject.toml`

Expected output during Phase 1 execution: no lines.

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 01-01-01 | 01-01 | 1 | PLAN-01 | T-01-01 | No secrets or local license paths copied into milestone plan | source | `Test-Path .planning/milestones/tr_e_claim_ready` | yes | pending |
| 01-01-02 | 01-01 | 1 | PLAN-02 | T-01-01 | Verification gates document commands but not private environment data | source | `rg -n "Do not before gate|Phase 4|TR-E submission-ready" .planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md` | yes | pending |
| 01-02-01 | 01-02 | 2 | PLAN-03 | T-01-02 | Audit records evidence paths without copying raw result rows or credentials | source | `rg -n "results/formal/phase06|formal_smoke_excluded|Allowed use|Prohibited use" .planning/milestones/tr_e_claim_ready/01_REPO_AND_EVIDENCE_AUDIT.md` | yes | pending |
| 01-03-01 | 01-03 | 3 | VERI-01 | T-01-03 | Action plan defers numeric injection and records scan families | source | `rg -n "defer until Phase 4|manuscript/sections|prohibited wording" .planning/milestones/tr_e_claim_ready/04_MANUSCRIPT_ACTION_PLAN.md` | yes | pending |

## Wave 0 Requirements

Existing infrastructure covers all Phase 1 requirements. No test framework
installation is needed because Phase 1 verifies planning Markdown artifacts and
repository boundaries.

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Evidence-role judgment | PLAN-03 | Requires research judgment over formal vs diagnostic vs excluded artifacts | Review `01_REPO_AND_EVIDENCE_AUDIT.md` and confirm every listed evidence role has allowed/prohibited use text. |
| Manuscript sequencing judgment | VERI-01 | Requires editorial judgment over phase ordering and numerical-injection gates | Review `04_MANUSCRIPT_ACTION_PLAN.md` and confirm all final percentages, confidence intervals, significance wording, and table/figure numbers are deferred to Phase 4. |

## Validation Sign-Off

- [x] All tasks have automated verify or manual review instructions.
- [x] Sampling continuity: no 3 consecutive tasks without automated verify.
- [x] Wave 0 covers all missing references.
- [x] No watch-mode flags.
- [x] Feedback latency <10s.
- [x] `nyquist_compliant: true` set in frontmatter.

**Approval:** pending

