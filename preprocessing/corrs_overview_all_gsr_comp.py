import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from matplotlib.gridspec import GridSpec
from IPython import embed
from cycler import cycler
import seaborn as sns
from scipy.stats import fisher_exact


r_threshold = 0.07

def get_incidence(r_data, r2_data):
    specific = 0
    non_specific = 0
    no_fc = 0
    for i in range(len(r_data)):
        if r_data[i] > r_threshold and r2_data[i] < r_threshold:
            specific += 1
        if r_data[i] > r_threshold and r2_data[i] > r_threshold:
            non_specific += 1
        if -0.1 < r_data[i] < r_threshold and -r_threshold < r2_data[i] < r_threshold:
            no_fc += 1
    spurious_fc = len(r_data) - (specific + non_specific + no_fc)
    return np.array([specific/len(r_data)*100, non_specific/len(r_data)*100, no_fc/len(r_data)*100, spurious_fc/len(r_data)*100])

def get_incidence_bar(r_data, r2_data):
    specific = 0
    non_specific = 0
    no_fc = 0
    for i in range(len(r_data)):
        if r_data[i] > r_threshold and r2_data[i] < r_threshold:
            specific += 1
        if r_data[i] > r_threshold and r2_data[i] > r_threshold:
            non_specific += 1
        if -0.1 < r_data[i] < r_threshold and -r_threshold < r2_data[i] < r_threshold:
            no_fc += 1
    spurious_fc = len(r_data) - (specific + non_specific + no_fc)
    return np.array([specific/len(r_data)*100, spurious_fc/len(r_data)*100, non_specific/len(r_data)*100, no_fc/len(r_data)*100])

corrs_r_matlab_all = np.load('corrs_r_matlab_all.npy')
corrs_r2_matlab_all = np.load('corrs_r2_matlab_all.npy')

corrs_r_matlab_qc_gsr = np.load('corrs_r_matlab_qc_gsr.npy')
corrs_r2_matlab_qc_gsr = np.load('corrs_r2_matlab_qc_gsr.npy')

corrs_r_rabies_qc = np.load('corrs_r_rabies_QC_0.5_NEW.npy')
corrs_r2_rabies_qc = np.load('corrs_r2_rabies_QC_0.5_NEW.npy')

corrs_r_rabies_qc_gsr = np.load('corrs_r_rabies_qc_gsr.npy')
corrs_r2_rabies_qc_gsr = np.load('corrs_r2_rabies_qc_gsr.npy')

corrs_r_mdma_all = np.load('corrs_r_mdma_all.npy')
corrs_r2_mdma_all = np.load('corrs_r2_mdma_all.npy')

corrs_r_mdma_all_gsr = np.load('corrs_r_mdma_all_gsr_NEW.npy')
corrs_r2_mdma_all_gsr = np.load('corrs_r2_mdma_all_gsr_NEW.npy')

corrs_r_marciano = np.load('corrs_r_marciano_smoothed.npy')
corrs_r2_marciano = np.load('corrs_r2_marciano_smoothed.npy')

corrs_r_marciano_gsr = np.load('corrs_r_marciano_smoothed_gsr_2500_NEW.npy')
corrs_r2_marciano_gsr = np.load('corrs_r2_marciano_smoothed_gsr_2500_NEW.npy')


data_x = [corrs_r_matlab_all, corrs_r_rabies_qc, corrs_r_mdma_all, corrs_r_marciano, corrs_r_matlab_qc_gsr, corrs_r_rabies_qc_gsr, corrs_r_mdma_all_gsr, corrs_r_marciano_gsr]
data_y = [corrs_r2_matlab_all, corrs_r2_rabies_qc, corrs_r2_mdma_all, corrs_r2_marciano, corrs_r2_matlab_qc_gsr, corrs_r2_rabies_qc_gsr, corrs_r2_mdma_all_gsr, corrs_r2_marciano_gsr]

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

labels = [f'AC MATLAB', f'AC RABIES', f'Iso MATLAB', f'Med MATLAB', 'AC MATLAB GSR', f'AC RABIES GSR', f'Iso GSR MATLAB', f'Med GSR MATLAB']

all_fc = {}
for i in range(len(fc_categories)):
    all_fc[fc_categories[i]] = np.array([
        incidence_all[0][i],
        incidence_all[1][i],
        incidence_all[2][i],
        incidence_all[3][i],
        incidence_all[4][i],
        incidence_all[5][i],
        incidence_all[6][i],
        incidence_all[7][i]])

fc_categories_short = ['Specific', 'Spurious', 'Non-specific', 'No FC']

incidence_all_short = []

for i in range(len(data_x)):
    incidence_all_short.append(get_incidence_bar(data_x[i], data_y[i]))

all_fc_short = {}
for i in range(len(fc_categories_short)):
    all_fc_short[fc_categories_short[i]] = np.array([
        incidence_all_short[0][i],
        incidence_all_short[1][i],
        incidence_all_short[2][i],
        incidence_all_short[3][i],
        incidence_all_short[4][i],
        incidence_all_short[5][i],
        incidence_all_short[6][i],
        incidence_all_short[7][i]])

og_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

CB_cmap = ['#377eb8', '#4daf4a', '#ff7f00',
                  '#f781bf', '#a65628', '#984ea3',
                  '#999999', '#e41a1c', '#dede00']
plt.rcParams['axes.prop_cycle'] = cycler(color=CB_cmap)

colors = sns.color_palette("colorblind", 4)
plt.rcParams['axes.prop_cycle'] = cycler(color=colors)

fig1, ax = plt.subplots()
bottom = np.zeros(8)

for label, fc in all_fc_short.items():
    p = ax.bar(labels, fc, width=0.65, label=label, bottom = bottom)
    bottom += fc
#ax.legend(fontsize = 8, markerscale = 0.75, frameon = True, labelspacing = 0.2, handlelength = 0.8, loc = 'lower left',bbox_to_anchor=(0.762, -0.005))
ax.legend(fontsize = 8, markerscale = 0.75, handlelength = 0.9, loc='lower center', bbox_to_anchor=(0.5, 1), ncol=len(labels), frameon=False)
ax.set_ylabel("Incidence (%)")
ax.set_xticklabels(labels, rotation = 45, ha = 'right')
plt.tight_layout()
plt.axvline(x=3.5, color='gray', linestyle='--', alpha=0.5)
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/barplot all gsr comp', dpi = 400)
plt.show

for i in range(len(data_x)):
    kernel = gaussian_kde(data_x[i], bw_method = 0.6)
    gkde = kernel(x)
    kdes_x.append(gkde)

for i in range(len(data_y)):
    kernel = gaussian_kde(data_y[i], bw_method = 0.6)
    gkde = kernel(y)
    kdes_y.append(gkde)

colors = og_colors
colors[7] = 'lightskyblue'
colors[5] = 'mediumseagreen'
plt.rcParams['axes.prop_cycle'] = cycler(color=colors)

fig = plt.figure(figsize = (7, 6), tight_layout = True)
gs = GridSpec(2,2, figure = fig, height_ratios= [1, 5], width_ratios = [5, 1])

ax0 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])

for i in range(len(data_x)):
    if i < 4:
        ax0.plot(x, kdes_x[i], alpha=0.15)
        ax0.fill_between(x, kdes_x[i], alpha = 0.05)
    else:
        ax0.plot(x, kdes_x[i], alpha=0.5)
        ax0.fill_between(x, kdes_x[i], alpha = 0.2)

ax0.set_xlim([-0.2, 1])

for i in range(len(data_y)):
    if i < 4:
        ax3.plot(kdes_y[i], y, alpha=0.15)
        ax3.fill_between(kdes_y[i], y, alpha = 0.05)
    else:
        ax3.plot(kdes_y[i], y, alpha=0.5)
        ax3.fill_between(kdes_y[i], y, alpha = 0.2)

ax2.set_ylim([-0.7, 1])
ax3.set_ylim([-0.7, 1])



for i in range(len(data_x)):
    if i < 4:
        ax2.plot(data_x[i], data_y[i], linestyle='', marker='o', label=labels[i], markersize = 5, alpha = 0.25, markeredgecolor = 'none')  # , c = cmap[0])
    else:
        ax2.plot(data_x[i], data_y[i], linestyle='', marker='o', label=labels[i], markersize=4)  # , c = cmap[0])
ax2.set_xlabel('Correlation S1bf left to right (r)')
ax2.set_ylabel('Correlation S1bf left to ACA (r)')
ax2.set_xlim([-0.3, 1])
ax2.set_ylim([-0.7, 1])
ax2.legend(fontsize = 8, markerscale = 0.75, frameon = False, title = 'Dataset', title_fontsize = 9, labelspacing = 0.2, handlelength = 0, borderaxespad = 2, draggable = True)
ax2.hlines(y = r_threshold, xmin=-r_threshold, xmax=0.8, linestyle='--', color='k')
ax2.vlines(x = r_threshold, ymin=-0.4, ymax=0.8, linestyle='--', color='k')
ax2.hlines(y = -r_threshold, xmin=-r_threshold, xmax=r_threshold, linestyle='--', color='k')
ax2.vlines(x = -r_threshold, ymin=-r_threshold, ymax=r_threshold, linestyle='--', color='k')
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

plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/qc corrs GSR comp all.png', dpi = 400, bbox_inches='tight')


plt.show()
