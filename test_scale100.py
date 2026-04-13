"""Quick test of all variants at scale=100 after feasibility fix and alns_iterations=5."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from experiments.scenarios import generate_synthetic
from experiments.variants import ALL_VARIANTS
from experiments.metrics import compute_metrics
import time

s = generate_synthetic(100, 10, 42)
results = []
t_total_start = time.perf_counter()
for v in ALL_VARIANTS:
    t0 = time.perf_counter()
    r = v.run(s)
    m = compute_metrics(r)
    elapsed = time.perf_counter() - t0
    line = f'{v.name:<30} {elapsed:.2f}s accept={m.acceptance_rate:.3f} vkm={m.vehicle_km:.1f}'
    results.append(line)

total = time.perf_counter() - t_total_start
results.append(f'\nTotal time: {total:.1f}s')

with open('test_scale100_output.txt', 'w') as f:
    f.write('\n'.join(results) + '\n')
print('Done')
