import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

"""
## RABIES 0.3 ##

subject_num = 17 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_rabies_all_rois_smoothed_0.3" # 2.Change folder directory to your conn project folder

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
    accl = data[101][20::].flatten()
    s1bfl = data[105][20::].flatten()
    s1bfr = data[106][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)


np.save('corrs_r_rabies_all_0.3.npy', corrs_r)
np.save('corrs_r2_rabies_all_0.3.npy', corrs_r2)


## RABIES 0.3 GSR ###
subject_num = 17 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_rabies_all_rois_smoothed_0.3_gsr" # 2.Change folder directory to your conn project folder

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
    accl = data[101][20::].flatten()
    s1bfl = data[105][20::].flatten()
    s1bfr = data[106][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)


np.save('corrs_r_rabies_all_0.3_gsr.npy', corrs_r)
np.save('corrs_r2_rabies_all_0.3_gsr.npy', corrs_r2)

"""
## RABIES 0.5 ##

subject_num = 21 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/rabies_data_new/no_gsr" # 2.Change folder directory to your conn project folder

subjects = np.arange(1, subject_num + 1)
corrs_r = []
corrs_r2 = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0]
    rois = file['names'][0]
    for j, k in enumerate(rois):
        print(j, k)
    accl = data[101][20::].flatten()
    s1bfl = data[105][20::].flatten()
    s1bfr = data[106][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)


np.save('../corrs_r_rabies_all_0.5_new.npy', corrs_r)
np.save('../corrs_r2_rabies_all_0.5_new.npy', corrs_r2)


## RABIES 0.5 GSR ##

subject_num = 18 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_rabies_all_rois_smoothed_0.5_gsr/results/preprocessing" # 2.Change folder directory to your conn project folder

subjects = np.arange(1, subject_num + 1)
corrs_r = []
corrs_r2 = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0]
    rois = file['names'][0]
    for j, k in enumerate(rois):
        print(j, k)
    accl = data[102][20::].flatten()
    s1bfl = data[106][20::].flatten()
    s1bfr = data[107][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)


np.save('../corrs_r_rabies_all_0.5_gsr_new.npy', corrs_r)
np.save('../corrs_r2_rabies_all_0.5_gsr_new.npy', corrs_r2)



"""
corrs_r = np.load('corrs_r.npy')
corrs_r2 = np.load('corrs_r2.npy')

corrs_r_rabies = np.load('corrs_r_rabies.npy')
corrs_r2_rabies = np.load('corrs_r2_rabies.npy')

corrs_r_rabies_all = np.load('corrs_r_rabies_all.npy')
corrs_r2_rabies_all = np.load('corrs_r2_rabies_all.npy')

corrs_r_matlab_all = np.load('corrs_r_matlab_all.npy')
corrs_r2_matlab_all = np.load('corrs_r2_matlab_all.npy')

x_rect = [0.4, 0.4, 0.1, 0.1, 0.4]
y_rect = [-0.5, 0.1, 0.1, -0.5, -0.5]

fig2, ax2 = plt.subplots(1,4, sharey = True, sharex=True, figsize = (14, 4))
ax2[0].plot(corrs_r, corrs_r2, linestyle='', marker = 'o')
ax2[0].axhline(0.1)
ax2[0].axvline(0.1)
ax2[0].fill(x_rect, y_rect, color = 'green', alpha = 0.3)
#ax2[0].set_xlim([0, 0.4])
#ax2[0].set_ylim([-0.4, 0.4])
ax2[0].set_ylabel('Corr S1BFl - Accl')
ax2[0].set_xlabel('Corr S1BFl - S1BFr')
ax2[0].set_title('matlab qc rois')

ax2[1].plot(corrs_r_matlab_all, corrs_r2_matlab_all, linestyle='', marker = 'o')
ax2[1].axhline(0.1)
ax2[1].axvline(0.1)
ax2[1].set_title('matlab all rois')
ax2[1].set_xlabel('Corr S1BFl - S1BFr')
ax2[1].fill(x_rect, y_rect, color = 'green', alpha = 0.3)

ax2[2].plot(corrs_r_rabies, corrs_r2_rabies, linestyle='', marker = 'o')
ax2[2].axhline(0.1)
ax2[2].axvline(0.1)
ax2[2].set_title('rabies qc rois')
ax2[2].set_xlabel('Corr S1BFl - S1BFr')
ax2[2].fill(x_rect, y_rect, color = 'green', alpha = 0.3)

ax2[3].plot(corrs_r_rabies_all, corrs_r2_rabies_all, linestyle='', marker = 'o')
ax2[3].axhline(0.1)
ax2[3].axvline(0.1)
ax2[3].set_title('rabies all rois')
ax2[3].set_xlabel('Corr S1BFl - S1BFr')
ax2[3].fill(x_rect, y_rect, color = 'green', alpha = 0.3)


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
"""
