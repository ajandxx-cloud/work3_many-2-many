"""
FIG-05: Sensitivity Analysis Line Plots
Two-panel figure: acceptance rate vs walking tolerance rho and vs fleet size.
Double-column width (180mm × 75mm), 300 dpi, TR Part A format.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

os.makedirs('figures', exist_ok=True)

plt.rcParams['font.family'] = 'serif'

# Load sensitivity data
walk_df  = pd.read_csv('results/sensitivity_walk.csv')
fleet_df = pd.read_csv('results/sensitivity_fleet.csv')

# Filter walk sweep to standard density tier only
walk_std  = walk_df[walk_df['density_tier'] == 'standard']
walk_full = walk_std[walk_std['variant'] == 'FullModel'].sort_values('rho')
walk_d2d  = walk_std[walk_std['variant'] == 'DoorToDoor'].sort_values('rho').drop_duplicates('rho')

fleet_full = fleet_df[fleet_df['variant'] == 'FullModel'].sort_values('n_vehicles')
fleet_d2d  = fleet_df[fleet_df['variant'] == 'DoorToDoor'].sort_values('n_vehicles')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.09, 2.95))

# --- Panel (a): Walking Tolerance Sweep ---
ax1.plot(walk_full['rho'], walk_full['acceptance_rate'],
         marker='o', color='#1A3A6B', label='FullModel', linewidth=1.5, markersize=4)
ax1.plot(walk_d2d['rho'], walk_d2d['acceptance_rate'],
         marker='s', color='#AAAAAA', linestyle='--', label='DoorToDoor',
         linewidth=1.5, markersize=4)
ax1.axvline(x=1000, color='#D65F5F', linestyle=':', linewidth=1.2,
            label=u'\u03c1=1000m threshold')
ax1.annotate('Min viable\nthreshold',
             xy=(1000, 0.05), xytext=(750, 0.15),
             fontsize=7, color='#D65F5F',
             arrowprops=dict(arrowstyle='->', color='#D65F5F', lw=0.8))
ax1.set_xlabel(u'Walking tolerance \u03c1 (m)', fontsize=9)
ax1.set_ylabel('Acceptance Rate', fontsize=9)
ax1.set_xticks([200, 400, 600, 800, 1000])
ax1.set_ylim(0, 0.7)
ax1.set_title('(a) Walking Tolerance Sweep', fontsize=9)
ax1.legend(loc='upper left', fontsize=7)
ax1.tick_params(axis='both', labelsize=8)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(alpha=0.3, linewidth=0.5)

# --- Panel (b): Fleet Size Sweep ---
ax2.plot(fleet_full['n_vehicles'], fleet_full['acceptance_rate'],
         marker='o', color='#1A3A6B', label='FullModel', linewidth=1.5, markersize=4)
ax2.plot(fleet_d2d['n_vehicles'], fleet_d2d['acceptance_rate'],
         marker='s', color='#AAAAAA', linestyle='--', label='DoorToDoor',
         linewidth=1.5, markersize=4)
ax2.axvline(x=20, color='#B47CC7', linestyle=':', linewidth=1.2,
            label='Diminishing returns (n=20)')
ax2.annotate('Diminishing\nreturns',
             xy=(20, 0.22), xytext=(22, 0.35),
             fontsize=7, color='#B47CC7',
             arrowprops=dict(arrowstyle='->', color='#B47CC7', lw=0.8))
ax2.set_xlabel('Fleet size (vehicles)', fontsize=9)
ax2.set_ylabel('Acceptance Rate', fontsize=9)
ax2.set_xticks([5, 10, 15, 20, 25, 30])
ax2.set_ylim(0, 0.9)
ax2.set_title('(b) Fleet Size Sweep', fontsize=9)
ax2.legend(loc='upper left', fontsize=7)
ax2.tick_params(axis='both', labelsize=8)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(alpha=0.3, linewidth=0.5)

plt.tight_layout(pad=0.5)
fig.savefig('figures/fig05_sensitivity.pdf', bbox_inches='tight', dpi=300)
fig.savefig('figures/fig05_sensitivity.png', bbox_inches='tight', dpi=300)
plt.close()
print("FIG-05 saved: figures/fig05_sensitivity.pdf + .png")
