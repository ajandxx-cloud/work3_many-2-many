# Work 3 — Bidirectional Meeting Point Assignment & Dynamic Routing for Many-to-Many DRT

**Target journal:** *Transportation Research Part E: Logistics and Transportation Review*

This project studies **bidirectional meeting-point DRT service design** for many-to-many
demand-responsive transit (DRT), with pickup and dropoff consolidation evaluated through
passenger-response-aware simulation and rolling-horizon routing. It extends Work 1
(many-to-one, dynamic pricing) and Work 2 (service menu design) to the many-to-many
setting, with logistics and operations framing around conditional service-design
trade-offs rather than policy validation.

---

## Directory Structure

```
3.工作3/
├── README.md                 # this file
├── CLAUDE.md                 # Claude Code project instructions
├── pyproject.toml            # Python package config (package: drt)
├── run_experiments.py        # root entry point — runs all experiments
├── .gitignore
│
├── src/drt/                  # core algorithm library
│   ├── milp.py               #   exact MILP (Gurobi)
│   ├── alns.py               #   ALNS heuristic (large-scale)
│   ├── choice.py             #   MNL passenger choice model
│   ├── insertion.py          #   insertion-based construction
│   ├── feasibility.py        #   feasibility checks
│   ├── candidate.py          #   candidate meeting-point generation
│   └── types.py              #   data structures
│
├── tests/                    # pytest test suite
├── analysis/                 # post-hoc analysis (equity, policy, sensitivity)
├── experiments/              # experiment runners (config, scenarios, metrics, variants)
├── results/                  # experiment outputs (CSV / JSON / MD)
│
├── manuscript/               # the paper (LaTeX) — canonical current submission
│   ├── main.tex              #   master document
│   ├── references.bib
│   ├── cover_letter.tex
│   ├── response_to_reviewers.tex
│   ├── main.pdf              #   compiled output
│   ├── sections/             #   abstract, intro, literature, model, algorithm,
│   │                         #   experiments, policy, conclusion
│   └── figures/              #   publication figures (PDF + PNG)
│       └── scripts/          #     Python scripts that generate each figure
│
├── docs/                     # human-written documentation & notes
│   ├── proposal/             #   PhD proposal (开题报告)
│   └── notes/                #   discussion notes
│
└── archive/                  # superseded / historical material (kept, not in active use)
    ├── model_draft/          #   early standalone Phase-1 LaTeX model (absorbed into manuscript)
    ├── pre_revision_results/ #   results snapshot before the latest paper revision
    ├── debug_scripts/        #   throwaway debug scripts
    ├── adhoc_tests/          #   one-off scale / smoke tests (not the pytest suite)
    ├── output_logs/          #   captured run/debug output
    └── paper_full_v3.txt     #   superseded full-text dump of an earlier draft
```

> **Tooling folders** (not shown): `.claude/` (Claude Code settings + agent worktrees),
> `.git/` (version control), `.planning/` (GSD workflow state).

---

## How to Run

### Install
```bash
pip install -e .            # installs the `drt` package (editable) per pyproject.toml
pip install -e ".[dev]"     # adds pytest, pytest-benchmark
```
Core dependencies: `gurobipy`, `numpy` (see `pyproject.toml`).

### Run experiments
```bash
python run_experiments.py   # from project root — writes results/ and prints a summary
```

### Tests
```bash
pytest                      # runs the test suite in tests/
```

### Compile the manuscript
From inside `manuscript/`:
```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main               # produces main.pdf (requires elsarticle.cls)
```
Figure scripts live in `manuscript/figures/scripts/` and write into `manuscript/figures/`.
Run them from inside `manuscript/` (they use relative paths).

---

## Known Issues (not blocking; recorded for later)

1. **Git repository is currently broken.** The project folder was renamed
   (`工作3` → `3.工作3`) but `.git/` still points at the old path — `git status` fails, and
   the index references old `paper/` / `paper_work3/` paths that no longer exist while the
   current `manuscript/` tree is untracked. **To repair later:** fix `.git/config` hooksPath
   and the worktree gitfiles, run `git worktree prune`, then commit the reorganized
   structure. No git operations were performed during the reorganization, by design.
2. **`.planning/` has duplicate `_v2` files** — `REQUIREMENTS.md`/`REQUIREMENTS_v2.md` and
   `ROADMAP.md`/`ROADMAP_v2.md`. Reconcile when convenient.
3. **`.planning/research/LITERATURE_GAPS.md` targets *Transportation Research Part D***,
   which conflicts with the *Transportation Research Part E* target in `CLAUDE.md` and `manuscript/main.tex`. This
   research note likely belongs to a different project — review and remove or re-scope.
4. **~19 MB of stale agent worktrees** live under `.claude/worktrees/` (11 "prunable"
   worktrees from earlier parallel GSD runs). Safe to remove with `git worktree prune`
   once the git repo is repaired.
