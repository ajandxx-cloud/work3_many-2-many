---
phase: 06-academic-figures-visualization
status: Ready for planning
gathered: "2026-04-12"
source: Autonomous execution (derived from roadmap, requirements, and Phase 3/4/5 artifacts)
---

# Phase 6: Academic Figures & Visualization — Context

**Gathered:** 2026-04-12
**Status:** Ready for planning
**Source:** Autonomous execution (derived from roadmap, requirements, and Phase 3/4/5 artifacts)

<domain>
## Phase Boundary

Phase 6 delivers all six publication-quality figures for the TR Part A paper. Figures are produced in Python/matplotlib, exported at 300 dpi as PDF/EPS, and placed in `figures/` so that `paper/main.tex` can include them. Phase 5 created placeholder comments in the section files; this phase replaces those placeholders with real figure files.

This phase depends on:
- Phase 1: model structure (for FIG-01, FIG-02)
- Phase 2: algorithm design (for FIG-03)
- Phase 3/4: numerical results (for FIG-04, FIG-05, FIG-06)
- Phase 5: paper sections with figure labels (fig:three-layer, fig:algorithm, fig:baseline-comparison, fig:sensitivity, fig:policy-map)

</domain>

<decisions>
## Implementation Decisions

### Figure Format
- Python/matplotlib for all figures (consistent with Phase 3/4 analysis code)
- Export format: PDF (vector, preferred for LaTeX) + PNG at 300 dpi (fallback)
- Output directory: `figures/` (relative to project root)
- Figure size: single-column (88mm wide) or double-column (180mm wide) per TR Part A guidelines
- Font: serif (matching LaTeX body text), size 9-10pt for axis labels

### Figure List (6 figures)
1. FIG-01 — System overview: many-to-many DRT with bidirectional meeting points
   - Shows: origin nodes, destination nodes, meeting point grid, vehicle routes, passenger walking legs
   - Style: schematic diagram (not data-driven), uses matplotlib patches/arrows
   - Label in paper: fig:system-overview (new) or fig:three-layer (existing placeholder)

2. FIG-02 — Three-layer model architecture diagram
   - Shows: Layer 1 (offer generation) → Layer 2 (passenger response) → Layer 3 (dispatch)
   - Style: flowchart/block diagram using matplotlib
   - Label in paper: fig:three-layer

3. FIG-03 — Algorithm flowchart: online insertion + rolling horizon + ALNS
   - Shows: request arrival → candidate generation → insertion evaluation → MNL check → ALNS re-opt loop
   - Style: flowchart with decision diamonds
   - Label in paper: fig:algorithm

4. FIG-04 — Experiment result charts: baseline comparison
   - Data: results/metrics_table.csv (6 variants × 9 metrics)
   - Shows: grouped bar charts for acceptance rate and vkm across 6 variants
   - Label in paper: fig:baseline-comparison

5. FIG-05 — Sensitivity analysis heatmaps/line plots
   - Data: results/sensitivity_walk.csv + results/sensitivity_fleet.csv
   - Shows: (a) acceptance rate vs walking tolerance ρ; (b) acceptance rate vs fleet size
   - Label in paper: fig:sensitivity

6. FIG-06 — Policy insight visualization: benefit map
   - Data: derived from policy_recommendations.md + sensitivity results
   - Shows: recommended service mode by demand density × walking tolerance (heatmap or contour)
   - Label in paper: fig:policy-map

### Plan Structure (3 plans)
- Plan 01: Conceptual diagrams — FIG-01 (system overview), FIG-02 (three-layer), FIG-03 (algorithm flowchart)
- Plan 02: Data-driven charts — FIG-04 (baseline comparison), FIG-05 (sensitivity)
- Plan 03: Policy visualization + LaTeX integration — FIG-06 (policy map) + update paper/main.tex to include figures

### Python Environment
- Use existing `src/drt/` package environment (pyproject.toml already set up)
- matplotlib, numpy, pandas already available (used in Phase 3/4)
- Figure scripts go in `figures/scripts/` directory
- Generated figures go in `figures/` directory

### Claude's Discretion
- Exact color palette (suggest: muted academic palette, colorblind-friendly)
- Exact layout within each figure
- Whether to use subplots or separate files for multi-panel figures
- Exact arrow styles and node shapes for diagrams

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase 3/4 Results (source of truth for data)
- `results/metrics_table.csv` — 6 variants × 9 metrics (FIG-04 data)
- `results/sensitivity_walk.csv` — walking tolerance sweep (FIG-05a data)
- `results/sensitivity_fleet.csv` — fleet size sweep (FIG-05b data)
- `results/equity_table.csv` — per-type acceptance rates + Gini (FIG-04 equity panel)
- `results/policy_recommendations.md` — 5 recommendations with thresholds (FIG-06 data)

### Phase 5 Paper Sections (figure labels used in paper)
- `paper/sections/model.tex` — contains fig:three-layer placeholder
- `paper/sections/algorithm.tex` — contains fig:algorithm placeholder
- `paper/sections/experiments.tex` — contains fig:baseline-comparison, fig:sensitivity placeholders
- `paper/sections/policy.tex` — contains fig:policy-map placeholder

### Phase 1 Model (for conceptual diagrams)
- `model/notation.tex` — M_r^P, M_r^D symbols
- `model/three-layer.tex` — three-layer model description

### Project State
- `.planning/STATE.md` — key decisions
- `.planning/REQUIREMENTS.md` — FIG-01..06 requirements

</canonical_refs>

<specifics>
## Specific Ideas

### FIG-01 System Overview
- Show a small grid (e.g., 3×3) of meeting points
- Draw 2-3 passenger origin/destination pairs with arrows to their assigned MPs
- Draw 1-2 vehicle routes connecting pickup MPs to dropoff MPs
- Walking legs shown as dashed arrows from origin to pickup MP and from dropoff MP to destination
- Annotate: M_r^P (pickup meeting point), M_r^D (dropoff meeting point)

### FIG-04 Baseline Comparison
- Two-panel figure: left = acceptance rate, right = vkm
- 6 bars per panel, one per variant
- Color-code: FullModel in a distinct color (e.g., dark blue), DoorToDoor in gray
- Add horizontal reference line at DoorToDoor level for vkm panel
- Annotate the −34.9% efficiency gain

### FIG-05 Sensitivity
- Two-panel: (a) line plot of acceptance rate vs ρ for FullModel and DoorToDoor; (b) line plot vs fleet size
- Mark the ρ=1000m threshold with a vertical dashed line
- Mark the n=20 diminishing returns point

### FIG-06 Policy Map
- 2D heatmap: x-axis = walking tolerance ρ (200-1000m), y-axis = demand density (requests/day)
- Color = recommended service mode (Tier 1/2/3)
- Overlay the three-tier boundaries from policy_recommendations.md

</specifics>

<deferred>
## Deferred Ideas

- Interactive/web figures (not needed for TR Part A submission)
- Supplementary figures beyond the 6 required
- Animated diagrams

</deferred>

---

*Phase: 06-academic-figures-visualization*
*Context gathered: 2026-04-12 (autonomous execution)*
