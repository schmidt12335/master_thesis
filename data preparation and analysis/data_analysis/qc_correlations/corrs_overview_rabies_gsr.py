import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from matplotlib.gridspec import GridSpec

corrs_r_matlab_all = np.load('corrs_r_matlab_all.npy')
corrs_r2_matlab_all = np.load('corrs_r2_matlab_all.npy')

corrs_r_matlab_all_gsr = np.load('corrs_r_matlab_all_gsr.npy')
corrs_r2_matlab_all_gsr = np.load('corrs_r2_matlab_all_gsr.npy')

corrs_r_mdma_all = np.load('corrs_r_mdma_all.npy')
corrs_r2_mdma_all = np.load('corrs_r2_mdma_all.npy')

corrs_r_mdma_all_gsr = np.load('corrs_r_mdma_all_gsr.npy')
corrs_r2_mdma_all_gsr = np.load('corrs_r2_mdma_all_gsr.npy')

corrs_r_rabies = np.load('corrs_r_rabies.npy')
corrs_r2_rabies = np.load('corrs_r2_rabies.npy')

corrs_r_rabies_gsr = np.load('corrs_r_rabies_gsr.npy')
corrs_r2_rabies_gsr = np.load('corrs_r2_rabies_gsr.npy')

corrs_r_rabies_0_3 = np.load('corrs_r_rabies_all_0.3.npy')
corrs_r2_rabies_0_3 = np.load('corrs_r2_rabies_all_0.3.npy')

corrs_r_rabies_0_3_gsr = np.load('corrs_r_rabies_all_0.3_gsr.npy')
corrs_r2_rabies_0_3_gsr = np.load('corrs_r2_rabies_all_0.3_gsr.npy')

corrs_r_rabies_0_5 = np.load('corrs_r_rabies_all_0.5.npy')
corrs_r2_rabies_0_5 = np.load('corrs_r2_rabies_all_0.5.npy')

corrs_r_rabies_0_5_gsr = np.load('corrs_r_rabies_all_0.5_gsr.npy')
corrs_r2_rabies_0_5_gsr = np.load('corrs_r2_rabies_all_0.5_gsr.npy')

corrs_r_marciano = np.load('corrs_r_marciano_smoothed.npy')
corrs_r2_marciano = np.load('corrs_r2_marciano_smoothed.npy')

corrs_r_marciano_gsr = np.load('corrs_r_marciano_smoothed_gsr.npy')
corrs_r2_marciano_gsr = np.load('corrs_r2_marciano_smoothed_gsr.npy')



data_x_kde = [corrs_r_rabies, corrs_r_rabies_gsr, corrs_r_rabies_0_3, corrs_r_rabies_0_3_gsr,corrs_r_rabies_0_5, corrs_r_rabies_0_5_gsr]
data_y_kde = [corrs_r2_rabies, corrs_r2_rabies_gsr, corrs_r2_rabies_0_3, corrs_r2_rabies_0_3_gsr, corrs_r2_rabies_0_5, corrs_r2_rabies_0_5_gsr]
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

ax2.plot(corrs_r_rabies, corrs_r2_rabies, linestyle='', marker = 'o', label = 'Rabies')
ax2.plot(corrs_r_rabies_gsr, corrs_r2_rabies_gsr, linestyle='', marker = 'o', label = 'Rabies GSR')
ax2.plot(corrs_r_rabies_0_3, corrs_r2_rabies_0_3, linestyle='', marker = 'o', label = 'Rabies 0.3mm³')
ax2.plot(corrs_r_rabies_0_3_gsr, corrs_r2_rabies_0_3_gsr, linestyle='', marker = 'o', label = 'Rabies 0.3mm³ GSR')
ax2.plot(corrs_r_rabies_0_5, corrs_r2_rabies_0_5, linestyle='', marker = 'o', label = 'Rabies 0.5mm³')
ax2.plot(corrs_r_rabies_0_5_gsr, corrs_r2_rabies_0_5_gsr, linestyle='', marker = 'o', label = 'Rabies 0.5mm³ GSR')
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

ax0.axis('off')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax3.axis('off')

plt.show()