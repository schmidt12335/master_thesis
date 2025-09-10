import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from matplotlib.gridspec import GridSpec
from cycler import cycler
from scipy.io import loadmat


corrs_r_rabies_qc = np.load('corrs_r_rabies_QC_0.5_NEW.npy')
corrs_r2_rabies_qc = np.load('corrs_r2_rabies_QC_0.5_NEW.npy')

corrs_r_rabies_qc_gsr = np.load('corrs_r_rabies_qc_gsr.npy')
corrs_r2_rabies_qc_gsr = np.load('corrs_r2_rabies_qc_gsr.npy')

data_x_kde = [corrs_r_rabies_qc, corrs_r_rabies_qc_gsr]
data_y_kde = [corrs_r2_rabies_qc, corrs_r2_rabies_qc_gsr]
kdes_x = []
kdes_y = []

xmin = -1
xmax = 1
ymin = -1
ymax = 2
dx = 0.0005
x = np.arange(xmin, xmax, dx)
y = np.arange(ymin, ymax, dx)

data_x = [corrs_r_rabies_qc, corrs_r_rabies_qc_gsr]
data_y = [corrs_r2_rabies_qc, corrs_r2_rabies_qc_gsr]

x_labels = [f'AC RABIES', f'AC RABIES GSR']

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

ax2.legend(fontsize = 8, markerscale = 0.75, frameon = False, title = 'Dataset', title_fontsize = 9, labelspacing = 0.2, handlelength = 0, borderaxespad = 2, draggable = True)
ax2.hlines(y = 0.1, xmin=-0.1, xmax=0.8, linestyle='--', color='k')
ax2.vlines(x = 0.1, ymin=-0.4, ymax=0.8, linestyle='--', color='k')
ax2.hlines(y = -0.1, xmin=-0.1, xmax=0.1, linestyle='--', color='k')
ax2.vlines(x = -0.1, ymin=-0.1, ymax=0.1, linestyle='--', color='k')
ax2.set_xticks([-0.2, 0, 0.2, 0.4, 0.6, 0.8], labels = [-0.2, 0, 0.2, 0.4, 0.6, 0.8])
ax2.set_yticks([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], labels = [-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8])

ax0.axis('off')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax3.axis('off')


print(data_x, data_y)

plt.show()
