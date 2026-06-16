"""
FIG-07: Coverage--Efficiency Pareto Frontier
Single-column width (88mm / 3.46in x 2.80in), 300 dpi, TR Part A format.

Reads results/pareto_gamma_sweep.csv (produced by experiments/pareto_sweep.py).
Plots seed-averaged (served_share, vkm_per_served_trip) for each Gamma value,
labeling each point with its Gamma value.
"""
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

os.makedirs('figures', exist_ok=True)

DATA_PATH = os.path.join('results', 'pareto_gamma_sweep.csv')

# --- Load and aggregate by gamma (mean across seeds) ---
df = pd.read_csv(DATA_PATH)
agg = df.groupby('gamma', as_index=False).agg(
    served_share=('served_share', 'mean'),
    vkm_per_served_trip=('vkm_per_served_trip', 'mean'),
    social_welfare=('social_welfare', 'mean'),
).sort_values('served_share')

plt.rcParams['font.family'] = 'serif'

fig, ax = plt.subplots(figsize=(3.46, 2.80))

# Plot frontier line + markers
ax.plot(
    agg['served_share'],
    agg['vkm_per_served_trip'],
    marker='o',
    color='#1A3A6B',
    linewidth=1.5,
    markersize=5,
    zorder=3,
)

# Label each point with its Gamma value
for _, row in agg.iterrows():
    gamma_label = r'$\Gamma$=' + str(int(row['gamma']))
    offset_x = 0.008
    offset_y = 5.0
    ax.annotate(
        gamma_label,
        xy=(row['served_share'], row['vkm_per_served_trip']),
        xytext=(row['served_share'] + offset_x, row['vkm_per_served_trip'] + offset_y),
        fontsize=7,
        color='#1A3A6B',
        ha='left',
    )

ax.set_xlabel('Served share (accepted / total requests)', fontsize=9)
ax.set_ylabel('vkm per served trip (km)', fontsize=9)
ax.set_title('Coverage\u2013Efficiency Pareto Frontier (FullModel)', fontsize=9)
ax.tick_params(axis='both', labelsize=8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(alpha=0.3, linewidth=0.5)

plt.tight_layout(pad=0.5)
fig.savefig('figures/fig07_pareto.pdf', bbox_inches='tight', dpi=300)
fig.savefig('figures/fig07_pareto.png', bbox_inches='tight', dpi=300)
plt.close()
print("FIG-07 saved: figures/fig07_pareto.pdf + .png")
