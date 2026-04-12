"""
FIG-06: Policy deployment map — demand density × walking tolerance
Three-tier DRT deployment framework for Chinese cities.
Run from project root: python figures/scripts/fig06_policy_map.py
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9

fig, ax = plt.subplots(figsize=(3.46, 3.46), dpi=300)

# Axis ranges
rho_min, rho_max = 200, 1200   # walking tolerance (m), x-axis
demand_min, demand_max = 0, 500  # requests/day, y-axis

# Draw three colored zones using filled rectangles:
# Tier 3 (door-to-door): demand < 100 — entire x range
ax.fill_between([rho_min, rho_max], [0, 0], [100, 100],
                color='#D65F5F', alpha=0.25, label='Tier 3: Door-to-door (<100 req/day)')

# Tier 2 (single-sided): demand 100–300 — entire x range
ax.fill_between([rho_min, rho_max], [100, 100], [300, 300],
                color='#F0A500', alpha=0.25, label='Tier 2: Single-sided (100–300 req/day)')

# Tier 1 (bidirectional): demand > 300, rho >= 1000 — only viable above rho threshold
# Split Tier 1 into viable (rho>=1000) and non-viable (rho<1000) sub-zones
ax.fill_between([rho_min, 1000], [300, 300], [demand_max, demand_max],
                color='#F0A500', alpha=0.25)  # same as Tier 2 color — not viable for bidir
ax.fill_between([1000, rho_max], [300, 300], [demand_max, demand_max],
                color='#4878CF', alpha=0.35, label='Tier 1: Bidirectional (>300 req/day, ρ≥1000m)')

# Vertical dashed line at rho=1000m (minimum viable threshold)
ax.axvline(x=1000, color='#1A3A6B', linestyle='--', linewidth=1.2, label='ρ=1000m threshold')

# Horizontal dashed lines at demand=100 and demand=300
ax.axhline(y=100, color='#555555', linestyle=':', linewidth=0.8)
ax.axhline(y=300, color='#555555', linestyle=':', linewidth=0.8)

# Zone text labels (centered in each zone)
ax.text(700, 50, 'Tier 3\nDoor-to-door', ha='center', va='center',
        fontsize=7, fontweight='bold', color='#8B0000')
ax.text(700, 200, 'Tier 2\nSingle-sided', ha='center', va='center',
        fontsize=7, fontweight='bold', color='#7A5000')
ax.text(1100, 400, 'Tier 1\nBidirectional', ha='center', va='center',
        fontsize=7, fontweight='bold', color='#1A3A6B')
ax.text(600, 400, 'Tier 1*\n(ρ too low)', ha='center', va='center',
        fontsize=6, color='#7A5000', style='italic')

# Axis formatting
ax.set_xlim(rho_min, rho_max)
ax.set_ylim(demand_min, demand_max)
ax.set_xlabel('Walking tolerance ρ (m)', fontsize=9)
ax.set_ylabel('Demand density (requests/day)', fontsize=9)
ax.tick_params(axis='both', labelsize=8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Legend (compact, inside upper-left)
handles = [
    mpatches.Patch(color='#4878CF', alpha=0.35, label='Tier 1: Bidirectional'),
    mpatches.Patch(color='#F0A500', alpha=0.25, label='Tier 2: Single-sided'),
    mpatches.Patch(color='#D65F5F', alpha=0.25, label='Tier 3: Door-to-door'),
    plt.Line2D([0], [0], color='#1A3A6B', linestyle='--', linewidth=1.2, label='ρ=1000m threshold'),
]
ax.legend(handles=handles, loc='upper left', fontsize=6, framealpha=0.8)

plt.tight_layout(pad=0.3)
fig.savefig('figures/fig06_policy_map.pdf', bbox_inches='tight', dpi=300)
fig.savefig('figures/fig06_policy_map.png', bbox_inches='tight', dpi=300)
plt.close()
print('FIG-06 saved.')
