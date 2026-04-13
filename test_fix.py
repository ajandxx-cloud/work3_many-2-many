"""Test FullModel at scale=20 after vehicle current_time fix."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from experiments.scenarios import generate_synthetic
from experiments.variants import ALL_VARIANTS
from experiments.metrics import compute_metrics

s = generate_synthetic(20, 2, 42)
lines = []
t_all = time.perf_counter()
for v in ALL_VARIANTS:
    t0 = time.perf_counter()
    r = v.run(s)
    m = compute_metrics(r)
    elapsed = time.perf_counter() - t0
    line = f'{v.name:<30} {elapsed:.2f}s accept={m.acceptance_rate:.3f} vkm={m.vehicle_km:.1f}'
    lines.append(line)

lines.append(f'Total: {time.perf_counter()-t_all:.1f}s')
output = '\n'.join(lines)
with open('test_fix_output.txt', 'w') as f:
    f.write(output + '\n')
