import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from matplotlib.gridspec import GridSpec
from cycler import cycler
gsr_comparison = True

corrs_r_matlab_all = np.load('corrs_r_matlab_all.npy')
corrs_r2_matlab_all = np.load('corrs_r2_matlab_all.npy')

corrs_r_matlab_all_gsr = np.load('corrs_r_matlab_all_gsr.npy')
corrs_r2_matlab_all_gsr = np.load('corrs_r2_matlab_all_gsr.npy')

corrs_r_mdma_all = np.load('corrs_r_mdma_all.npy')
corrs_r2_mdma_all = np.load('corrs_r2_mdma_all.npy')

corrs_r_mdma_all_gsr = np.load('corrs_r_mdma_all_gsr.npy')
corrs_r2_mdma_all_gsr = np.load('corrs_r2_mdma_all_gsr.npy')

corrs_r_marciano = np.load('corrs_r_marciano_smoothed.npy')
corrs_r2_marciano = np.load('corrs_r2_marciano_smoothed.npy')

corrs_r_marciano_gsr = np.load('corrs_r_marciano_smoothed_gsr.npy')
corrs_r2_marciano_gsr = np.load('corrs_r2_marciano_smoothed_gsr.npy')

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
    return specific/len(r_data)*100, non_specific/len(r_data)*100, no_fc/len(r_data)*100, spurious_fc/len(r_data)*100


alpha_specific, alpha_non_specific, alpha_no_fc, alpha_spurious_fc = get_incidence(corrs_r_matlab_all, corrs_r2_matlab_all)
alpha_specific_gsr, alpha_non_specific_gsr, alpha_no_fc_gsr, alpha_spurious_fc_gsr = get_incidence(corrs_r_matlab_all_gsr, corrs_r2_matlab_all_gsr)
iso_specific, iso_non_specific, iso_no_fc, iso_spurious_fc = get_incidence(corrs_r_mdma_all, corrs_r2_mdma_all)
iso_specific_gsr, iso_non_specific_gsr, iso_no_fc_gsr, iso_spurious_fc_gsr = get_incidence(corrs_r_mdma_all_gsr, corrs_r2_mdma_all_gsr)
mede_specific, mede_non_specific, mede_no_fc, mede_spurious_fc = get_incidence(corrs_r_marciano, corrs_r2_marciano)
mede_specific_gsr, mede_non_specific_gsr, mede_no_fc_gsr, mede_spurious_fc_gsr = get_incidence(corrs_r_marciano_gsr, corrs_r2_marciano_gsr)

if gsr_comparison == True:

    x_labels = ("Alpha-chloralose\n + 0.5% Iso", "1.3% Isoflurane", "Medetomidin\n + 0.5% Iso", "Alpha-chloralose\n + 0.5% Iso\n GSR", "1.3% Isoflurane\n GSR", "Medetomidin\n + 0.5% Iso\n GSR")

    alpha_fc = {
        "specific": np.array([alpha_specific, iso_specific, mede_specific, alpha_specific_gsr, iso_specific_gsr, mede_specific_gsr]),
        "Spurious": np.array([alpha_spurious_fc, iso_spurious_fc, mede_spurious_fc, alpha_spurious_fc_gsr, iso_spurious_fc_gsr, mede_spurious_fc_gsr]),
        "Non-specific": np.array([alpha_non_specific, iso_non_specific, mede_non_specific, alpha_non_specific_gsr, iso_non_specific_gsr, mede_non_specific_gsr]),
        "No FC": np.array([alpha_no_fc, iso_no_fc, mede_no_fc, alpha_no_fc_gsr, iso_no_fc_gsr, mede_no_fc_gsr])}

    fig1, ax = plt.subplots()
    bottom = np.zeros(6)

    for label, fc in alpha_fc.items():
        p = ax.bar(x_labels, fc, width=0.6, label=label, bottom = bottom)
        bottom += fc
    ax.legend(fontsize = 8, markerscale = 0.75, frameon = True, labelspacing = 0.2, handlelength = 0.8, borderaxespad = 2, draggable = True)
    ax.set_ylabel("Incidence (%)")
    ax.tick_params(axis = 'x', length = 0)


    data_x_kde = [corrs_r_matlab_all, corrs_r_matlab_all_gsr, corrs_r_mdma_all, corrs_r_mdma_all_gsr, corrs_r_marciano, corrs_r_marciano_gsr]
    data_y_kde = [corrs_r2_matlab_all, corrs_r2_matlab_all_gsr, corrs_r2_mdma_all, corrs_r2_mdma_all_gsr, corrs_r2_marciano, corrs_r2_marciano_gsr]
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

    CB_cmap = ['#377eb8', '#4daf4a', '#ff7f00',
               '#f781bf', '#a65628', '#984ea3',
               '#999999', '#e41a1c', '#dede00']
    plt.rcParams['axes.prop_cycle'] = cycler(color=CB_cmap)

    ax2.plot(corrs_r_matlab_all, corrs_r2_matlab_all, linestyle='', marker = 'o', label = 'alpha-chlor.')#, c = cmap[0])
    ax2.plot(corrs_r_matlab_all_gsr, corrs_r2_matlab_all_gsr, linestyle='', marker = 'o', label = 'alpha-chlor. GSR')#, c = cmap[0])
    ax2.plot(corrs_r_mdma_all, corrs_r2_mdma_all, linestyle='', marker = 'o', label = '1.3% Iso')#, c = cmap[1])
    ax2.plot(corrs_r_mdma_all_gsr, corrs_r2_mdma_all_gsr, linestyle='', marker = 'o', label = '1.3% Iso GSR')#, c = cmap[1])
    ax2.plot(corrs_r_marciano, corrs_r2_marciano, linestyle='', marker = 'o', label = 'medetomidin')#, c = cmap[2])
    ax2.plot(corrs_r_marciano_gsr, corrs_r2_marciano_gsr, linestyle='', marker = 'o', label = 'medetomidin GSR')#, c = cmap[2])
    ax2.set_xlabel('Correlation S1bf left to right (r)')
    ax2.set_ylabel('Correlation S1bf left to ACA (r)')
    ax2.set_xlim([-0.3, 1])
    ax2.set_ylim([-0.7, 1])
    ax2.legend(fontsize = 8, markerscale = 0.75, frameon = False, title = 'Anaesthesia', title_fontsize = 9, labelspacing = 0.2, handlelength = 0, borderaxespad = 2, draggable = True)
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

else:

    x_labels = ("Alpha-chloralose\n + 0.5% Iso", "1.3% Isoflurane", "Medetomidin\n + 0.5% Iso")

    alpha_fc = {
        "specific": np.array(
            [alpha_specific, iso_specific, mede_specific]),
        "Spurious": np.array(
            [alpha_spurious_fc, iso_spurious_fc, mede_spurious_fc]),
        "Non-specific": np.array(
            [alpha_non_specific, iso_non_specific, mede_non_specific]),
        "No FC": np.array([alpha_no_fc, iso_no_fc, mede_no_fc])}

    fig1, ax = plt.subplots()
    bottom = np.zeros(3)

    for label, fc in alpha_fc.items():
        p = ax.bar(x_labels, fc, width=0.6, label=label, bottom=bottom)
        bottom += fc
    ax.legend(fontsize=8, markerscale=0.75, frameon=True, labelspacing=0.2, handlelength=0.8, borderaxespad=2,
              draggable=True)
    ax.set_ylabel("Incidence (%)")
    ax.tick_params(axis='x', length=0)
    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)

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
        kernel = gaussian_kde(data_x_kde[i], bw_method=0.6)
        gkde = kernel(x)
        kdes_x.append(gkde)

    for i in range(len(data_y_kde)):
        kernel = gaussian_kde(data_y_kde[i], bw_method=0.6)
        gkde = kernel(y)
        kdes_y.append(gkde)

    fig = plt.figure(figsize=(7, 6), tight_layout=True)
    gs = GridSpec(2, 2, figure=fig, height_ratios=[1, 5], width_ratios=[5, 1])

    ax0 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[1, 1])

    for i in range(len(data_x_kde)):
        ax0.plot(x, kdes_x[i], alpha=0.5)
        ax0.fill_between(x, kdes_x[i], alpha=0.2)

    ax0.set_xlim([-0.2, 1])

    for i in range(len(data_y_kde)):
        ax3.plot(kdes_y[i], y, alpha=0.5)
        ax3.fill_between(kdes_y[i], y, alpha=0.2)

    ax2.set_ylim([-0.7, 1])
    ax3.set_ylim([-0.7, 1])

    # cmap = ['#377eb8', '#ff7f00', '#4daf4a', 'mediumvioletred', '#a65628', '#984ea3', '#999999', '#e41a1c', '#dede00']

    ax2.plot(corrs_r_matlab_all_gsr, corrs_r2_matlab_all_gsr, linestyle='', marker='o', label='alpha-chlor. GSR')  # , c = cmap[0])
    ax2.plot(corrs_r_mdma_all_gsr, corrs_r2_mdma_all_gsr, linestyle='', marker='o', label='1.3% Iso GSR')  # , c = cmap[1])
    ax2.plot(corrs_r_marciano_gsr, corrs_r2_marciano_gsr, linestyle='', marker='o', label='medetomidin GSR')  # , c = cmap[2])
    ax2.set_xlabel('Correlation S1bf left to right (r)')
    ax2.set_ylabel('Correlation S1bf left to ACA (r)')
    ax2.set_xlim([-0.3, 1])
    ax2.set_ylim([-0.7, 1])
    ax2.legend(fontsize=8, markerscale=0.75, frameon=False, title='Anaesthesia', title_fontsize=9, labelspacing=0.2,
               handlelength=0, borderaxespad=2, draggable=True)
    ax2.hlines(y=0.1, xmin=-0.1, xmax=0.8, linestyle='--', color='k')
    ax2.vlines(x=0.1, ymin=-0.4, ymax=0.8, linestyle='--', color='k')
    ax2.hlines(y=-0.1, xmin=-0.1, xmax=0.1, linestyle='--', color='k')
    ax2.vlines(x=-0.1, ymin=-0.1, ymax=0.1, linestyle='--', color='k')
    ax2.set_xticks([-0.2, 0, 0.2, 0.4, 0.6, 0.8], labels=[-0.2, 0, 0.2, 0.4, 0.6, 0.8])
    ax2.set_yticks([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], labels=[-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8])

    ax0.axis('off')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax3.axis('off')

    plt.show()