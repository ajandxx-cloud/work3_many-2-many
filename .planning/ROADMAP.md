# Roadmap: Work 3 TR-E Claim-Ready Manuscript Package

## Overview

This roadmap converts the current Work 3 experimental repository into a TR Part E-ready manuscript package. The work proceeds from evidence and source audit, to TR-E positioning and claim locking, to manuscript revision, table/figure provenance, and final verification. The roadmap is deliberately claim-led: manuscript prose changes come after evidence boundaries and safe wording are documented.

## Phases

**Phase Numbering:**

- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions, if needed

- [x] **Phase 1: Evidence Foundation and Milestone Setup** - Create the milestone scaffold, repo/evidence audit, and manuscript action plan. *(Completed 2026-06-16)*
- [x] **Phase 2: TR-E Positioning Lock and Claim Ledger** - Lock the allowed framing and map claims to evidence before manuscript edits. (completed 2026-06-17)
- [ ] **Phase 3: TR-E Manuscript Repositioning** - Rewrite the manuscript structure and TR-E framing while deferring final numerical injection.
- [ ] **Phase 4: Tables, Figures, and Numerical Provenance** - Refresh formal-evidence tables/figures, reconcile all reported numbers, and inject verified final numerical claims.
- [ ] **Phase 5: Verification and Readiness Closeout** - Run targeted verification, compile the manuscript, and classify readiness.

## Phase Details

### Phase 1: Evidence Foundation and Milestone Setup

**Goal**: Establish the milestone workspace and audit the canonical manuscript/evidence boundary before any claim edits.
**Depends on**: Nothing (first phase)
**Requirements**: [PLAN-01, PLAN-02, PLAN-03, VERI-01]
**Success Criteria** (what must be TRUE):

  1. `.planning/milestones/tr_e_claim_ready/` exists with the required planning files.
  2. `00_MILESTONE_PLAN.md` defines execution order, evidence boundaries, and verification gates.
  3. `01_REPO_AND_EVIDENCE_AUDIT.md` identifies canonical sources, formal Phase 6 evidence, non-canonical archives, and repo risks.
  4. `04_MANUSCRIPT_ACTION_PLAN.md` sequences the manuscript and verification work.

**Plans**: 3 plans

Plans:
**Wave 1**

- [x] 01-01: Create milestone folder and initial milestone plan.

**Wave 2** *(blocked on Wave 1 completion)*

- [x] 01-02: Audit canonical manuscript, formal Phase 6 evidence, and non-canonical outputs.

**Wave 3** *(blocked on Wave 2 completion)*

- [x] 01-03: Draft manuscript action plan and phase handoff notes.

**Cross-cutting constraints:**

- D-17: Known risks are classified by manuscript impact.
- D-06: Evidence references use complete relative paths.

### Phase 2: TR-E Positioning Lock and Claim Ledger

**Goal**: Define the safe TR-E framing and complete the claim ledger before editing prose.
**Depends on**: Phase 1
**Requirements**: [PLAN-04, CLAI-01, CLAI-02, CLAI-03, CLAI-04]
**Success Criteria** (what must be TRUE):

  1. `02_TR_E_POSITIONING_LOCK.md` states the allowed TR-E framing and prohibited framing.
  2. `03_CLAIM_LEDGER.md` maps every current and planned manuscript claim to source path, script path, generation command, metric formula, numerator, denominator, evidence role, allowed sentence, and prohibited sentence.
  3. `05_BLOCKERS_AND_SAFE_CLAIMS.md` distinguishes safe claims, downgraded claims, blockers, and prohibited wording.
  4. Primary evidence, diagnostics, robustness, equity, algorithm diagnostics, and limitations are separated.

**Plans**: 3 plans

Plans:

**Wave 1**

- [x] 02-01-PLAN.md - Write TR-E positioning lock and journal-fit rationale.

**Wave 2** *(blocked on Wave 1 completion)*

- [x] 02-02-PLAN.md - Build claim ledger from manuscript claims and Phase 6 formal evidence with hard provenance and denominator columns.

**Wave 3** *(blocked on Wave 2 completion)*

- [x] 02-03-PLAN.md - Create blockers and safe-claims table with prohibited wording.

### Phase 3: TR-E Manuscript Repositioning

**Goal**: Rewrite the manuscript as a logistics/operations contribution while applying the claim ledger, but do not finalize evidence-dependent numerical claims.
**Depends on**: Phase 2
**Requirements**: [POSE-01, POSE-02, POSE-03, POSE-04, CLAI-05, CLAI-06, CLAI-07, CLAI-08, MANU-01, MANU-02, MANU-03, MANU-04, MANU-05, MANU-06, MANU-07, MANU-08]
**Success Criteria** (what must be TRUE):

  1. Main manuscript metadata and touched project docs consistently target Transportation Research Part E.
  2. Abstract, introduction, contributions, literature review, and conclusion use TR-E logistics/operations framing with placeholders or non-numeric wording where final values depend on Phase 4 provenance checks.
  3. Experiments separate primary evidence from diagnostics, robustness, equity, and algorithm checks.
  4. Gamma, Beijing, MILP, and FullModel/DoorToDoor claims obey the safe wording from the ledger.
  5. The policy section is reframed as managerial and operational implications.
  6. No final percentages, uplift values, confidence intervals, significance wording, or table/figure numbers are newly locked into abstract, introduction, or conclusion before Phase 4.

**Plans**: 4 plans

Plans:

**Wave 1**

- [x] 03-01: Revise metadata, title, abstract, introduction, and contributions without final numerical injection.

**Wave 2** *(blocked on Wave 1 completion)*

- [ ] 03-02: Revise literature review, model, and algorithm sections for TR-E positioning and scope clarity.

**Wave 3** *(blocked on Wave 2 completion)*

- [ ] 03-03: Revise experiments narrative to separate evidence roles and denominators.

**Wave 4** *(blocked on Wave 3 completion)*

- [ ] 03-04: Revise managerial implications and conclusion with conditional non-overclaiming structure while deferring final numerical values.

### Phase 4: Tables, Figures, and Numerical Provenance

**Goal**: Ensure all manuscript numbers, tables, and figures are generated from validated formal Phase 6 evidence, then inject verified final values into the manuscript.
**Depends on**: Phase 3
**Requirements**: [TFIG-01, TFIG-02, TFIG-03, TFIG-04, TFIG-05, TFIG-06]
**Success Criteria** (what must be TRUE):

  1. Manuscript-ready tables and figures consume formal Phase 6 processed outputs only.
  2. Old 3-seed, smoke, archived, or root legacy numbers are replaced, removed, or explicitly labeled as superseded.
  3. Values such as 18.3%, 29.1%, 35.0%, and 0.1216 are retained only with current formal provenance or updated.
  4. Denominators and weight sensitivity formulas are verified and documented.
  5. Abstract, introduction, experiments, managerial/operational implications, and conclusion receive only verified final numbers after provenance is confirmed.

**Plans**: 3 plans

Plans:

- [ ] 04-01: Refresh tables and figures from validated formal Phase 6 outputs.
- [ ] 04-02: Reconcile all reported numerical claims against the claim ledger and inject verified final values into manuscript sections.
- [ ] 04-03: Verify denominators, weight sensitivity, Gamma invariance, and source provenance.

### Phase 5: Verification and Readiness Closeout

**Goal**: Verify the manuscript package and record readiness status with exact evidence.
**Depends on**: Phase 4
**Requirements**: [VERI-02, VERI-03, VERI-04, VERI-05, VERI-06]
**Success Criteria** (what must be TRUE):

  1. Formal statistics validation is run or its unavailability is documented.
  2. Targeted pytest checks pass, or failures are documented with manuscript impact.
  3. Manuscript compilation is run from `manuscript/` or failures are documented.
  4. `99_MILESTONE_VERIFICATION.md` records commands, outputs, pass/fail status, blockers, and readiness classification.
  5. `TR-E submission-ready` is used only if all hard readiness gates pass: manuscript compilation, validation/test status or no-impact explanations, 100% numerical claim-ledger coverage, formal Phase 6 table/figure provenance, and no prohibited wording.

**Plans**: 3 plans

Plans:

- [ ] 05-01: Run formal statistics validation and targeted pytest checks.
- [ ] 05-02: Compile manuscript with pdflatex/bibtex/pdflatex/pdflatex.
- [ ] 05-03: Write final verification report and readiness classification.

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4 -> 5

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Evidence Foundation and Milestone Setup | 3/3 | Complete | 2026-06-16 |
| 2. TR-E Positioning Lock and Claim Ledger | 3/3 | Complete   | 2026-06-17 |
| 3. TR-E Manuscript Repositioning | 1/4 | In Progress|  |
| 4. Tables, Figures, and Numerical Provenance | 0/3 | Not started | - |
| 5. Verification and Readiness Closeout | 0/3 | Not started | - |
