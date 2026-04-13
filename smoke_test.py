"""Smoke test: run_all_experiments at scale=20."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tempfile, time
from experiments.runner import run_all_experiments
import pandas as pd

tmp = tempfile.mkdtemp()
t0 = time.perf_counter()
syn, bei = run_all_experiments(scales=[20], seeds=[42], beijing=True, results_dir=tmp)
elapsed = time.perf_counter() - t0

tbl = pd.read_csv(os.path.join(tmp, 'metrics_table.csv'))

lines = [
    f'syn rows: {len(syn)}, bei rows: {len(bei)}',
    f'metrics_table rows: {len(tbl)}',
    f'NaN count: {tbl.isnull().sum().sum()}',
    f'elapsed: {elapsed:.1f}s',
    '',
]
lines.append(tbl[['variant','acceptance_rate_mean','vehicle_km_mean']].to_string(index=False))
lines.append('')
lines.append('PASSED' if len(tbl)==6 and tbl.isnull().sum().sum()==0 else 'FAILED')

with open('smoke_test_output.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')
