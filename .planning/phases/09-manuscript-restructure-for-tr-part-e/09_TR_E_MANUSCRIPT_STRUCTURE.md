# Phase 9 TR-E Manuscript Structure

**Purpose:** Source-of-truth manuscript architecture for restructuring the
current draft into a Transportation Research Part E evidence-chain manuscript.

## Current Manuscript Diagnosis

The current manuscript is organized around a method-and-policy story: the master
file targets Transportation Research Part A, then proceeds from introduction and
literature to separate model, algorithm, experiments, policy, and conclusion
sections. That order keeps useful technical material, but it lets old numerical
claims, diagnostic results, and policy-style language appear before the rebuilt
claim gate has approved them.

Primary diagnosis:

- The dominant story is still "the method wins" rather than evidence-chain
  reconstruction.
- `manuscript/main.tex` currently targets Transportation Research Part A and
  must be updated later if the paper is finalized for Transportation Research
  Part E.
- The current experiment section mixes behavioral comparisons, matched-coverage
  diagnostics, MILP/ALNS diagnostics, Beijing-inspired synthetic results,
  sensitivity, equity, gamma/welfare, and weight sensitivity.
- The current policy section should become `Managerial Insights and Boundary
  Conditions`, with limitations stated before applied implications.
- The current Beijing/city language must remain `Beijing-inspired synthetic
  scenario` unless later case-study evidence supports stronger wording.

## TR-E Evidence-Chain Architecture

The target manuscript structure should make the evidence chain visible before
the reader reaches any result or managerial implication:

1. **Introduction** - evidence gap, research questions, contribution order, and
   claim discipline.
2. **Literature and Positioning** - prior DARP, meeting-point, ridepooling,
   passenger-choice, and rolling-horizon work, with no broad first/only claims.
3. **Framework and Solution Approach** - choice-aware service-design framework,
   passenger response, route-then-sample operation, rolling-horizon ALNS, and
   clearly labeled diagnostics.
4. **Experimental Design and Evidence Families** - service-design variants,
   response assumptions, metrics, paired design, and evidence-family roles.
5. **Formal Main Evidence** - claim-gated behavioral comparisons only.
6. **Robustness, Equity, and Diagnostic Evidence** - matched coverage, fixed
   accepted-set controls, utility sensitivity, equity summaries, and scoped
   algorithm diagnostics.
7. **Limitations and Boundary Conditions** - synthetic-data, calibration,
   case-study, algorithm-diagnostic, and claim-gate limits before implications.
8. **Managerial Insights and Boundary Conditions** - conditional insights, not
   universal city-policy prescriptions or parameter rules.
9. **Conclusion** - evidence-graded takeaways, unresolved limits, and future
   work.

## Old-to-New Section Map

| Current source | Current role | Target section role |
|---|---|---|
| `manuscript/main.tex` | Journal target, title, front matter, include order, appendix, bibliography | Update target-journal metadata from Transportation Research Part A to Transportation Research Part E during later manuscript-edit execution; revise include order to match the TR-E evidence-chain architecture. |
| `manuscript/sections/abstract.tex` | Old abstract, keywords, legacy numerical claims | Rebuild via `Introduction` framing plus claim-gated front matter; final wording waits for Phase 8 supported claims. |
| `manuscript/sections/intro.tex` | Motivation, broad gap, contribution list, organization | `Introduction`, with evidence-confounding problem first and conditional research questions before claims. |
| `manuscript/sections/literature.tex` | DARP, meeting points, passenger choice, dynamic scheduling, positioning | `Literature and Positioning`, with precise overlap language and no unverified first/only statements. |
| `manuscript/sections/model.tex` | Problem formulation, passenger choice, three-layer model | `Framework and Solution Approach`, especially framework, utility, response, feasibility, and model architecture material. |
| `manuscript/sections/algorithm.tex` | MILP diagnostic, rolling-horizon ALNS, complexity | `Framework and Solution Approach` for operational mechanism; diagnostic solver details may be scoped or moved to appendix/supplement. |
| `manuscript/sections/experiments.tex` | Mixed setup, main results, diagnostics, case, sensitivity, equity, welfare, weight sensitivity | Split across `Experimental Design and Evidence Families`, `Formal Main Evidence`, and `Robustness, Equity, and Diagnostic Evidence`. |
| `manuscript/sections/policy.tex` | R1-R5 policy recommendations, VOT interpretation, deployment map | `Limitations and Boundary Conditions` plus `Managerial Insights and Boundary Conditions`, using conditional insight templates. |
| `manuscript/sections/conclusion.tex` | Old result recap, contributions, policy implications, limitations | `Conclusion`, with Phase 8-supported claims only and unsupported/exploratory items moved to limitations or future work. |

