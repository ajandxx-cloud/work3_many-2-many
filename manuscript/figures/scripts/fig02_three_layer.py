import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

os.makedirs('figures', exist_ok=True)

plt.rcParams['font.family'] = 'serif'

fig, ax = plt.subplots(figsize=(3.46, 4.33))  # 88mm x 110mm
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

box_color = '#4878CF'
arrow_color = '#555555'
text_color = 'white'

# Three layer boxes
layer_labels = [
    'Layer 1\nService Offer Generation\n(Candidate gen. \u2192 Insertion eval. \u2192 Bundle $b^*$)',
    'Layer 2\nPassenger Response\n(MNL choice: accept $z_r=1$ / reject $z_r=0$)',
    'Layer 3\nDynamic Dispatch\n(Rolling horizon ALNS, every $\\Delta$ min)',
]
y_tops = [11.0, 7.5, 4.0]
box_h = 2.5
box_x = 1.0
box_w = 7.5

for i, (y_top, label) in enumerate(zip(y_tops, layer_labels)):
    rect = mpatches.FancyBboxPatch((box_x, y_top - box_h), box_w, box_h,
                                    boxstyle='round,pad=0.15',
                                    facecolor=box_color, edgecolor='#222222',
                                    linewidth=1.2, alpha=0.90)
    ax.add_patch(rect)
    ax.text(box_x + box_w / 2, y_top - box_h / 2, label,
            ha='center', va='center', fontsize=6.5, color=text_color,
            multialignment='center')

# Downward arrows between boxes
# Layer 1 bottom -> Layer 2 top
ax.annotate('', xy=(5, 7.5), xytext=(5, 8.5),
            arrowprops=dict(arrowstyle='->', color=arrow_color, lw=1.5))
ax.text(5.2, 8.0, 'bundle $b^*$, decision $x_r$', fontsize=5.5, color=arrow_color)

# Layer 2 bottom -> Layer 3 top
ax.annotate('', xy=(5, 4.0), xytext=(5, 5.0),
            arrowprops=dict(arrowstyle='->', color=arrow_color, lw=1.5))
ax.text(5.2, 4.5, '$z_r$, updated routes', fontsize=5.5, color=arrow_color)

# Feedback arrow: right side from Layer 3 back up to Layer 1
# From right side of Layer 3 box up to right side of Layer 1 box
ax.annotate('', xy=(9.2, 9.75), xytext=(9.2, 2.0),
            arrowprops=dict(arrowstyle='->', color='#D65F5F', lw=1.2,
                            connectionstyle='arc3,rad=0.0'))
# Horizontal connectors
ax.plot([8.5, 9.2], [2.0, 2.0], color='#D65F5F', lw=1.2)
ax.plot([8.5, 9.2], [9.75, 9.75], color='#D65F5F', lw=1.2)
ax.text(9.3, 5.9, 'Updated\nroutes\n$\\{\\sigma_v\\}$\nfeed back\nto Layer 1',
        fontsize=5.0, color='#D65F5F', va='center')

# "Request r arrives" label pointing into Layer 1
ax.annotate('Request $r$ arrives', xy=(box_x, 9.75), xytext=(-0.1, 9.75),
            fontsize=6.0, color='#333333', va='center',
            arrowprops=dict(arrowstyle='->', color='#333333', lw=1.0))

plt.tight_layout(pad=0.3)
fig.savefig('figures/fig02_three_layer.pdf', bbox_inches='tight', dpi=300)
fig.savefig('figures/fig02_three_layer.png', bbox_inches='tight', dpi=300)
plt.close()
print("FIG-02 saved")
