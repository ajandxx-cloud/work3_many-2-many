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
RHO_P = 500.0                      # pickup walking radius
RHO_D = 500.0                      # dropoff walking radius

# Rolling-horizon parameters (seconds)
H_WINDOW = 30 * 60.0               # rolling horizon window
DELTA = 5 * 60.0                   # time step between decisions

# MNL attribute weights [walk, wait, ivt, price, opting-out penalty]
ALPHA_WEIGHTS = [1.0, 1.0, 1.0, 1.0, 5.0]

# Vehicle parameters
VEHICLE_CAPACITY = 8
MAX_RIDE_TIME = 45 * 60.0          # 45 min max in-vehicle time
MAX_ROUTE_DURATION = 8 * 3600.0    # 8 h max route duration

# Beijing semi-realistic scenario (fixed scale used for semi-realistic runs)
BEIJING_SCALE = 200
