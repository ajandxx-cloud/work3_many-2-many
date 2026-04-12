---
plan: 05-03
status: complete
files_created: [paper/sections/model.tex, paper/sections/algorithm.tex]
---

## Summary

Wrote `paper/sections/model.tex` (2298 words) covering Sections 3–5: Problem Formulation
(network, service offer bundle, 5-component objective, 14 operational constraints, online
decision vector), Passenger Choice Model (MNL utility eq:utility, outside option, choice
probability eq:choice-prob, three passenger types with β values), and Three-Layer Coupled
Model (Layer 1 bundle generation, Layer 2 Bernoulli acceptance eq:acceptance-indicator,
Layer 3 rolling horizon re-optimization eq:rh-trigger, coupling table tab:layer-coupling,
figure placeholder fig:three-layer).

Wrote `paper/sections/algorithm.tex` (1046 words) covering Section 6: Solution Methodology
with MILP exact formulation (Gurobi, decision variables, constraint references), Rolling
Horizon ALNS heuristic (candidate generation, online insertion evaluation, 5 ALNS operators
per HEUR-05, rolling horizon loop with H=30min/Δ=5min, algorithm placeholder alg:rh-alns,
citations ropke2006 and bent2004), and Computational Complexity (NP-hardness via DARP
reduction, per-step complexity analysis, practical performance benchmark).

All Phase 1 equation labels reproduced verbatim. Zero notation drift from model/notation.tex.
