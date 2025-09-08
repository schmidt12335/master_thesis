import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from matplotlib.gridspec import GridSpec
from IPython import embed
from cycler import cycler

def get_incidence(r_data, r2_data):
    specific = 0
    non_specific = 0
    no_fc = 0
    for i in range(len(r_data)):
        if r_data[i] > 0.1 and r2_data[i] < 0.1:
            specific += 1
        if r_data[i] > 0.1 and r2_data[i] > 0.1:
            non_specific += 1
        if -0.1 < r_data[i] < 0.1 and -0.1 < r2_data[i] < 0.1:
            no_fc += 1
    spurious_fc = len(r_data) - (specific + non_specific + no_fc)
    return np.array([specific/len(r_data)*100, non_specific/len(r_data)*100, no_fc/len(r_data)*100, spurious_fc/len(r_data)*100])

corrs_r_matlab_qc_gsr = np.load('corrs_r_matlab_qc_gsr.npy')
corrs_r2_matlab_qc_gsr = np.load('corrs_r2_matlab_qc_gsr.npy')

corrs_r_matlab_all_gsr = np.load('corrs_r_matlab_all_gsr.npy')
corrs_r2_matlab_all_gsr = np.load('corrs_r2_matlab_all_gsr.npy')

corrs_r_rabies_qc_gsr = np.load('corrs_r_rabies_qc_gsr.npy')
corrs_r2_rabies_qc_gsr = np.load('corrs_r2_rabies_qc_gsr.npy')

corrs_r_rabies_0_5_gsr = np.load('corrs_r_rabies_all_0.5_gsr.npy')
corrs_r2_rabies_0_5_gsr = np.load('corrs_r2_rabies_all_0.5_gsr.npy')

data_x = [corrs_r_matlab_qc_gsr, corrs_r_matlab_all_gsr, corrs_r_rabies_qc_gsr, corrs_r_rabies_0_5_gsr]
data_y = [corrs_r2_matlab_qc_gsr, corrs_r2_matlab_all_gsr, corrs_r2_rabies_qc_gsr, corrs_r2_rabies_0_5_gsr]

kdes_x = []
kdes_y = []

xmin = -1
xmax = 1
ymin = -1
ymax = 2
dx = 0.0005
x = np.arange(xmin, xmax, dx)
y = np.arange(ymin, ymax, dx)
incidence_all = []

for i in range(len(data_x)):
    incidence_all.append(get_incidence(data_x[i], data_y[i]))

total_incidence = np.sum(incidence_all, axis = 0)/8
fc_categories = ['Specific FC', 'Non-specific FC', 'No FC', 'Spurious FC']
print(f'total incidence = {total_incidence}', f'incidence ={incidence_all}')

labels = [f'AC QC GSR', f'AC GSR', f'AC QC Rabies', f'AC Rabies GSR']

all_fc = {}
for i in range(len(fc_categories)):
    all_fc[fc_categories[i]] = np.array([
        incidence_all[0][i],
        incidence_all[1][i],
        incidence_all[2][i],
        incidence_all[3][i]])



fig1, ax = plt.subplots()
bottom = np.zeros(len(all_fc.keys()))

for label, fc in all_fc.items():
    p = ax.bar(labels, fc, width=0.6, label=label, bottom = bottom)
    bottom += fc
ax.legend(fontsize = 8, loc = 'lower left', markerscale = 0.75, frameon = True, labelspacing = 0.2, handlelength = 0.8, borderaxespad = 2, draggable = True)
ax.set_ylabel("Incidence (%)")
ax.set_xticklabels(labels, rotation = 45, ha = 'right')
#ax.tick_params(axis = 'x', length = 0)
plt.tight_layout()
#plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/barplot gsr comp', dpi = 400)
plt.show()

for i in range(len(data_x)):
    kernel = gaussian_kde(data_x[i], bw_method = 0.6)
    gkde = kernel(x)
    kdes_x.append(gkde)

for i in range(len(data_y)):
    kernel = gaussian_kde(data_y[i], bw_method = 0.6)
    gkde = kernel(y)
    kdes_y.append(gkde)

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
orange = colors[1]
colors[0] = 'blue'
colors[1] = colors[2]
colors[2] = orange
colors[7] = 'lightskyblue'
plt.rcParams['axes.prop_cycle'] = cycler(color=colors)

fig = plt.figure(figsize = (7, 6), tight_layout = True)
gs = GridSpec(2,2, figure = fig, height_ratios= [1, 5], width_ratios = [5, 1])

ax0 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])

for i in range(len(data_x)):
    ax0.plot(x, kdes_x[i], alpha=0.5)
    ax0.fill_between(x, kdes_x[i], alpha = 0.2)

ax0.set_xlim([-0.2, 1])

for i in range(len(data_y)):
    ax3.plot(kdes_y[i], y, alpha=0.5)
    ax3.fill_between(kdes_y[i], y, alpha = 0.2)

ax2.set_ylim([-0.7, 1])
ax3.set_ylim([-0.7, 1])

for i in range(len(data_x)):
    ax2.plot(data_x[i], data_y[i], linestyle='', marker='o', label=labels[i], markersize = 4)  # , c = cmap[0])
ax2.set_xlabel('Correlation S1bf left to right (r)')
ax2.set_ylabel('Correlation S1bf left to ACA (r)')
ax2.set_xlim([-0.3, 1])
ax2.set_ylim([-0.7, 1])
ax2.legend(fontsize = 8, markerscale = 0.75, frameon = False, title = 'Dataset', title_fontsize = 9, labelspacing = 0.2, handlelength = 0, borderaxespad = 2, draggable = True)
ax2.hlines(y = 0.1, xmin=-0.1, xmax=0.8, linestyle='--', color='k')
ax2.vlines(x = 0.1, ymin=-0.4, ymax=0.8, linestyle='--', color='k')
ax2.hlines(y = -0.1, xmin=-0.1, xmax=0.1, linestyle='--', color='k')
ax2.vlines(x = -0.1, ymin=-0.1, ymax=0.1, linestyle='--', color='k')
ax2.set_xticks([-0.2, 0, 0.2, 0.4, 0.6, 0.8], labels = [-0.2, 0, 0.2, 0.4, 0.6, 0.8])
ax2.set_yticks([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], labels = [-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8])

pos = [[0.85, -0.6], [0.85, 0.2, ], [-0.18, 0.1], [-0.1, -0.6]]
for i in range(len(fc_categories)):
    if total_incidence[i] == 100 or total_incidence[i] == 0:
        ax2.text(x = pos[i][0], y = pos[i][1], s = f'{total_incidence[i]:.0f}%\n{fc_categories[i]}', ha='center', va='center')
    else:
        ax2.text(x = pos[i][0], y = pos[i][1], s = f'{total_incidence[i]:.2f}%\n{fc_categories[i]}', ha='center', va='center')


ax0.axis('off')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax3.axis('off')
plt.tight_layout()

#plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/', dpi = 400, bbox_inches='tight')


plt.show()
