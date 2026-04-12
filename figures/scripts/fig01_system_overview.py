import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

os.makedirs('figures', exist_ok=True)
os.makedirs('figures/scripts', exist_ok=True)

plt.rcParams['font.family'] = 'serif'

fig, ax = plt.subplots(figsize=(3.46, 3.46))  # 88mm x 88mm
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-0.5, 4.5)
ax.axis('off')

# 3x3 meeting point grid at (i*1.5, j*1.5) for i,j in 0..2
mp_color = '#4878CF'
for i in range(3):
    for j in range(3):
        ax.plot(i * 1.5, j * 1.5, 'o', color=mp_color, markersize=9, zorder=3)

ax.text(1.5, 3.5, 'Meeting Point Grid $M$', ha='center', va='bottom', fontsize=7, color=mp_color)

# Passenger origins (green squares)
o1 = (0.3, 0.3)
o2 = (3.5, 3.8)
ax.plot(*o1, 's', color='#6ACC65', markersize=9, zorder=4)
ax.plot(*o2, 's', color='#6ACC65', markersize=9, zorder=4)
ax.text(o1[0] - 0.15, o1[1] - 0.25, r'$o_1$', fontsize=7, ha='center', color='#6ACC65')
ax.text(o2[0] + 0.15, o2[1] + 0.15, r'$o_2$', fontsize=7, ha='center', color='#6ACC65')

# Passenger destinations (red squares)
d1 = (3.8, 0.5)
d2 = (0.5, 3.5)
ax.plot(*d1, 's', color='#D65F5F', markersize=9, zorder=4)
ax.plot(*d2, 's', color='#D65F5F', markersize=9, zorder=4)
ax.text(d1[0] + 0.15, d1[1] - 0.25, r'$\delta_1$', fontsize=7, ha='center', color='#D65F5F')
ax.text(d2[0] - 0.25, d2[1] + 0.15, r'$\delta_2$', fontsize=7, ha='center', color='#D65F5F')

# Passenger 1: o1 -> pickup MP (0,0) -> dropoff MP (3,0) -> d1
p1_pickup = (0.0, 0.0)
p1_dropoff = (3.0, 0.0)
walk_style = dict(arrowstyle='->', color='#C4AD66', lw=1.2,
                  linestyle='dashed', connectionstyle='arc3,rad=0.0')
ax.annotate('', xy=p1_pickup, xytext=o1,
            arrowprops=dict(arrowstyle='->', color='#C4AD66', lw=1.2,
                            linestyle='dashed'))
ax.annotate('', xy=d1, xytext=p1_dropoff,
            arrowprops=dict(arrowstyle='->', color='#C4AD66', lw=1.2,
                            linestyle='dashed'))

# Passenger 2: o2 -> pickup MP (3,3) -> dropoff MP (0,3) -> d2
p2_pickup = (3.0, 3.0)
p2_dropoff = (0.0, 3.0)
ax.annotate('', xy=p2_pickup, xytext=o2,
            arrowprops=dict(arrowstyle='->', color='#C4AD66', lw=1.2,
                            linestyle='dashed'))
ax.annotate('', xy=d2, xytext=p2_dropoff,
            arrowprops=dict(arrowstyle='->', color='#C4AD66', lw=1.2,
                            linestyle='dashed'))

# Vehicle route: (0,0) -> (1.5,0) -> (3,0) for passenger 1
veh_color = '#B47CC7'
ax.annotate('', xy=(1.5, 0.0), xytext=(0.0, 0.0),
            arrowprops=dict(arrowstyle='->', color=veh_color, lw=2.0))
ax.annotate('', xy=(3.0, 0.0), xytext=(1.5, 0.0),
            arrowprops=dict(arrowstyle='->', color=veh_color, lw=2.0))
# Vehicle route for passenger 2: (3,3) -> (1.5,3) -> (0,3)
ax.annotate('', xy=(1.5, 3.0), xytext=(3.0, 3.0),
            arrowprops=dict(arrowstyle='->', color=veh_color, lw=2.0))
ax.annotate('', xy=(0.0, 3.0), xytext=(1.5, 3.0),
            arrowprops=dict(arrowstyle='->', color=veh_color, lw=2.0))

# Small vehicle icon at midpoint of route 1
veh_rect = mpatches.FancyBboxPatch((1.3, -0.15), 0.4, 0.3,
                                    boxstyle='round,pad=0.02',
                                    facecolor=veh_color, edgecolor='#333333', lw=0.8, zorder=5)
ax.add_patch(veh_rect)

# Annotations for M_r^P and M_r^D
ax.annotate(r'$M_r^P$', xy=p1_pickup, xytext=(-0.4, 0.5), fontsize=7,
            color=mp_color,
            arrowprops=dict(arrowstyle='->', color=mp_color, lw=0.8))
ax.annotate(r'$M_r^D$', xy=p1_dropoff, xytext=(3.4, 0.5), fontsize=7,
            color=mp_color,
            arrowprops=dict(arrowstyle='->', color=mp_color, lw=0.8))

# Legend
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=mp_color,
               markersize=7, label='Meeting point'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='#6ACC65',
               markersize=7, label='Origin'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='#D65F5F',
               markersize=7, label='Destination'),
    plt.Line2D([0], [0], color=veh_color, lw=2, label='Vehicle route'),
    plt.Line2D([0], [0], color='#C4AD66', lw=1.2, linestyle='--', label='Walking leg'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=5.5,
          ncol=1, framealpha=0.8, edgecolor='#cccccc')

plt.tight_layout(pad=0.3)
fig.savefig('figures/fig01_system_overview.pdf', bbox_inches='tight', dpi=300)
fig.savefig('figures/fig01_system_overview.png', bbox_inches='tight', dpi=300)
plt.close()
print("FIG-01 saved")
