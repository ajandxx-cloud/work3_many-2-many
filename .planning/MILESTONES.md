# MILESTONES: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

## v1.0 — Initial Paper Draft (Completed 2026-04-12)

**Goal:** Produce a complete, submission-ready first draft of the TR Part A paper with all sections, figures, and supporting code.

**Delivered:**
- Phase 1: Problem formulation, notation, three-layer model (LaTeX)
- Phase 2: MILP + rolling horizon ALNS implementation (Python/Gurobi)
- Phase 3: Numerical experiments — 6 variants, 9 metrics, synthetic + Beijing scenarios
- Phase 4: Policy analysis — sensitivity sweeps, equity analysis, 5 recommendations
- Phase 5: Full paper draft — 8 section files, 59 BibTeX entries
- Phase 6: 6 publication-quality figures (PDF + PNG, matplotlib)

**Key results:**
- FullModel vkm/accepted trip: 2383.85 vs DoorToDoor 3662.33 (−34.9%)
- Equity Gini = 0.1216 across three passenger types
- Walking threshold: ρ ≥ 1000m minimum viable for bidirectional DRT
- Fleet recommendation: ≥15 vehicles per 100 peak requests

**Codex review (GPT-5.2):** Round 1 = 5/10 (weak reject) → Round 2 = 6/10 (weak accept)

**Remaining issues for v2.0:**
- CRITICAL: MNL multi-bundle vs single-offer behavioral inconsistency
- MAJOR: Coverage–efficiency Pareto frontier missing
- MAJOR: MILP benchmark scope unclear under stochastic acceptance
- MAJOR: Objective weights lack policy/VOT interpretation

---

*Milestones file created: 2026-04-12*
