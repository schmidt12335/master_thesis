import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat


subject_num = 21 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_rabies_prepro" # 2.Change folder directory to your conn project folder

subjects = np.arange(1, subject_num + 1)
corrs_r = []
corrs_r2 = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0]
    rois = file['names'][0]
    for j, k in enumerate(rois):
        print(j, k)
    accl = data[3][20::].flatten()
    s1bfl = data[4][20::].flatten()
    s1bfr = data[5][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)

    #fig, ax = plt.subplots()
    #ax.plot(time, s1bfl, label = 's1bfl', c = 'lightcoral')
    #ax.plot(time, s1bfr, label = 's1bfr', c = 'darkred')
    #ax.plot(time, accl, label = 'accl', c = 'darkturquoise')
    ##ax.plot(time, accr, label = 'accr', c = 'darkcyan')
    #ax.set_ylabel('% signal change')
    #ax.set_xlabel('time [min]')
    #ax.legend()
    #plt.show()

np.save('corrs_r_rabies.npy', corrs_r)
np.save('corrs_r2_rabies.npy', corrs_r2)

corrs_r = np.load('corrs_r.npy')
corrs_r2 = np.load('corrs_r2.npy')

corrs_r_rabies = np.load('corrs_r_rabies.npy')
corrs_r2_rabies = np.load('corrs_r2_rabies.npy')

x_rect = [0.4, 0.4, 0.1, 0.1, 0.4]
y_rect = [-0.5, 0.1, 0.1, -0.5, -0.5]

fig2, ax2 = plt.subplots(1,2, sharey = True, sharex=True, figsize = (14, 4))
ax2[0].plot(corrs_r, corrs_r2, linestyle='', marker = 'o')
ax2[0].axhline(0.1)
ax2[0].axvline(0.1)
ax2[0].fill(x_rect, y_rect, color = 'green', alpha = 0.3)
#ax2[0].set_xlim([0, 0.4])
#ax2[0].set_ylim([-0.4, 0.4])
ax2[0].set_ylabel('Corr S1BFl - Accl')
ax2[0].set_xlabel('Corr S1BFl - S1BFr')
ax2[0].set_title('matlab')

ax2[1].plot(corrs_r_rabies, corrs_r2_rabies, linestyle='', marker = 'o')
ax2[1].axhline(0.1)
ax2[1].axvline(0.1)
ax2[1].set_title('rabies')
ax2[1].set_xlabel('Corr S1BFl - S1BFr')
ax2[1].fill(x_rect, y_rect, color = 'green', alpha = 0.3)


good_r = []
for i in range(len(corrs_r)):
    if corrs_r[i] > 0.1 and corrs_r2[i] < 0.1:
        good_r.append(i)
print(f'for matlab, {len(good_r)} good animals')

good_r_rabies = []
for i in range(len(corrs_r_rabies)):
    if corrs_r_rabies[i] > 0.1 and corrs_r2_rabies[i] < 0.1:
        good_r_rabies.append(i)
print(f'for rabies, {len(good_r_rabies)} good animals')

plt.show()

