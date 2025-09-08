import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import seaborn as sns


### MATLAB ###
subject_num = 30 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_schifer_all_rois"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:58]
    rois = file['names'][0][3:58]
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8, 6))
sns.heatmap(mean_matrix, cmap='jet', vmin=-1, vmax=1, square=True,
            cbar_kws={"shrink": .8}, fmt=".2f")

plt.xlabel('ROI')
plt.ylabel('ROI')


### MATLAB with GSR###

subject_num = 30 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_schifer_all_rois_gsr"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:58]
    rois = file['names'][0][3:58]
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8,6))
sns.heatmap(mean_matrix, cmap='jet', vmin=-1, vmax=1, square=True,
            cbar_kws={"shrink": .8}, fmt=".2f")

plt.xlabel('ROI')
plt.ylabel('ROI')
plt.show()

"""
### MATLAB MDMA ###

subject_num = 9 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_mdma_all_rois"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:58]
    rois = file['names'][0][3:58]
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8,6))
sns.heatmap(mean_matrix, cmap='turbo', vmin=-1, vmax=1, square=True,
            cbar_kws={"shrink": .8}, fmt=".2f")

plt.xlabel('ROI')
plt.ylabel('ROI')
plt.show()

### RABIES ###

subject_num = 21 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_rabies_all_rois_short"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:237]
    rois = file['names'][0][3:237]
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)


all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8,6))
sns.heatmap(mean_matrix, cmap='turbo', vmin=-1, vmax=1, square=True,
            cbar_kws={"shrink": .8}, fmt=".2f")

plt.xlabel('ROI')
plt.ylabel('ROI')
plt.show()


### unsmoothed ###

subject_num = 22 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_new_sabina_data_unsmoothed"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:58]
    rois = file['names'][0][3:58]
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8,6))
sns.heatmap(mean_matrix, cmap='turbo', vmin=-1, vmax=1, square=True,
            cbar_kws={"shrink": .8}, fmt=".2f")

plt.xlabel('ROI')
plt.ylabel('ROI')
plt.show()


### unsmoothed ###

subject_num = 23 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_new_sabina_data_smoothed"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:58]
    rois = file['names'][0][3:58]
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8,6))
sns.heatmap(mean_matrix, cmap='turbo', vmin=-1, vmax=1, square=True,
            cbar_kws={"shrink": .8}, fmt=".2f")

plt.xlabel('ROI')
plt.ylabel('ROI')
plt.show()
"""