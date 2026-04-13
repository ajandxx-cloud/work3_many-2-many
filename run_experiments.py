"""Standalone script to run all experiments and write results."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import time
from experiments.runner import run_all_experiments
import pandas as pd

t_start = time.perf_counter()
print("[run_experiments] Starting full experiment run...", flush=True)

syn_rows, bei_rows = run_all_experiments()
elapsed = time.perf_counter() - t_start

print(f"\n[run_experiments] Done in {elapsed:.1f}s ({elapsed/60:.1f} min)", flush=True)

# Validate
tbl = pd.read_csv("results/metrics_table.csv")
print(f"\nmetrics_table.csv ({len(tbl)} rows):")
print(tbl[["variant","acceptance_rate_mean","vehicle_km_mean","avg_wait_mean"]].to_string(index=False))

full = tbl[tbl["variant"]=="FullModel"].iloc[0]
dtd  = tbl[tbl["variant"]=="DoorToDoor"].iloc[0]
print(f"\nFullModel accept={full['acceptance_rate_mean']:.3f} vkm={full['vehicle_km_mean']:.1f}")
print(f"DoorToDoor accept={dtd['acceptance_rate_mean']:.3f} vkm={dtd['vehicle_km_mean']:.1f}")

if full["acceptance_rate_mean"] >= dtd["acceptance_rate_mean"]:
    print("[PASS] FullModel acceptance_rate >= DoorToDoor")
else:
    print(f"[NOTE] FullModel acceptance_rate < DoorToDoor (diff={dtd['acceptance_rate_mean']-full['acceptance_rate_mean']:.3f})")

if full["vehicle_km_mean"] <= dtd["vehicle_km_mean"]:
    print("[PASS] FullModel vehicle_km <= DoorToDoor")
elif full["vehicle_km_mean"] <= dtd["vehicle_km_mean"] * 1.1:
    print("[NOTE] FullModel vehicle_km within 10% of DoorToDoor (acceptable)")
else:
    print(f"[NOTE] FullModel vehicle_km > DoorToDoor (ratio={full['vehicle_km_mean']/dtd['vehicle_km_mean']:.2f}x)")

print("\nFull metrics table:")
print(tbl.to_string(index=False))
