"""
experiments/config.py — Shared experiment constants and parameter grid.

All numerical experiments import these constants to ensure consistency
across config, scenarios, variants, and runner modules.
"""

# Reproducibility
RANDOM_SEED = 42
SEEDS = [42, 43, 44]

# Demand / vehicle scale grid
SCALES = [100, 200, 300, 500]                          # REQUEST_SCALES
VEHICLE_COUNTS = {100: 10, 200: 15, 300: 20, 500: 30}  # maps n_requests → n_vehicles

# Candidate meeting point filter
K_TOP = 3                          # top-K meeting points per origin/destination

# Walking radii (meters)
# Synthetic grid: 10x10 at 2km spacing → max dist to nearest MP = 1414m
# Beijing grid:   9x9 at 1875m spacing → max dist to nearest MP = 1326m
# RHO = 1500m ensures every request can reach at least one meeting point.
RHO_P = 1500.0                     # pickup walking radius
RHO_D = 1500.0                     # dropoff walking radius

# Rolling-horizon parameters (seconds)
H_WINDOW = 30 * 60.0               # rolling horizon window
DELTA = 5 * 60.0                   # time step between decisions

# ALNS iterations per re-optimization trigger
ALNS_ITERATIONS = 50

# Binary logit cost weights [alpha_op, alpha_wait, alpha_walk, alpha_ivt]
# NOTE: alpha_weights[4] (rejection penalty Gamma) is NOT used in routing.
# It is used only for post-hoc social welfare computation (metrics.py).
ALPHA_WEIGHTS = [1.0, 1.0, 1.0, 1.0, 5.0]

# Phase 3 passenger choice parameters.
# Values are inherited/simulation-range inputs documented in
# .planning/phases/03-passenger-choice-model-rebuild/03_PARAMETER_CALIBRATION.md;
# they are not real-data calibration.
CHOICE_SERVICE_ASC = 0.0
CHOICE_OUTSIDE_OPTION_CONSTANT = 0.0
CHOICE_SEED = RANDOM_SEED
CHOICE_TYPE_SHARES = {
    "price_sensitive": 0.34,
    "time_sensitive": 0.33,
    "walk_sensitive": 0.33,
}

# Vehicle parameters
VEHICLE_CAPACITY = 8
MAX_RIDE_TIME = 45 * 60.0          # 45 min max in-vehicle time
MAX_ROUTE_DURATION = 8 * 3600.0    # 8 h max route duration

# Beijing semi-realistic scenario (fixed scale used for semi-realistic runs)
BEIJING_SCALE = 200
