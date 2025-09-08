import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import seaborn as sns


with open('D:/Uni/Master/Masterarbeit/matlab_conn/atlas_conn/SIGMA_ROIS_250_labels.txt', "r", encoding="utf-8") as f:
    labels = np.array([line.strip() for line in f])


### RABIES ###

subject_num = 1 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_rabies_roi_testing"

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

np.savetxt('roi_labels', rois, fmt="%s")

all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8, 6))
sns.heatmap(mean_matrix, cmap='jet', vmin=-1, vmax=1, square=True,
            cbar_kws={"shrink": .8}, fmt=".2f")

plt.xlabel('ROI')
plt.ylabel('ROI')
