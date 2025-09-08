import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

"""
### MDMA ###

subject_num = 9 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_mdma_all_rois" # 2.Change folder directory to your conn project folder

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
    accl = data[11][20::].flatten()
    s1bfl = data[29][20::].flatten()
    s1bfr = data[30][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)

np.save('corrs_r_mdma_all.npy', corrs_r)
np.save('corrs_r2_mdma_all.npy', corrs_r2)


### MDMA with GSR ###

subject_num = 9 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_mdma_all_rois_gsr" # 2.Change folder directory to your conn project folder

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
    accl = data[11][20::].flatten()
    s1bfl = data[29][20::].flatten()
    s1bfr = data[30][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)

np.save('corrs_r_mdma_all_gsr.npy', corrs_r)
np.save('corrs_r2_mdma_all_gsr.npy', corrs_r2)

### marciano smoothed ###

subject_num = 23 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_new_sabina_data_smoothed" # 2.Change folder directory to your conn project folder

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
    accl = data[11][20::].flatten()
    s1bfl = data[29][20::].flatten()
    s1bfr = data[30][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)

np.save('corrs_r_marciano_smoothed.npy', corrs_r)
np.save('corrs_r2_marciano_smoothed.npy', corrs_r2)


### marciano smoothed with GSR ###

subject_num = 23 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_new_sabina_data_smoothed_gsr" # 2.Change folder directory to your conn project folder

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
    accl = data[11][20::].flatten()
    s1bfl = data[29][20::].flatten()
    s1bfr = data[30][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)

np.save('corrs_r_marciano_smoothed_gsr.npy', corrs_r)
np.save('corrs_r2_marciano_smoothed_gsr.npy', corrs_r2)
"""
### marciano smoothed with GSR and 2500 TR ###

subject_num = 23 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_new_sabina_data_smoothed_gsr_2500_TR" # 2.Change folder directory to your conn project folder

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
    accl = data[11][20::].flatten()
    s1bfl = data[29][20::].flatten()
    s1bfr = data[30][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)

np.save('../corrs_r_marciano_smoothed_gsr_2500.npy', corrs_r)
np.save('../corrs_r2_marciano_smoothed_gsr_2500.npy', corrs_r2)