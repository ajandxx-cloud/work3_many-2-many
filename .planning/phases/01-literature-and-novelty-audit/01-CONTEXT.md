# Phase 1: Literature and Novelty Audit - Context

**Gathered:** 2026-06-15
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 1 audits the manuscript's literature positioning and novelty claims before any manuscript rewrite or new experiment design. It must decide what the paper can safely claim about bidirectional pickup/dropoff meeting points, passenger choice, rolling-horizon dispatch, and many-to-many DRT integration.

In scope:
- Audit prior work on DARP with meeting points, pickup/dropoff walking locations, ridepooling with bidirectional walking, choice-based DRT, rolling-horizon DRT, and ALNS for DRT/DARP.
- Identify whether current "first", "gap", and "existing work only..." statements are defensible.
- Reframe the contribution around the strongest defensible integrated-system claim.
- Resolve whether the rebuild should target TR-E quality/framing or stay closer to the current TR-A policy framing.

Out of scope:
- Running experiments.
- Editing manuscript prose directly.
- Redesigning metrics or baselines in detail; those belong to Phase 2.
- Final claim approval; that belongs to Phase 8 after formal evidence exists.

</domain>

<decisions>
## Implementation Decisions

### Literature Corpus Boundary
- **D-01:** Treat the Phase 1 corpus as broader than the current bibliography. It must include DARP with meeting points, DARPmp, pickup/dropoff walking locations, static ridepooling with bidirectional walking, choice-based DRT/ridepooling, online/rolling-horizon DRT, and ALNS/heuristic DARP validation.
- **D-02:** The audit must explicitly check the review-note targets: Cortenbach et al. (2024), Fielbaum et al. (2021), Wu et al. (2025), Alonso-Mora-style dynamic assignment work, and any cited literature that could already cover pickup/dropoff walking locations.

### Novelty Standard
- **D-03:** Default to a conservative novelty threshold. Do not preserve "first", "only", or "existing work assigns meeting points only on pickup side" unless Phase 1 verifies that exact scoped claim.
- **D-04:** The preferred contribution fallback is an integrated-framework claim: combining bidirectional pickup/dropoff meeting-point sets, simulated binary-logit acceptance, online rolling-horizon dispatch, many-to-many DRT, and equity/coverage diagnostics in one simulation framework.

### Journal Positioning
- **D-05:** Phase 1 should compare two story positions: TR-E / operations-oriented evidence-chain framing versus the current TR-A / policy-implication framing.
- **D-06:** Use TR-E-level rigor as the planning bar even if the final venue remains undecided. This means conservative claims, stronger methodological taxonomy, and cleaner reproducibility expectations.

### Output Format
- **D-07:** Produce a citation-by-claim matrix. Rows should include cited work, problem setting, meeting-point scope, passenger response, dynamic/online component, algorithmic method, and implication for this paper's novelty.
- **D-08:** Produce a revised contribution-positioning memo with allowed, risky, and forbidden wording.
- **D-09:** Preserve unresolved literature gaps as explicit Phase 1 blockers rather than papering over them.

### the agent's Discretion

The planner may choose the exact table schema and file split as long as Phase 1 outputs include a literature audit, novelty-positioning memo, revised research questions, and updates to `.planning/CLAIMS_AND_RISKS.md`.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase Definition
- `.planning/ROADMAP.md` - Phase 1 goal, requirements, and success criteria.
- `.planning/REQUIREMENTS.md` - POS-01, POS-02, and POS-03 requirements.
- `.planning/PROJECT.md` - Project framing, core value, constraints, and Phase 0 decisions.
- `.planning/STATE.md` - Current status and Phase 0 caveats.

### Phase 0 Audit Inputs
- `.planning/phases/00-repository-and-manuscript-audit/00-01-SUMMARY.md` - Phase 0 close-out and decisions.
- `.planning/phases/00-repository-and-manuscript-audit/00-VERIFICATION.md` - Phase 0 verification result and residual risks.
- `.planning/phases/00-repository-and-manuscript-audit/00_MANUSCRIPT_CLAIM_AUDIT.md` - Current claim classifications and section-level risk scan.
- `.planning/phases/00-repository-and-manuscript-audit/00_REPOSITORY_AUDIT.md` - Routed blockers and manuscript/code artifact map.
- `.planning/phases/00-repository-and-manuscript-audit/00_CURRENT_EXPERIMENT_MAP.md` - Current result provenance and evidence caveats.

### Manuscript and Review Sources
- `manuscript/sections/abstract.tex` - Current novelty and headline claim wording.
- `manuscript/sections/intro.tex` - Claimed contributions and research positioning.
- `manuscript/sections/literature.tex` - Current literature table and gap statement.
- `manuscript/sections/model.tex` - Model scope, binary-logit response, and value-of-time discussion.
- `manuscript/sections/conclusion.tex` - Contribution summary and limitations wording.
- `manuscript/references.bib` - Current bibliography to audit and extend.
- `docs/工作3讨论-6.14.md` - Readable review-note risk source when available.
- `docs/宸ヤ綔3璁ㄨ-6.14.md` - Mojibake filename/path copy referenced by existing state; use only if readable.

### Codebase Context
- `.planning/codebase/CONVENTIONS.md` - Documentation and file conventions.
- `.planning/codebase/STRUCTURE.md` - Location of manuscript, docs, results, and experiment source.
- `.planning/codebase/CONCERNS.md` - Prior known concerns that affect novelty and evidence framing.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `manuscript/references.bib`: Starting bibliography for literature and novelty audit.
- `manuscript/sections/literature.tex`: Current gap table and prior-work positioning to verify.
- `.planning/phases/00-repository-and-manuscript-audit/*`: Phase 0 evidence and risk register for the literature audit.
- `.planning/CLAIMS_AND_RISKS.md`: Existing claim/risk register to update if present.

### Established Patterns
- Planning and audit artifacts live under `.planning/phases/{NN}-{slug}/` with numbered phase prefixes.
- Active manuscript text lives under `manuscript/sections/`; Phase 1 should not edit manuscript prose yet.
- Current source and docs contain some encoding damage; agents should cite concrete file paths and avoid relying on garbled text where a readable copy exists.

### Integration Points
- Phase 1 outputs feed Phase 2 experiment taxonomy, Phase 8 claim gate, and Phase 9 manuscript restructuring.
- Literature and novelty decisions should update `.planning/CLAIMS_AND_RISKS.md` rather than directly changing final paper claims.

</code_context>

<specifics>
## Specific Ideas

- Treat "bidirectional meeting points" alone as a risky novelty claim until audited.
- Prefer "integrated choice-aware dynamic service-design simulation framework" as the conservative contribution center.
- Keep Chinese-city policy framing conditional and secondary unless later phases add stronger empirical/case evidence.

</specifics>

<deferred>
## Deferred Ideas

- Final manuscript language changes belong to Phase 9 after the Phase 8 claim gate.
- Detailed metric definitions, baseline taxonomy, and coverage-confounding controls belong to Phase 2.
- Real/semi-real Beijing case-study decisions belong to Phase 7.

</deferred>

---

*Phase: 1-Literature and Novelty Audit*
*Context gathered: 2026-06-15*
