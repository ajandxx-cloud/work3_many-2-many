# Phase 10: Reproducibility Package and Final Verification - Context

**Gathered:** 2026-06-16T11:30:41+08:00
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 10 prepares the project for paper writing, coauthor checking, and peer
review by creating a reproducibility package and final verification framework.
It must organize commands, dependencies, configs, seeds, result manifests,
claim links, table/figure provenance, manuscript build steps, and a final
artifact index.

In scope:
- Create `10_REPRODUCIBILITY.md`, `10_RESULT_MANIFEST.md`, and
  `10_FINAL_VERIFICATION.md`.
- Record reviewer-facing reproduction entry points for final main tables,
  final main figures, Phase 6 formal artifacts, Phase 8 claim-gate artifacts,
  and manuscript build outputs.
- Inventory pilot, legacy, diagnostic, robustness, supplementary, and manuscript
  artifacts with explicit evidence roles.
- Fail closed when required upstream evidence is missing, while still producing
  blocked/pending Phase 10 artifacts that tell the next agent exactly what is
  missing.
- Provide a human-readable final artifact index and a manifest table structure
  that can later be converted to JSON or CSV.

Out of scope:
- Running or repairing Phase 6 formal experiments.
- Creating Phase 8 claim-gate judgments.
- Approving final manuscript claims without Phase 8 evidence.
- Treating pilot, legacy, or diagnostic artifacts as headline evidence.
- Rewriting manuscript prose beyond documenting reproducibility and verification
  requirements.

</domain>

<decisions>
## Implementation Decisions

### Upstream Prerequisite Gap Policy
- **D-01:** Phase 10 must fail closed if Phase 6 formal results/artifacts or
  the Phase 8 claim-gate files are missing. It must not claim final
  verification passed in that state.
- **D-02:** Even when fail-closed blockers exist, Phase 10 should still create
  `10_REPRODUCIBILITY.md`, `10_RESULT_MANIFEST.md`, and
  `10_FINAL_VERIFICATION.md` as blocked/pending artifacts.
- **D-03:** Hard blockers are the Phase 6 formal results/artifacts and the
  Phase 8 claim-gate trio:
  `08_CLAIM_EVIDENCE_MATRIX.md`, `08_SUPPORTED_CLAIMS.md`, and
  `08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md`.
- **D-04:** The blocked wording should be `Blocked: prerequisites missing`.
  This means required upstream evidence is absent, not that the research result
  failed.

### Reproduction Command Scope
- **D-05:** Reviewer-facing reproduction entry points should prioritize final
  evidence: final main tables/figures, Phase 6 formal artifacts, Phase 8 claim
  gate, and manuscript build.
- **D-06:** Pilot and legacy artifacts may appear in the manifest, but their
  role must be marked as `readiness`, `provenance`, or `legacy`, and they must
  not support headline claims.
- **D-07:** Diagnostic and supplementary commands should be layered by evidence
  role: `critical robustness`, `supplementary diagnostic`, and
  `legacy diagnostic`. Only Phase 8-supported evidence may enter main-text
  claims.
- **D-08:** Manuscript build reproducibility includes the LaTeX/PDF build and
  the table/figure generation chain: commands, input data paths, output PDF
  paths, output figure/table paths, and relevant script paths.

### Manifest Granularity
- **D-09:** `10_RESULT_MANIFEST.md` should use a layered manifest plus
  row-level index. First group by evidence family, then list each artifact.
- **D-10:** Each artifact row should include at least `path`, `role`,
  `evidence_family`, `status`, `source_command`, `inputs`, `outputs`,
  `code_revision`, `claim_link`, and `notes/blockers`.
- **D-11:** Checksums and dependency snapshots are recommended but not hard
  blockers. Phase 10 must record code revision and dependency commands; missing
  checksums or dependency snapshots should be listed as improvements.
- **D-12:** When Phase 8 is missing, artifact `claim_link` should be recorded as
  `pending Phase 8`, and the artifact must be marked unable to support final
  claims until the claim gate exists.

### Final Claim Verification Format
- **D-13:** `10_FINAL_VERIFICATION.md` should use a gate matrix that lists
  prerequisites, artifacts, tables/figures, claims, status, evidence paths, and
  blockers.
- **D-14:** Verification statuses should be `Pass`, `Pending`, `Blocked`, and
  `Not final evidence`.
- **D-15:** Claim verification must operate at the level of each final
  manuscript claim. Every final claim needs Phase 8 evidence, result artifacts,
  and table/figure links; missing evidence is marked `Blocked` or `Pending`.
- **D-16:** The final artifact index should appear as a human-readable section
  in `10_REPRODUCIBILITY.md`, while `10_RESULT_MANIFEST.md` keeps a structured
  table suitable for later JSON/CSV conversion.

### the agent's Discretion
The planner may choose exact table layouts, artifact-family headings, status
color labels, command formatting, optional checksum tooling, and whether to add
machine-readable companion files later, provided the three roadmap outputs
remain the canonical Phase 10 deliverables and the fail-closed policy is
preserved.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project and Phase Definition
- `.planning/ROADMAP.md` - Phase 10 goal, REP-01/REP-02 requirements, success
  criteria, and required outputs.
- `.planning/REQUIREMENTS.md` - Reproducibility requirements, claim-gate
  requirements, formal-experiment requirements, and final manuscript constraints.
- `.planning/PROJECT.md` - Core value, strict phase gates, pilot/formal
  separation, evidence-graded claims, reproducibility, and synthetic-data
  honesty.
- `.planning/STATE.md` - Current state: Phase 10 is ready to plan, while Phase
  8 claim-gate artifacts and Phase 6 formal result report are absent.

### Upstream Evidence and Claim Gates
- `.planning/phases/06-formal-synthetic-experiments/06-CONTEXT.md` - Formal
  evidence design decisions, required artifact manifests, main evidence matrix,
  supplementary package boundaries, failure/rerun rules, and Phase 8 handoff.
- `.planning/phases/06-formal-synthetic-experiments/06_FORMAL_SYNTHETIC_RESULTS.md` - Required upstream formal evidence report. Missing at context time;
  Phase 10 must mark this as a hard blocker until it exists.
- `.planning/phases/08-evidence-synthesis-and-claim-gate/08_CLAIM_EVIDENCE_MATRIX.md` - Required claim-to-evidence matrix. Missing at context time; hard
  blocker.
- `.planning/phases/08-evidence-synthesis-and-claim-gate/08_SUPPORTED_CLAIMS.md` - Required supported-claims list. Missing at context time; hard blocker.
- `.planning/phases/08-evidence-synthesis-and-claim-gate/08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md` - Required unsupported/exploratory-claims list. Missing
  at context time; hard blocker.

### Prior Phase Contracts
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_EXPERIMENT_CONTRACT.md` - Behavioral evidence versus diagnostic evidence
  boundaries.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_METRICS_DEFINITIONS.md` - Required metric names, formulas, denominator rules, and
  forbidden ambiguous metric language.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_STATISTICAL_PLAN.md` - Paired-seed and confidence-interval discipline.
- `.planning/phases/03-passenger-choice-model-rebuild/03_CHOICE_MODEL_CONTRACT.md` - Choice timing, status semantics, and utility-component logging contract.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04-CONTEXT.md` - Behavioral baseline, diagnostic role, output schema, and failure-row
  decisions.
- `.planning/phases/05-pilot-experiments/05-CONTEXT.md` - Pilot/formal
  separation and readiness-only status.
- `.planning/phases/05-pilot-experiments/05_PILOT_RESULTS.md` - Pilot results
  and readiness caveats; may be manifest provenance but not final evidence.

### Manuscript and Display Planning
- `.planning/phases/09-manuscript-restructure-for-tr-part-e/09-CONTEXT.md` - Manuscript restructuring decisions, claim-placeholder policy, and
  Phase 8 dependency.
- `.planning/phases/09-manuscript-restructure-for-tr-part-e/09_TABLE_FIGURE_PLAN.md` - Main table/figure contract, caption vocabulary checklist,
  reproducible script/data requirements, and limitations-before-insights policy.
- `manuscript/main.tex` - Current LaTeX entry point.
- `manuscript/sections/` - Manuscript section sources whose final claims must
  be checked after Phase 8.
- `manuscript/figures/scripts/` - Figure-generation scripts to document in the
  reproduction chain.
- `manuscript/figures/` - Generated figure outputs to manifest by evidence role.

### Codebase and Artifact Maps
- `.planning/codebase/CONVENTIONS.md` - Naming, code style, output, and command
  conventions.
- `.planning/codebase/STRUCTURE.md` - Repository layout, source directories,
  results directory, manuscript directory, figure script locations, and testing
  locations.
- `.planning/codebase/TESTING.md` - Pytest commands, runner smoke patterns, and
  reproducibility-oriented tests.
- `.planning/codebase/CONCERNS.md` - Reproducibility, artifact, metric,
  generated-output, and overclaiming risks that Phase 10 should surface.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `experiments/phase06_formal.py` and `tests/test_phase06_formal.py` are
  referenced by Phase 6 plans as the intended formal manifest and validation
  surface. If absent or incomplete, Phase 10 should report that gap instead of
  fabricating formal evidence.
- `experiments/runner.py` writes raw result rows, metrics tables, utility logs,
  status fields, and provenance fields that can feed the result manifest.
- `experiments/metrics.py` defines the formal metric vocabulary that Phase 10
  must use in table/figure verification.
- `results/pilot/phase05/` contains pilot/readiness artifacts that can be
  manifested as non-final evidence.
- `manuscript/figures/scripts/` and `manuscript/figures/` provide the expected
  figure-generation chain and generated outputs for manuscript reproducibility.

### Established Patterns
- Planning artifacts live under `.planning/phases/{phase-dir}/` with a
  zero-padded phase prefix.
- Formal evidence belongs under a clearly isolated formal results directory
  such as `results/formal/phase06/`; pilot outputs belong under
  `results/pilot/phase05/`.
- Result rows and manifest rows must carry evidence family and diagnostic role
  metadata so behavioral evidence, robustness evidence, diagnostics, legacy
  outputs, and manuscript displays cannot be mixed.
- Tests use deterministic generated scenarios, fixed seeds, and pytest smoke
  patterns rather than mocks.

### Integration Points
- Create `.planning/phases/10-reproducibility-package-and-final-verification/10_REPRODUCIBILITY.md`.
- Create `.planning/phases/10-reproducibility-package-and-final-verification/10_RESULT_MANIFEST.md`.
- Create `.planning/phases/10-reproducibility-package-and-final-verification/10_FINAL_VERIFICATION.md`.
- Read Phase 6 formal reports and Phase 8 claim-gate files when available; if
  missing, record hard blockers in all three Phase 10 artifacts.
- Inventory `results/`, `results/pilot/phase05/`, `manuscript/`, and the Phase
  9 display plan, but preserve the distinction between final evidence and
  provenance.

</code_context>

<specifics>
## Specific Ideas

- Use `Blocked: prerequisites missing` as the exact final-verification status
  when Phase 6/8 prerequisites are absent.
- Use `Pass`, `Pending`, `Blocked`, and `Not final evidence` as gate status
  values.
- Use `pending Phase 8` as the `claim_link` value when the claim gate is absent.
- Treat missing checksums and dependency snapshots as improvements, not hard
  blockers, while still recording code revision and dependency commands.
- Keep reviewer-facing reproduction entry points focused on final evidence and
  manuscript build; list pilot and legacy artifacts only as provenance.

</specifics>

<deferred>
## Deferred Ideas

None. Discussion stayed within Phase 10 scope.

</deferred>

---

*Phase: 10-Reproducibility Package and Final Verification*
*Context gathered: 2026-06-16T11:30:41+08:00*
