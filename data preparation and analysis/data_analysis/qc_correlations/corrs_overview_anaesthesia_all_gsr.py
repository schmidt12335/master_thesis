import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde, chi2_contingency
from matplotlib.gridspec import GridSpec
import pandas as pd
from scipy.stats import fisher_exact
from cycler import cycler

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


corrs_r_matlab_all_gsr = np.load('corrs_r_matlab_all_gsr.npy')
corrs_r2_matlab_all_gsr = np.load('corrs_r2_matlab_all_gsr.npy')

corrs_r_mdma_all_gsr = np.load('corrs_r_mdma_all_gsr.npy')
corrs_r2_mdma_all_gsr = np.load('corrs_r2_mdma_all_gsr.npy')

corrs_r_marciano_gsr = np.load('corrs_r_marciano_smoothed_gsr.npy')
corrs_r2_marciano_gsr = np.load('corrs_r2_marciano_smoothed_gsr.npy')

data_x = [corrs_r_matlab_all_gsr, corrs_r_mdma_all_gsr, corrs_r_marciano_gsr]
data_y = [corrs_r2_matlab_all_gsr, corrs_r2_mdma_all_gsr, corrs_r2_marciano_gsr]

incidence_all = []

for i in range(len(data_x)):
    incidence_all.append(get_incidence(data_x[i], data_y[i]))

total_incidence = np.sum(incidence_all, axis = 0)/len(data_x)
fc_categories = ['Specific FC', 'Non-specific FC', 'No FC', 'Spurious FC']
fc_categories_short = ['Specific', 'Spurious', 'Non-specific', 'No FC']
print(f'total incidence = {total_incidence}', f'incidence ={incidence_all}')

x_labels = (["α-chloralose", "Isoflurane", "Medetomidine"])

all_fc = {}
for i in range(len(fc_categories)):
    all_fc[fc_categories[i]] = np.array([
        incidence_all[0][i],
        incidence_all[1][i],
        incidence_all[2][i]])

incidence_all_short = []

for i in range(len(data_x)):
    incidence_all_short.append(get_incidence_bar(data_x[i], data_y[i]))

all_fc_short = {}
for i in range(len(fc_categories_short)):
    all_fc_short[fc_categories_short[i]] = np.array([
        incidence_all_short[0][i],
        incidence_all_short[1][i],
        incidence_all_short[2][i]])

# example p-values from pairwise tests
p_values = []

# Run all 3 pairwise tests and collect p-values
p_values.append(fisher_exact([[16, 14], [8, 1]])[1])  # A vs B
p_values.append(fisher_exact([[16, 14], [22, 1]])[1])  # A vs C
p_values.append(fisher_exact([[8, 1], [22, 1]])[1])    # B vs C

# Bonferroni corrected threshold
alpha_corrected = 0.05 / len(p_values)

# Check significance
for i, p in enumerate(p_values):
    print(f"Comparison {i+1}: p = {p:.4f} {'(significant)' if p < alpha_corrected else ''}")

x = np.arange(len(x_labels))
y_max = 100
y_bar = y_max + 2  # height of the significance bar
h = 1

fig1, ax = plt.subplots(figsize = (4,4))
bottom = np.zeros(3)

for label, fc in all_fc_short.items():
    p = ax.bar(x_labels, fc, width=0.6, label=label, bottom = bottom)
    bottom += fc
ax.plot([x[0], x[0], x[2], x[2]], [y_bar, y_bar+h, y_bar+h, y_bar], lw=1, c='k')
ax.text((x[0] + x[2]) / 2, y_bar + h + 0.5, '**', ha='center', va='bottom', fontsize=10)
ax.legend(fontsize = 10, markerscale = 0.75, frameon = True, labelspacing = 0.2, handlelength = 0.8, loc = 'lower left',bbox_to_anchor=(0.592, -0.005))
ax.set_ylabel("Incidence (%)")
ax.tick_params(axis = 'x', length = 0)
plt.tight_layout()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/barplot anaesthesia comp.png', dpi = 400)

data_x_kde = [corrs_r_matlab_all_gsr, corrs_r_mdma_all_gsr, corrs_r_marciano_gsr]
data_y_kde = [corrs_r2_matlab_all_gsr, corrs_r2_mdma_all_gsr, corrs_r2_marciano_gsr]
kdes_x = []
kdes_y = []

xmin = -1
xmax = 1
ymin = -1
ymax = 2
dx = 0.0005
x = np.arange(xmin, xmax, dx)
y = np.arange(ymin, ymax, dx)


for i in range(len(data_x_kde)):
    kernel = gaussian_kde(data_x_kde[i], bw_method = 0.6)
    gkde = kernel(x)
    kdes_x.append(gkde)

for i in range(len(data_y_kde)):
    kernel = gaussian_kde(data_y_kde[i], bw_method = 0.6)
    gkde = kernel(y)
    kdes_y.append(gkde)

CB_cmap = ['#377eb8', '#4daf4a', '#ff7f00',
                  '#f781bf', '#a65628', '#984ea3',
                  '#999999', '#e41a1c', '#dede00']
plt.rcParams['axes.prop_cycle'] = cycler(color=CB_cmap)

fig = plt.figure(figsize = (7,6), tight_layout = True)
gs = GridSpec(2,2, figure = fig, height_ratios= [1,5], width_ratios = [5,1])

ax0 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])

for i in range(len(data_x_kde)):
    ax0.plot(x, kdes_x[i], alpha=0.5)
    ax0.fill_between(x, kdes_x[i], alpha = 0.2)

ax0.set_xlim([-0.2, 1])

for i in range(len(data_y_kde)):
    ax3.plot(kdes_y[i], y, alpha=0.5)
    ax3.fill_between(kdes_y[i], y, alpha = 0.2)

ax2.set_ylim([-0.7, 1])
ax3.set_ylim([-0.7, 1])

for i in range(len(data_x)):
    ax2.plot(data_x[i], data_y[i], linestyle='', marker='o', label=x_labels[i], markersize = 4)
ax2.set_xlabel('Correlation S1bf left to right (r)')
ax2.set_ylabel('Correlation S1bf left to ACA (r)')
ax2.set_xlim([-0.3, 1])
ax2.set_ylim([-0.7, 1])
ax2.legend(fontsize = 10, markerscale = 0.75, frameon = False, title = 'Anaesthesia', title_fontsize = 11, labelspacing = 0.2, handlelength = 0, borderaxespad = 2, draggable = True)
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
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/qc corrs anaesthesia gsr.png', dpi = 400)

plt.show()
