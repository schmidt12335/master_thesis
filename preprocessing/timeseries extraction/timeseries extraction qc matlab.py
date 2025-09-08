import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat


### SaBu Rabies ###

subject_num = 21 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_schifer_QC_rois_gsr" # 2.Change folder directory to your conn project folder

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
    s1bfr = data[3][20::].flatten()
    accl = data[4][20::].flatten()
    s1bfl = data[5][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)

np.save('corrs_r_matlab_qc_gsr.npy', corrs_r)
np.save('corrs_r2_matlab_qc_gsr.npy', corrs_r2)


### SaBu Rabies with GSR ###

subject_num = 18 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_rabies_QC_rois_smoothed_0.5_gsr" # 2.Change folder directory to your conn project folder

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

np.save('corrs_r_rabies_qc_gsr.npy', corrs_r)
np.save('corrs_r2_rabies_qc_gsr.npy', corrs_r2)



