# Phase 9 Revised Introduction and Literature Positioning Plan

**Purpose:** Plan the new introduction and literature-positioning logic for a
Transportation Research Part E evidence-chain manuscript. This file is a
planning artifact, not final manuscript prose.

## Current Introduction Risks

The current introduction opens with a plausible DRT motivation, but it still
sets up the manuscript as a broad gap-filling method paper and previews old
effect-size results before the claim gate exists. It also uses risky novelty
language around prior meeting-point work and ends with a paper organization
that preserves the old model/algorithm/experiments/policy flow.

Risks to remove or quarantine:

- Overstating the novelty gap by implying prior work only handles pickup-side
  meeting points.
- Previewing unsupported numerical gains before Phase 8 supported claims exist.
- Treating algorithm diagnostics as a headline contribution rather than support
  evidence.
- Framing policy implications before limitations and boundary conditions.
- Mixing behavioral evidence, coverage controls, and diagnostics in the setup.

## Revised Introduction Flow

1. **Evidence problem first.** Open with the reviewer-facing fair-evidence
   problem: passenger response, coverage, baseline inconsistency, and
   diagnostic/result mixing can make meeting-point DRT look stronger or weaker
   than the evidence supports.
2. **Operational setting.** Explain why demand-responsive transit with walking
   access/egress creates a service-design problem for operators rather than a
   simple routing-only problem.
3. **Framework response.** Introduce the choice-aware dynamic service-design
   framework as an integrated simulation and evidence-chain tool, not as a
   broad first/only novelty claim.
4. **Claim discipline.** State that comparisons require shared passenger
   response, explicit denominators, paired seeds, coverage controls, and a
   claim-evidence gate.
5. **Research questions and contributions.** Present the three approved
   research questions and order contributions around evidence discipline,
   model/framework, experimental findings, and managerial implications.
6. **Paper organization.** Close with the TR-E evidence-chain structure.

## Paragraph-Level Outline

1. **Opening evidence-confounding paragraph.** Meeting-point DRT can reduce
   vehicle detours, but passenger response, coverage, baseline inconsistency,
   and diagnostic/result mixing can confound conclusions. The paragraph should
   make the fair-comparison problem the reason for the paper.
2. **DRT service-design paragraph.** Describe the operating challenge:
   bidirectional pickup/dropoff meeting points can support route consolidation,
   but only if passengers accept the offered walk, wait, fare, and in-vehicle
   travel trade-off.
3. **Literature gap paragraph.** Position prior DARP, meeting-point, walking
   ridepooling, passenger-choice, and rolling-horizon work as partially
   overlapping literatures. Avoid saying no prior work considers dropoff
   walking.
4. **Framework paragraph.** Introduce the integrated choice-aware dynamic
   service-design simulation framework, including shared passenger response,
   route-then-sample operation, rolling-horizon dispatch, and diagnostic
   solvers as support tools.
5. **Evidence-chain paragraph.** Explain the paper's evidence discipline:
   Phase 2 metric denominators, behavioral main comparisons, matched-coverage
   controls, fixed accepted-set diagnostics, paired seeds, and Phase 8 claim
   gating.
6. **Research questions and contribution paragraph.** Use the exact three
   research questions and contribution order defined below.
7. **Organization paragraph.** State that the manuscript proceeds through
   `Literature and Positioning`, `Framework and Solution Approach`,
   `Experimental Design and Evidence Families`, `Formal Main Evidence`,
   `Robustness, Equity, and Diagnostic Evidence`,
   `Limitations and Boundary Conditions`,
   `Managerial Insights and Boundary Conditions`, and `Conclusion`.

