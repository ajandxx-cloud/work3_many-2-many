"""Debug RollingHorizon windows."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from experiments.scenarios import generate_synthetic
from src.drt.alns import RollingHorizon, _get_assigned_ids, ALNSState
from src.drt.types import Route, Vehicle
from experiments.config import RHO_P, RHO_D, K_TOP, H_WINDOW, DELTA, ALPHA_WEIGHTS
from copy import deepcopy

s = generate_synthetic(20, 2, 42)
vehicles_dict = {v.id: v for v in s.vehicles}
_COST_WEIGHTS = tuple(ALPHA_WEIGHTS[:4])
TRAVEL_SPEED = 8.33

rh = RollingHorizon(
    vehicles=vehicles_dict,
    meeting_points=s.meeting_points,
    rho_p=RHO_P, rho_d=RHO_D, k_top=K_TOP,
    H=H_WINDOW, delta=DELTA,
    cost_weights=_COST_WEIGHTS,
    travel_speed=TRAVEL_SPEED,
    alns_iterations=5, seed=42,
)

sorted_requests = sorted(s.requests, key=lambda r: r.earliest)
arrival_times = [r.earliest for r in sorted_requests]

# Monkey-patch reoptimize to add logging
original_reoptimize = rh.reoptimize
reopt_count = [0]

def logged_reoptimize(current_time):
    reopt_count[0] += 1
    n_active = len(rh.active_requests)
    result = original_reoptimize(current_time)
    n_accepted = result['n_accepted']
    if n_active > 0 or n_accepted > 0:
        print(f'  reopt #{reopt_count[0]:3d} t={current_time:.0f}: active={n_active} accepted={n_accepted}')
    return result

rh.reoptimize = logged_reoptimize

print(f'Running simulation with {len(sorted_requests)} requests...')
rh.run_simulation(sorted_requests, arrival_times)

total_assigned = len(_get_assigned_ids(ALNSState(routes=rh.routes, unassigned=[], cost=0.0)))
print(f'\nTotal assigned in routes: {total_assigned}')
print(f'Total reoptimizations: {reopt_count[0]}')
