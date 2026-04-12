"""
FIG-04: Baseline Comparison Bar Charts
Two-panel bar chart: acceptance rate and vehicle-km across 6 model variants.
Double-column width (180mm × 80mm), 300 dpi, TR Part A format.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
import os

os.makedirs('figures', exist_ok=True)
os.makedirs('figures/scripts', exist_ok=True)

plt.rcParams['font.family'] = 'serif'

# Load data from CSV
df = pd.read_csv('results/metrics_table.csv')
df_idx = df.set_index('variant')

order = ['DoorToDoor', 'SingleSidedPickup', 'BidirectionalNoChoice',
         'FullModel', 'AblationNoChoice', 'AblationNoRollingHorizon']
short_labels = ['D2D', 'Single\nPickup', 'Bidir\nNoChoice',
                'FullModel', 'Ablation\nNoChoice', 'Ablation\nNoRH']

colors = {
    'DoorToDoor': '#AAAAAA',
    'SingleSidedPickup': '#78A8D1',
    'BidirectionalNoChoice': '#4878CF',
    'FullModel': '#1A3A6B',
    'AblationNoChoice': '#B47CC7',
    'AblationNoRollingHorizon': '#D65F5F',
}

accept_vals = df_idx.loc[order, 'acceptance_rate_mean'].values
accept_errs = df_idx.loc[order, 'acceptance_rate_std'].values
vkm_vals    = df_idx.loc[order, 'vehicle_km_mean'].values
vkm_errs    = df_idx.loc[order, 'vehicle_km_std'].values

x = np.arange(len(order))
width = 0.6
bar_colors = [colors[v] for v in order]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.09, 3.15))

# --- Panel (a): Acceptance Rate ---
bars1 = ax1.bar(x, accept_vals, width, color=bar_colors,
                edgecolor='#333333', linewidth=0.8)
ax1.errorbar(x, accept_vals, yerr=accept_errs, fmt='none',
             capsize=3, ecolor='#333333', elinewidth=0.8)
d2d_accept = df_idx.loc['DoorToDoor', 'acceptance_rate_mean']
ax1.axhline(y=d2d_accept, color='#AAAAAA', linestyle='--', linewidth=1.0,
            alpha=0.7, label='D2D baseline')
ax1.set_xticks(x)
ax1.set_xticklabels(short_labels, fontsize=8, rotation=0)
ax1.set_ylabel('Acceptance Rate', fontsize=9)
ax1.set_ylim(0, 0.75)
ax1.set_title('(a) Acceptance Rate', fontsize=9)
ax1.tick_params(axis='both', labelsize=8)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(axis='y', alpha=0.3, linewidth=0.5)

# --- Panel (b): Vehicle-km ---
bars2 = ax2.bar(x, vkm_vals, width, color=bar_colors,
                edgecolor='#333333', linewidth=0.8)
ax2.errorbar(x, vkm_vals, yerr=vkm_errs, fmt='none',
             capsize=3, ecolor='#333333', elinewidth=0.8)
d2d_vkm = df_idx.loc['DoorToDoor', 'vehicle_km_mean']
ax2.axhline(y=d2d_vkm, color='#AAAAAA', linestyle='--', linewidth=1.0,
            alpha=0.7, label='D2D baseline')

# Annotate −34.9% efficiency gain on FullModel bar
fm_idx = order.index('FullModel')
fm_vkm = df_idx.loc['FullModel', 'vehicle_km_mean']
ax2.annotate(u'\u221234.9%\nvkm/acceptance\nvs D2D',
             xy=(fm_idx, fm_vkm + vkm_errs[fm_idx]),
             xytext=(fm_idx + 1.1, fm_vkm + 900),
             fontsize=7, color='#1A3A6B',
             arrowprops=dict(arrowstyle='->', color='black', lw=0.8))

ax2.set_xticks(x)
ax2.set_xticklabels(short_labels, fontsize=8, rotation=0)
ax2.set_ylabel('Vehicle-km (vkm)', fontsize=9)
ax2.set_ylim(0, 3200)
ax2.set_title('(b) Vehicle-km', fontsize=9)
ax2.tick_params(axis='both', labelsize=8)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(axis='y', alpha=0.3, linewidth=0.5)

plt.tight_layout(pad=0.5)
fig.savefig('figures/fig04_baseline_comparison.pdf', bbox_inches='tight', dpi=300)
fig.savefig('figures/fig04_baseline_comparison.png', bbox_inches='tight', dpi=300)
plt.close()
print("FIG-04 saved: figures/fig04_baseline_comparison.pdf + .png")
