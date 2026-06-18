# Phase 5: Verification and Readiness Closeout - Context

**Gathered:** 2026-06-18T19:37:52.5465811+08:00
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 5 verifies the TR-E manuscript package and records the final readiness
classification with exact evidence. It owns formal statistics validation,
targeted pytest verification, manuscript compilation, prohibited wording checks
for the core submission package, and the final
`.planning/milestones/tr_e_claim_ready/99_MILESTONE_VERIFICATION.md` report.

This phase may run validation/test/compile commands, inspect logs, classify
failures by manuscript impact, and write the final verification report and
core submit-ready materials checklist. It may make only manuscript-critical
fixes when a verification failure blocks readiness and the fix stays within
the existing evidence and claim boundaries.

This phase must not broaden claims, rerun full formal experiments by default,
manually edit result numbers, promote diagnostic evidence, or use
`TR-E submission-ready` unless every hard readiness gate passes.

</domain>

<decisions>
## Implementation Decisions

### Hard Readiness Gates

- **D-01:** Phase 5 uses strict hard gates. `TR-E submission-ready` is allowed
  only when all readiness gates pass.
- **D-02:** If a hard gate fails, `near-ready` is allowed only for external or
  tooling blockers. Claim, evidence, ledger, prohibited wording, or manuscript
  content failures classify the package as not ready until fixed.
- **D-03:** Core submission package readiness is the hard gate. `README.md` and
  `CLAUDE.md` are not blockers unless the user later includes them in the
  submission package.

### Targeted Test Scope

- **D-04:** The pytest readiness gate is the active-suite command:
  `$env:PYTHONPATH='src'; pytest tests/ analysis/test_sensitivity.py`.
- **D-05:** Bare `pytest` from the repository root is not a Phase 5 hard gate.
  The archived ad hoc test collection issue is a future hardening item, not a
  submission-readiness blocker.
- **D-06:** Gurobi or MILP skips are acceptable when they appear as pytest
  skips and are recorded in the final report, provided the manuscript keeps
  MILP framed as a simplified diagnostic.

### LaTeX Compilation Failure Handling

- **D-07:** The LaTeX readiness gate is the full sequence from
  `manuscript/`: `pdflatex main`, `bibtex main`, `pdflatex main`,
  `pdflatex main`.
- **D-08:** External LaTeX toolchain failures, such as missing TeX, BibTeX, or
  `elsarticle.cls`, can support only `near-ready external blocker`, never
  `TR-E submission-ready`. The report must record the exact missing tool or
  package, failed command, and manuscript impact.
- **D-09:** Undefined references and citation warnings are hard blockers.
  Overfull or underfull box warnings are recorded and block readiness only if
  they affect readability or submission suitability.

### Submission Package Consistency

- **D-10:** The prohibited wording scan covers the core submission package:
  `manuscript/main.tex`, `manuscript/sections/*.tex`, main table/figure
  captions and source notes, the claim ledger, and the final verification
  report.
- **D-11:** `manuscript/cover_letter.tex` and
  `manuscript/response_to_reviewers.tex` are not Phase 5 readiness hard gates
  unless the user later explicitly includes them in the submission package.
- **D-12:** `99_MILESTONE_VERIFICATION.md` must include a core submit-ready
  materials checklist covering manuscript source, PDF, formal evidence/table/
  figure provenance, claim ledger, and validation/test/compile commands.

### Agent Discretion

- Downstream agents may choose the exact wording and layout of
  `99_MILESTONE_VERIFICATION.md`, the exact prohibited-wording scan commands,
  and the log excerpt format, as long as the decisions above are preserved.
- Downstream agents may decide whether a failed gate should trigger a narrow
  manuscript-critical fix or be documented as a blocker, but they must not
  downgrade claim/evidence/provenance failures to `near-ready`.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Planning Source Of Truth

- `.planning/PROJECT.md` - Project goal, evidence boundary, TR-E target,
  readiness standard, and claim posture constraints.
- `.planning/REQUIREMENTS.md` - Phase 5 requirements VERI-02 through VERI-06.
- `.planning/ROADMAP.md` - Phase 5 goal, success criteria, and plan list.
- `.planning/STATE.md` - Current workflow state and accumulated decisions.
- `.planning/phases/02-tr-e-positioning-lock-and-claim-ledger/02-CONTEXT.md`
  - Claim ledger, evidence-role, blocker, and safe wording decisions.
- `.planning/phases/03-tr-e-manuscript-repositioning/03-CONTEXT.md` -
  Manuscript framing, prohibited wording, and diagnostic boundary decisions.
- `.planning/phases/04-tables-figures-and-numerical-provenance/04-CONTEXT.md`
  - Table/figure provenance, final-number placement, and formal evidence
  decisions.

### Milestone Controls

- `.planning/milestones/tr_e_claim_ready/00_MILESTONE_PLAN.md` - Milestone
  gates, evidence boundary, execution order, and readiness rules.
- `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md` - Claim ledger
  and mandatory provenance schema; must remain fully covered for readiness.
- `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md` -
  Prohibited wording, old-value blockers, and package consistency risks.

### Codebase Maps

- `.planning/codebase/TESTING.md` - Active-suite pytest command, archive
  collection risk, and test organization.
- `.planning/codebase/STRUCTURE.md` - Canonical manuscript, results, tests,
  and planning artifact locations.
- `.planning/codebase/CONCERNS.md` - Known risks around bare pytest,
  dependencies, Gurobi, Gamma, Beijing wording, and MILP scope.

### Active Verification Targets

- `experiments/formal_statistics.py` - Formal statistics, table, plot,
  manifest, verification, and synthesis generator.
- `experiments/formal_validation.py` - Formal denominator and validation
  helpers.
- `experiments/phase06_formal.py` - Formal main behavioral package validation
  and manifest entry point.
- `experiments/phase06_coverage_controls.py` - Matched-coverage and
  fixed-accepted-set diagnostic controls.
- `experiments/phase06_robustness.py` - Robustness, equity/type, Gamma, and
  algorithm diagnostic packages.
- `tests/` - Active pytest suite for core algorithms, runner behavior, phase
  harnesses, controls, and robustness packages.
- `analysis/test_sensitivity.py` - Active analysis test included in the Phase 5
  pytest gate.

### Core Submission Package

- `manuscript/main.tex` - Master manuscript source and compile target.
- `manuscript/sections/*.tex` - Core manuscript sections covered by the
  prohibited wording scan.
- `manuscript/references.bib` - Bibliography source used by the BibTeX
  readiness gate.
- `manuscript/figures/` - Main figure assets referenced by the manuscript.
- `results/formal/phase06/` - Canonical formal evidence boundary for tables,
  figures, and formal claims.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets

- `experiments/formal_statistics.py`: Reusable formal closeout entry point for
  formal tables, plots, manifests, verification reports, and synthesis
  validation.
- `experiments/formal_validation.py`, `experiments/phase06_formal.py`,
  `experiments/phase06_coverage_controls.py`, and
  `experiments/phase06_robustness.py`: Existing validators and package-specific
  checks that should inform formal validation status.
- `tests/` plus `analysis/test_sensitivity.py`: Active maintained test suite
  for Phase 5 readiness, intentionally scoped away from archived ad hoc tests.
- `manuscript/main.tex`, `manuscript/sections/*.tex`, and
  `manuscript/references.bib`: LaTeX compile and prohibited-wording targets.

### Established Patterns

- Formal claims must trace to `results/formal/phase06/`; root legacy results,
  smoke outputs, pilot outputs, archive outputs, and ad hoc outputs remain
  non-canonical by default.
- Generated evidence and manuscript figures live under `results/` and
  `manuscript/figures/`; Phase 5 should verify provenance rather than
  regenerate or reinterpret numbers unless a narrow verification fix requires
  it.
- Default bare pytest can collect `archive/adhoc_tests/`; the maintained active
  command scopes pytest to `tests/` and `analysis/test_sensitivity.py` with
  `PYTHONPATH=src`.
- Gurobi availability is machine-specific. Skips can be acceptable only when
  recorded and aligned with the manuscript's diagnostic MILP scope.

### Integration Points

- `.planning/milestones/tr_e_claim_ready/99_MILESTONE_VERIFICATION.md`: Final
  Phase 5 report to create with commands, outputs, blockers, readiness
  classification, and core materials checklist.
- `.planning/milestones/tr_e_claim_ready/03_CLAIM_LEDGER.md`: Must support
  100% numerical-claim coverage before `TR-E submission-ready`.
- `.planning/milestones/tr_e_claim_ready/05_BLOCKERS_AND_SAFE_CLAIMS.md`:
  Source for prohibited wording and readiness-blocking risk families.
- `manuscript/`: Compile target and core submission package scan target.

</code_context>

<specifics>
## Specific Ideas

- Keep the final readiness vocabulary conservative: `TR-E submission-ready`
  only when every hard gate passes; `near-ready external blocker` only for
  external tooling blockers.
- Include a submit-ready materials checklist in the final report so the
  manuscript package can be handed off without pulling non-submission files
  into the hard gate.
- Preserve the known bare-pytest/archive issue as future reproducibility
  hardening, not a Phase 5 submission blocker.

</specifics>

<deferred>
## Deferred Ideas

None - discussion stayed within Phase 5 scope.

</deferred>

---

*Phase: 5-Verification and Readiness Closeout*
*Context gathered: 2026-06-18T19:37:52.5465811+08:00*
