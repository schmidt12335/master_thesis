import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat



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

corrs_r_marciano = np.load('corrs_r_marciano_smoothed.npy')
corrs_r2_marciano = np.load('corrs_r2_marciano_smoothed.npy')

corrs_r_marciano_gsr = np.load('corrs_r_marciano_smoothed_gsr.npy')
corrs_r2_marciano_gsr = np.load('corrs_r2_marciano_smoothed_gsr.npy')

x_rect = [0.4, 0.4, 0.1, 0.1, 0.4]
y_rect = [-0.5, 0.1, 0.1, -0.5, -0.5]

fig2, ax2 = plt.subplots(2,4, sharey = True, sharex=True, figsize = (14, 4))

ax2[0,0].plot(corrs_r_matlab_all, corrs_r2_matlab_all, linestyle='', marker = 'o')
ax2[0,0].axhline(0.1)
ax2[0,0].axvline(0.1)
ax2[0,0].set_title('Haas Matlab')
ax2[0,0].set_xlabel('Corr S1BFl - S1BFr')
ax2[0,0].fill(x_rect, y_rect, color = 'green', alpha = 0.3)

ax2[1,0].plot(corrs_r_matlab_all_gsr, corrs_r2_matlab_all_gsr, linestyle='', marker = 'o')
ax2[1,0].axhline(0.1)
ax2[1,0].axvline(0.1)
ax2[1,0].set_title('Haas Matlab GSR')
ax2[1,0].set_xlabel('Corr S1BFl - S1BFr')
ax2[1,0].fill(x_rect, y_rect, color = 'green', alpha = 0.3)

ax2[0,1].plot(corrs_r_mdma_all, corrs_r2_mdma_all, linestyle='', marker = 'o')
ax2[0,1].axhline(0.1)
ax2[0,1].axvline(0.1)
ax2[0,1].set_title('MDMA data')
ax2[0,1].set_xlabel('Corr S1BFl - S1BFr')
ax2[0,1].fill(x_rect, y_rect, color = 'green', alpha = 0.3)

ax2[1,1].plot(corrs_r_mdma_all_gsr, corrs_r2_mdma_all_gsr, linestyle='', marker = 'o')
ax2[1,1].axhline(0.1)
ax2[1,1].axvline(0.1)
ax2[1,1].set_title('MDMA data GSR')
ax2[1,1].set_xlabel('Corr S1BFl - S1BFr')
ax2[1,1].fill(x_rect, y_rect, color = 'green', alpha = 0.3)

ax2[0,2].plot(corrs_r_rabies, corrs_r2_rabies, linestyle='', marker = 'o')
ax2[0,2].axhline(0.1)
ax2[0,2].axvline(0.1)
ax2[0,2].set_title('Haas Rabies')
ax2[0,2].set_xlabel('Corr S1BFl - S1BFr')
ax2[0,2].fill(x_rect, y_rect, color = 'green', alpha = 0.3)

ax2[1,2].plot(corrs_r_rabies_gsr, corrs_r2_rabies_gsr, linestyle='', marker = 'o')
ax2[1,2].axhline(0.1)
ax2[1,2].axvline(0.1)
ax2[1,2].set_title('Haas Rabies GSR')
ax2[1,2].set_xlabel('Corr S1BFl - S1BFr')
ax2[1,2].fill(x_rect, y_rect, color = 'green', alpha = 0.3)

ax2[0,3].plot(corrs_r_marciano, corrs_r2_marciano, linestyle='', marker = 'o')
ax2[0,3].axhline(0.1)
ax2[0,3].axvline(0.1)
ax2[0,3].set_title('Marciano smoothed')
ax2[0,3].set_xlabel('Corr S1BFl - S1BFr')
ax2[0,3].fill(x_rect, y_rect, color = 'green', alpha = 0.3)

ax2[1,3].plot(corrs_r_marciano_gsr, corrs_r2_marciano_gsr, linestyle='', marker = 'o')
ax2[1,3].axhline(0.1)
ax2[1,3].axvline(0.1)
ax2[1,3].set_title('Marciaco smoothed GSR')
ax2[1,3].set_xlabel('Corr S1BFl - S1BFr')
ax2[1,3].fill(x_rect, y_rect, color = 'green', alpha = 0.3)

plt.show()

