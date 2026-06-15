# Phase 2: Experimental Contract and Metric Standardization - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md; this log preserves the alternatives considered.

**Date:** 2026-06-15
**Phase:** 2-Experimental Contract and Metric Standardization
**Areas discussed:** Experiment Family Boundary, Baseline Taxonomy Naming, Metric Denominator Contract, Coverage Confounding Controls, Output File Granularity

---

## Experiment Family Boundary

| Question | Options Presented | User's Choice |
|----------|-------------------|---------------|
| What should the main-evidence experiment primarily prove? | A. Operating vehicle-km savings versus door-to-door under consistent passenger response; B. Full tradeoff among coverage, acceptance, and operating efficiency; C. All experiment families equal | B |
| How should behavioral choice experiments relate to deterministic diagnostics? | A. Strictly separate behavioral main evidence from deterministic diagnostics; B. Show side by side with clear labels; C. Mix in one table with footnotes | A |
| What role should fixed accepted-set routing diagnostics play? | A. Core supplementary diagnostic for same-passenger routing efficiency; B. Main evidence equal to behavioral results; C. Phase 4 algorithm validation only | A |
| How should ALNS/MILP exact results enter the Phase 2 contract? | A. Small-scale algorithm diagnostics only; B. Part of the main experiment; C. Leave detailed definition to Phase 4 | C |

**Notes:** Main evidence should explain tradeoffs, not just vehicle-km savings. Deterministic and algorithmic diagnostics must not be mixed into behavioral service-design claims.

---

## Baseline Taxonomy Naming

| Question | Options Presented | User's Choice |
|----------|-------------------|---------------|
| What should be the primary structure of the baseline taxonomy? | A. Four-axis taxonomy; B. Code variant first; C. Paper table first | A |
| How should the current FullModel name be handled? | A. Replace with descriptive method label; B. Keep as code name but use display name; C. Keep unchanged | A |
| How should SingleSidedPickup and SingleSidedDropoff be positioned? | A. Formal service-design baselines with same choice/routing setup; B. Supplementary diagnostics only; C. Do not require SingleSidedDropoff yet | A |
| What passenger response should DoorToDoor use in behavioral experiments? | A. Same choice model as meeting-point services; B. Deterministic all-accept; C. Report behavioral and deterministic DoorToDoor separately | A |

**Notes:** The taxonomy should prevent recurrence of the current problem where only `FullModel` uses passenger response. `FullModel` should not remain the paper-facing method name.

---

## Metric Denominator Contract

| Question | Options Presented | User's Choice |
|----------|-------------------|---------------|
| Which coverage and acceptance metrics must appear together in the main table? | A. `served_share`, `behavioral_acceptance_rate`, `choice_rejection_rate`, `feasibility_rejection_rate`; B. `served_share` only; C. `served_share` plus behavioral acceptance | A |
| How should `served_share` be defined? | A. Final served/completed requests divided by original requests; B. Passenger-accepted requests divided by original requests; C. Algorithm-inserted requests divided by original requests | A |
| How should `vkm_per_trip` be named and reported? | A. Use `vkm_per_served_trip` and `vkm_per_original_request`; B. Keep `vkm_per_trip` with documented denominator; C. Report only total vehicle-km | A |
| What record granularity is required for rejection and service status? | A. Request-level durable status; B. Aggregate-level counts only; C. Define formulas now and status later | A |

**Notes:** The metric contract must make denominator switching visible and should require request-level status rows.

---

## Coverage Confounding Controls

| Question | Options Presented | User's Choice |
|----------|-------------------|---------------|
| Which main method should matched-coverage control use? | A. Target served-share cap; B. Post-hoc random sampling match; C. Fixed accepted-set rerun | A |
| What status should matched-coverage have in the evidence chain? | A. Core supplementary evidence; B. Equal headline evidence with unconstrained behavioral results; C. Robustness appendix only | A |
| How should unconstrained results be framed if lower vehicle-km comes with lower `served_share`? | A. Coverage-efficiency tradeoff; B. Still claim superiority while disclosing lower `served_share`; C. Ignore unconstrained result | A |
| Which requests should fixed accepted-set diagnostics hold fixed? | A. Common serviceable/accepted intersection across all methods; B. BidirectionalMP accepted set; C. DoorToDoor accepted set | A |

**User clarification:** Matched-coverage should be a core supplementary experiment in the main text using served-share cap control. Fixed accepted-set should remain a diagnostic experiment using the intersection of requests commonly serviceable/accepted by all methods, avoiding bias toward any one service design.

---

## Output File Granularity

| Question | Options Presented | User's Choice |
|----------|-------------------|---------------|
| How should Phase 2 outputs be structured? | A. Five independent files; B. One main file with all sections; C. One main file plus metric/statistical appendices | C |
| How deep should the statistical plan go? | A. Principles only; B. Concrete tests/formulas without final sample size lock; C. Full statistical scheme including final seed count | B |
| Should metric definitions include forbidden or high-risk metrics? | A. Include forbidden/high-risk metric list; B. Positive definitions only; C. Put forbidden metrics elsewhere | A |
| Should Phase 2 output a code-change task list for later phases? | A. Output later code-change task list without implementation; B. Concept contract only; C. Only list minimal schema/variant gaps | A |

**User clarification:** Phase 2 should use one main experiment contract file plus two standalone appendices. The main file locks experiment design, service variants, main/supplementary evidence, and claim boundaries. Metric definitions and the statistical plan should be standalone so later code and manuscript tables can cite them. The statistical plan should specify paired seeds, paired differences, confidence intervals, and concrete computations without locking the final seed count. Metric definitions must include forbidden or high-risk metrics. Phase 2 should also output Phase 4/5 code-change tasks without implementing code in Phase 2.

---

## the agent's Discretion

- The planner may choose exact document filenames and whether the Phase 4/5 code-change task list is embedded in the main contract or split into a separate file.

## Deferred Ideas

- Passenger choice calibration belongs to Phase 3.
- Detailed ALNS/MILP scope belongs to Phase 4.
- Pilot execution belongs to Phase 5.
- Formal final seed count belongs to Phase 6.
- Final claim approval and manuscript wording belong to Phase 8/9.
