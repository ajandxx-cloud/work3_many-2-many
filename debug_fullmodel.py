"""Debug FullModel acceptance at scale=20."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from experiments.scenarios import generate_synthetic
from experiments.variants import FullModel
from experiments.metrics import compute_metrics
from src.drt.alns import RollingHorizon
from experiments.config import RHO_P, RHO_D, K_TOP, H_WINDOW, DELTA, ALPHA_WEIGHTS

s = generate_synthetic(20, 2, 42)
print(f'Requests: {len(s.requests)}, Vehicles: {len(s.vehicles)}, MPs: {len(s.meeting_points)}')
print(f'Request earliest range: {min(r.earliest for r in s.requests):.0f} - {max(r.earliest for r in s.requests):.0f}')
print(f'Request window sizes: {[(r.latest-r.earliest)/60 for r in s.requests[:5]]} min')
print(f'Vehicle current_times: {[v.current_time for v in s.vehicles]}')
print()

# Check candidates for first few requests
from src.drt.candidate import generate_candidates
for req in s.requests[:3]:
    pu_cands = generate_candidates(req, s.meeting_points, RHO_P, K_TOP, 'pickup')
    do_cands = generate_candidates(req, s.meeting_points, RHO_D, K_TOP, 'dropoff')
    print(f'req {req.id}: earliest={req.earliest:.0f} latest={req.latest:.0f} '
          f'pu_cands={len(pu_cands)} do_cands={len(do_cands)}')

print()
# Run FullModel with verbose
v = FullModel()
r = v.run(s)
m = compute_metrics(r)
print(f'FullModel: accept={m.acceptance_rate:.3f} ({sum(1 for rec in r.records if rec.accepted)}/{len(r.records)})')
print(f'Accepted requests:')
for rec in r.records:
    if rec.accepted:
        print(f'  {rec.request_id}: wait={rec.wait_time:.0f}s walk={rec.pickup_walk:.0f}m')
