# Requirements: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

**Defined:** 2026-04-11
**Updated:** 2026-04-13 (v4.0 milestone)
**Core Value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.

---

## v4.0 Requirements (Active)

### Comparison Design

- [ ] **COMP-01**: Implement `DoorToDoorCapped` variant — DoorToDoor with an acceptance cap that limits served share to ≈ FullModel's mean (~23.5%); re-route remaining accepted trips using the same ALNS heuristic
- [ ] **COMP-02**: Run `DoorToDoorCapped` experiment (seeds 42/43/44, n=200, 15 vehicles) and record vkm/trip at matched served share
- [ ] **COMP-03**: Update Section 5.2 to present endogenous matched-coverage result as the primary efficiency claim; demote post-hoc 74.3% to supplementary footnote

### Behavioral Consistency

- [ ] **BEHAV-01**: Add a units/variables reference table to the paper (or appendix) listing all time variables with units (seconds vs minutes), walking variables (meters), and fare (CNY)
- [ ] **BEHAV-02**: Add one worked numerical utility example showing how U_{rb}^k is computed for a representative request, with explicit unit conversions
- [ ] **BEHAV-03**: Add a paragraph reconciling offer-stage predicted attributes (wait, IVT, walk) with realized attributes after rolling-horizon re-optimization; state the commitment assumption explicitly

### Text Fixes

- [ ] **TEXT-01**: Replace "2383.85 vs 3662.33" and "-34.9%" in `paper/sections/intro.tex` (contribution list item 3) with v3.0 numbers
- [ ] **TEXT-02**: Replace "2383.85 vs 3662.33" and "34.9%" in the conclusion section with v3.0 numbers
- [ ] **TEXT-03**: Verify no other occurrences of old numbers remain in any paper section

### Literature

- [ ] **LIT-01**: Add Fielbaum, Bai & Alonso-Mora (2021) "On-demand ridesharing with optimized pick-up and drop-off walking locations" (TR Part C, DOI: 10.1016/j.trc.2021.103061) to `paper/references.bib`
- [ ] **LIT-02**: Add 1-2 sentences in Section 2.2 (Meeting Points and Virtual Stops) positioning this paper relative to Fielbaum et al. (2021): they study ridepooling with flexible walking, not DRT with MNL choice + rolling horizon

### Robustness

- [ ] **ROB-01**: Add mean +/- std notation to Table 1 (main results) for acceptance rate, vkm, and vkm/trip
- [ ] **ROB-02**: Add a brief note in Section 5.1 (Experimental Setup) clarifying that 3 seeds is standard in DRT simulation literature and citing Wu et al. (2025) as precedent

---

## Validated Requirements (v1.0-v3.0)

### v1.0 (Problem Formulation & Algorithm)
- [x] PROB-01..05: Many-to-many DRT problem with bidirectional meeting point sets formally defined
- [x] CHOICE-01..04: MNL utility function, outside option, three passenger types, binary logit acceptance
- [x] EXACT-01..04: MILP formulation with Gurobi, ex-post benchmark role
- [x] HEUR-01..06: Rolling horizon ALNS with 5 operators, <1s per request
- [x] EXP-01..09: Synthetic + semi-realistic experiments, 6 variants, 9 metrics
- [x] POLICY-01..06: Sensitivity sweeps, equity analysis, 5 policy recommendations
- [x] PAPER-01..10: Full paper written in academic English
- [x] FIG-01..06: All 6 publication-quality figures produced

### v2.0 (Reviewer Revision)
- [x] REV-01..04: Binary logit replacing multi-bundle MNL; single-offer mechanism justified
- [x] REV-05..08: Gamma sweep Pareto frontier; MILP labeled as ex-post routing lower bound; VOT mapping

### v3.0 (Codex Review Fixes)
- [x] METRIC-01/02: vkm/trip corrected to vkm/(n x alpha); all tables/abstract/policy updated
- [x] COVER-01/02: Post-hoc matched-coverage experiment (10.9 vs 42.3, 74.3%); Section 5.2 updated
- [x] FORM-01/02: Timing/decision diagram (tab:timing-diagram); ALNS online objective (eq:alns-objective)
- [x] PFRAM-01..03: Generalizability caveats for R1 and R2; reviewer response v3.0 section

---

## Out of Scope

| Feature | Reason |
|---------|--------|
| Pricing as decision variable | Avoid overlap with Work 1/2 |
| Reinforcement learning as main method | Extension discussion only |
| Real GPS/smart card data | Simulation-based standard for DARP |
| TR Part D environmental framing | Wrong journal |
| Multi-bundle MNL with single-offer mechanism | Behaviorally inconsistent (v2.0 decision) |
| Endogenous meeting point placement | Outside scope; future work |

---

## Traceability (v4.0)

| Requirement | Phase | Status |
|-------------|-------|--------|
| COMP-01 | Phase 12 | Pending |
| COMP-02 | Phase 12 | Pending |
| COMP-03 | Phase 12 | Pending |
| BEHAV-01 | Phase 13 | Pending |
| BEHAV-02 | Phase 13 | Pending |
| BEHAV-03 | Phase 13 | Pending |
| TEXT-01 | Phase 13 | Pending |
| TEXT-02 | Phase 13 | Pending |
| TEXT-03 | Phase 13 | Pending |
| LIT-01 | Phase 13 | Pending |
| LIT-02 | Phase 13 | Pending |
| ROB-01 | Phase 13 | Pending |
| ROB-02 | Phase 13 | Pending |

**Coverage:**
- v4.0 requirements: 13 total
- Mapped to phases: 13
- Unmapped: 0 (check mark)

---
*Requirements defined: 2026-04-11*
*Last updated: 2026-04-13 — v4.0 milestone (GPT-5 review fixes)*
