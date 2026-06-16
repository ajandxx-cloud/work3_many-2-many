import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

os.makedirs('figures', exist_ok=True)

plt.rcParams['font.family'] = 'serif'

fig, ax = plt.subplots(figsize=(3.46, 6.30))  # 88mm x 160mm
ax.set_xlim(0, 10)
ax.set_ylim(0, 18)
ax.axis('off')

proc_color = '#4878CF'
dec_color = '#D65F5F'
end_color = '#6ACC65'
arrow_color = '#333333'


def draw_box(ax, cx, cy, w, h, text, color=proc_color, fontsize=6.2):
    rect = mpatches.FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                    boxstyle='round,pad=0.12',
                                    facecolor=color, edgecolor='#222222',
                                    linewidth=1.0, zorder=3)
    ax.add_patch(rect)
    ax.text(cx, cy, text, ha='center', va='center', fontsize=fontsize,
            color='white', multialignment='center', zorder=4)


def draw_diamond(ax, cx, cy, w, h, text, color=dec_color, fontsize=5.8):
    diamond = plt.Polygon(
        [[cx, cy + h / 2], [cx + w / 2, cy], [cx, cy - h / 2], [cx - w / 2, cy]],
        facecolor=color, edgecolor='#222222', linewidth=1.0, zorder=3)
    ax.add_patch(diamond)
    ax.text(cx, cy, text, ha='center', va='center', fontsize=fontsize,
            color='white', multialignment='center', zorder=4)


def arrow(ax, x1, y1, x2, y2, label='', label_dx=0.2, label_dy=0.0):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=arrow_color, lw=1.2))
    if label:
        mx = (x1 + x2) / 2 + label_dx
        my = (y1 + y2) / 2 + label_dy
        ax.text(mx, my, label, fontsize=5.2, color='#555555', va='center')


# Node positions (top to bottom)
cx = 5.0
nodes = {
    'start':    (cx, 17.2),
    'gen_mp':   (cx, 15.6),
    'enum_b':   (cx, 13.9),
    'feas':     (cx, 12.2),
    'reject1':  (8.5, 12.2),
    'best_b':   (cx, 10.5),
    'mnl_prob': (cx, 9.0),
    'accept':   (cx, 7.4),
    'discard':  (8.5, 7.4),
    'insert':   (cx, 5.8),
    'trigger':  (cx, 4.2),
    'alns':     (cx, 2.7),
    'end':      (cx, 1.2),
}

# Draw nodes
draw_box(ax, *nodes['start'], 5.5, 0.8, 'Request $r$ arrives', end_color)
draw_box(ax, *nodes['gen_mp'], 6.5, 0.9,
         'Generate candidates\n$M_r^P$, $M_r^D$ (walking radius $\\rho$ filter)')
draw_box(ax, *nodes['enum_b'], 6.5, 0.9,
         r'Enumerate bundles $(m^P, m^D)$' + '\n' + r'for each vehicle $v$, positions $(\pi^P, \pi^D)$')
draw_diamond(ax, *nodes['feas'], 4.5, 1.1, 'Feasible insertion\nexists?')
draw_box(ax, *nodes['reject1'], 2.8, 0.7, 'Reject request\n$(z_r=0)$', dec_color)
draw_box(ax, *nodes['best_b'], 6.5, 0.9,
         'Select best bundle $b^*$\n(min incremental cost $\\Delta C$)')
draw_box(ax, *nodes['mnl_prob'], 6.5, 0.9,
         'Compute MNL probability\n$P_{rb^*}^k$ (Eq. choice-prob)')
draw_diamond(ax, *nodes['accept'], 4.5, 1.1,
             'Passenger accepts?\n(Bernoulli sample $z_r$)')
draw_box(ax, *nodes['discard'], 2.8, 0.7,
         'Discard $x_r$\nroutes unchanged', dec_color)
draw_box(ax, *nodes['insert'], 6.5, 0.9,
         'Insert $m_r^P$ at $\\pi_r^P$,\n$m_r^D$ at $\\pi_r^D$ in route $\\sigma_{v_r}$')
draw_diamond(ax, *nodes['trigger'], 4.5, 1.1,
             'Rolling horizon\ntrigger? (t mod \u0394 = 0)')
draw_box(ax, *nodes['alns'], 6.5, 0.9,
         'ALNS re-opt on\n$R^{act}(t_{now})$ over $[t, t+H]$')
draw_box(ax, *nodes['end'], 5.5, 0.8, 'Dispatch updated routes', end_color)

# Arrows (main flow)
arrow(ax, cx, 16.8, cx, 16.05)
arrow(ax, cx, 15.15, cx, 14.35)
arrow(ax, cx, 13.45, cx, 12.75)
arrow(ax, cx, 11.65, cx, 10.95)
arrow(ax, cx, 10.05, cx, 9.45)
arrow(ax, cx, 8.55, cx, 7.95)
arrow(ax, cx, 6.95, cx, 6.25)
arrow(ax, cx, 5.35, cx, 4.75)
arrow(ax, cx, 3.65, cx, 3.15)
arrow(ax, cx, 2.25, cx, 1.6)

# No branch from Feasible -> Reject
arrow(ax, cx + 2.25, 12.2, 7.2, 12.2)
ax.text(cx + 2.35, 12.45, 'No', fontsize=5.5, color='#555555')
ax.text(cx + 0.15, 11.65, 'Yes', fontsize=5.5, color='#555555')

# No branch from Accept -> Discard
arrow(ax, cx + 2.25, 7.4, 7.2, 7.4)
ax.text(cx + 2.35, 7.65, 'No', fontsize=5.5, color='#555555')
ax.text(cx + 0.15, 8.55, 'Yes', fontsize=5.5, color='#555555')

# No branch from trigger -> end (horizontal then down)
ax.annotate('', xy=(8.5, 1.2), xytext=(8.5, 4.2),
            arrowprops=dict(arrowstyle='->', color=arrow_color, lw=1.2))
ax.plot([cx + 2.25, 8.5], [4.2, 4.2], color=arrow_color, lw=1.2)
ax.annotate('', xy=(cx + 2.75, 1.2), xytext=(8.5, 1.2),
            arrowprops=dict(arrowstyle='->', color=arrow_color, lw=1.2))
ax.text(cx + 2.35, 4.45, 'No', fontsize=5.5, color='#555555')
ax.text(cx + 0.15, 3.65, 'Yes', fontsize=5.5, color='#555555')

plt.tight_layout(pad=0.3)
fig.savefig('figures/fig03_algorithm.pdf', bbox_inches='tight', dpi=300)
fig.savefig('figures/fig03_algorithm.png', bbox_inches='tight', dpi=300)
plt.close()
print("FIG-03 saved")
