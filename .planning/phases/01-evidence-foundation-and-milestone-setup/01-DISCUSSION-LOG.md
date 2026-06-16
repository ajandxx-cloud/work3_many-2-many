# Phase 1: Evidence Foundation and Milestone Setup - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md; this log preserves the alternatives considered.

**Date:** 2026-06-16T22:33:13+08:00
**Phase:** 1-Evidence Foundation and Milestone Setup
**Areas discussed:** Audit Strictness, Milestone Plan Contract, Manuscript Action Plan Granularity, Risk And Blocker Posture

---

## Audit Strictness

| Question | Options Considered | Selected |
|----------|--------------------|----------|
| How deep should `01_REPO_AND_EVIDENCE_AUDIT.md` inventory evidence and manuscript artifacts? | Canonical-first + risk appendix; full inventory of all related paths; core boundaries and known risks only | Canonical-first + risk appendix |
| How should `results/formal/phase06/` be classified? | By evidence role; by directory structure; by manuscript use case | By evidence role |
| How should non-canonical evidence be handled? | Default prohibition for formal claims; pending evidence pool; archive only | Default prohibition for formal claims |
| Should Phase 1 name known old values and wording risks? | High-priority tracking items; general risk only; locate and judge each old value in Phase 1 | High-priority tracking items |
| Should the audit include an allowed/prohibited use table? | Yes by evidence role; prose only; leave to Phase 2 claim ledger | Yes by evidence role |
| Should evidence paths be complete relative paths? | Complete relative paths required; complete for core paths only; directory-level paths only | Complete relative paths required |
| How should current Phase 6 validation status be treated? | Record existing status and paths, no default rerun; rerun formal validation; only record package existence | Record existing status and paths, no default rerun |
| Should audit include out-of-scope items? | Include deferred v2/out-of-scope section; only reference REQUIREMENTS.md; do not include | Include deferred v2/out-of-scope section |

**Notes:** User chose the recommended strict-but-bounded audit posture throughout. Phase 1 should support downstream claim control without becoming a full provenance rebuild or manuscript-edit phase.

---

## Milestone Plan Contract

| Question | Options Considered | Selected |
|----------|--------------------|----------|
| How binding should `00_MILESTONE_PLAN.md` be for later phases? | Hard gate plan; execution order plus responsibilities; lightweight roadmap summary | Hard gate plan |
| Should gates include failure routing? | Each key gate includes failure routing; gate only; leave to Phase 5 | Each key gate includes failure routing |
| Should the milestone plan forbid specific actions before gates pass? | Do not before gate rules; positive sequence only; individual phase plans only | Do not before gate rules |
| How detailed should verification gates be? | Command-level placeholders plus success criteria; verification categories only; exact final commands in Phase 1 | Command-level placeholders plus success criteria |

**Notes:** Milestone planning should prevent premature manuscript edits, premature numerical injection, and premature readiness claims.

---

## Manuscript Action Plan Granularity

| Question | Options Considered | Selected |
|----------|--------------------|----------|
| How should `04_MANUSCRIPT_ACTION_PLAN.md` be organized? | Manuscript section + evidence role; evidence role first; phase/task sequence | Manuscript section + evidence role |
| Should the action plan list manuscript file paths and region-level tasks? | File paths and region-level tasks; section names only; sentence/paragraph replacements | File paths and region-level tasks |
| How should numbers and table/figure references be handled? | Explicit defer-until-Phase-4 placeholders; general reminder; list old numbers and temporary wording in Phase 1 | Explicit defer-until-Phase-4 placeholders |
| How specifically should old Part A and policy wording be handled? | List wording families; general TR-E reframe only; search and list every hit in Phase 1 | List wording families |

**Notes:** The action plan should be concrete enough for Phase 3 execution but must not draft final manuscript prose or inject evidence-dependent numbers during Phase 1.

---

## Risk And Blocker Posture

| Question | Options Considered | Selected |
|----------|--------------------|----------|
| How should known repository risks be classified? | By manuscript impact; all high-priority concerns are blockers; all concerns wait until Phase 5 | By manuscript impact |
| Which risks may trigger code fixes during this milestone? | Only claim-critical or verification-blocking; all high-priority concerns; no code fixes | Only claim-critical or verification-blocking |
| How should bare pytest failure be classified? | Verification risk + reproducibility hardening; claim-critical blocker; fully deferred to v2 | Verification risk + reproducibility hardening |
| How should undeclared `pandas`/`matplotlib` dependencies be classified? | Verification/reproducibility risk; Phase 1 blocker; future hardening only | Verification/reproducibility risk |
| How should Gamma, Beijing, and MILP semantic risks be classified? | Claim-critical wording risks; future model/evidence only; technical blockers | Claim-critical wording risks |
| How should route-stop bookkeeping and completed-trip metric precision risk be handled? | Claim-impact conditional risk; immediate claim-critical blocker; future model hardening | Claim-impact conditional risk |
| How should README old known issues and Part A framing be classified? | Manuscript/package consistency risk; Phase 1 blocker; cosmetic issue | Manuscript/package consistency risk |
| Should Phase 1 reserve the Phase 2 blockers/safe-claims interface? | Reserve Phase 2 interface; let Phase 2 decide; create initial safe-claims table in Phase 1 | Reserve Phase 2 interface |

**Notes:** The risk posture keeps the milestone focused on claim readiness rather than broad engineering cleanup, while still preserving escalation paths for issues that affect claims or verification.

---

## Agent Discretion

None. The user selected specific options for all discussed gray areas.

## Deferred Ideas

- Real Beijing public-data ingestion and empirical validation.
- Endogenous Gamma behavior.
- Full dynamic exact benchmark.
- Broad import cleanup, root pytest hardening, dependency metadata cleanup, route-stop refactoring, and dependency locking unless claim-critical or verification-blocking.
