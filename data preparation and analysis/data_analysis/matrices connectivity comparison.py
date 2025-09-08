import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import seaborn as sns

x_y_tick_labelsize = 13


### MATLAB ###
subject_num = 30 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_schifer_all_rois"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:61]
    rois = file['names'][0][3:61]
    remove = [44, 45, 46, 47, 52, 53, 55]
    data = np.delete(data, remove)
    rois = np.delete(rois, remove)
    rois[-1] = '[RSPXROIS.Medulla (Med)]' # Rename because it's not propperly named.
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

roi_labels = np.array([str(item).split('(')[-1].split(')')[0] for item in rois.flatten()])
all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8, 7))
ax = sns.heatmap(mean_matrix, xticklabels=roi_labels, yticklabels=roi_labels, cmap='jet', vmin=-1, vmax=1, square=True,
                 cbar_kws={"shrink": .8}, fmt=".2f")
ax.tick_params(axis='both', labelsize=x_y_tick_labelsize, length=0)

every_n = 2
ax.set_xticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_xticklabels(roi_labels[::every_n], rotation=90)
ax.set_yticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_yticklabels(roi_labels[::every_n])

cbar = ax.collections[0].colorbar
cbar.set_ticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # choose your own tick positions
cbar.set_ticklabels([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # custom labels
cbar.ax.tick_params(labelsize=10, rotation=90, length=0)
cbar.set_label("Pearsons's r", rotation=90, labelpad=10)
for label in cbar.ax.get_yticklabels():
    label.set_verticalalignment('center')
plt.tight_layout()
plt.xlabel('ROI', fontsize=x_y_tick_labelsize)
plt.ylabel('ROI', fontsize=x_y_tick_labelsize)
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/Haas matlab.png', dpi = 400, bbox_inches='tight')

### MATLAB with GSR###

subject_num = 30 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_schifer_all_rois_gsr"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:61]
    rois = file['names'][0][3:61]
    remove = [44, 45, 46, 47, 52, 53, 55]
    data = np.delete(data, remove)
    rois = np.delete(rois, remove)
    rois[-1] = '[RSPXROIS.Medulla (Med)]' # Rename because it's not propperly named.
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

roi_labels = np.array([str(item).split('(')[-1].split(')')[0] for item in rois.flatten()])
all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8, 7))
ax = sns.heatmap(mean_matrix, xticklabels=roi_labels, yticklabels=roi_labels, cmap='jet', vmin=-1, vmax=1, square=True,
                 cbar_kws={"shrink": .8}, fmt=".2f")
ax.tick_params(axis='both', labelsize=x_y_tick_labelsize, length=0)

every_n = 2
ax.set_xticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_xticklabels(roi_labels[::every_n], rotation=90)
ax.set_yticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_yticklabels(roi_labels[::every_n])

cbar = ax.collections[0].colorbar
cbar.set_ticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # choose your own tick positions
cbar.set_ticklabels([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # custom labels
cbar.ax.tick_params(labelsize=10, rotation=90, length=0)
cbar.set_label("Pearsons's r", rotation=90, labelpad=10)
for label in cbar.ax.get_yticklabels():
    label.set_verticalalignment('center')
plt.tight_layout()
plt.xlabel('ROI', fontsize = x_y_tick_labelsize)
plt.ylabel('ROI', fontsize = x_y_tick_labelsize)
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/Haas matlab GSR.png', dpi = 400, bbox_inches='tight')

plt.show()

### MATLAB MDMA ###

subject_num = 9 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_mdma_all_rois"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:61]
    rois = file['names'][0][3:61]
    remove = [44, 45, 46, 47, 52, 53, 55]
    data = np.delete(data, remove)
    rois = np.delete(rois, remove)
    rois[-1] = '[RSPXROIS.Medulla (Med)]' # Rename because it's not propperly named.
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

roi_labels = np.array([str(item).split('(')[-1].split(')')[0] for item in rois.flatten()])
all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8, 7))
ax = sns.heatmap(mean_matrix, xticklabels=roi_labels, yticklabels=roi_labels, cmap='jet', vmin=-1, vmax=1, square=True,
                 cbar_kws={"shrink": .8}, fmt=".2f")
ax.tick_params(axis='both', labelsize=x_y_tick_labelsize, length=0)

every_n = 2
ax.set_xticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_xticklabels(roi_labels[::every_n], rotation=90)
ax.set_yticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_yticklabels(roi_labels[::every_n])

cbar = ax.collections[0].colorbar
cbar.set_ticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # choose your own tick positions
cbar.set_ticklabels([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # custom labels
cbar.ax.tick_params(labelsize=10, rotation=90, length=0)
cbar.set_label("Pearsons's r", rotation=90, labelpad=10)
for label in cbar.ax.get_yticklabels():
    label.set_verticalalignment('center')
plt.tight_layout()
plt.xlabel('ROI', fontsize = x_y_tick_labelsize)
plt.ylabel('ROI', fontsize = x_y_tick_labelsize)
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/MDMA.png', dpi = 400, bbox_inches='tight')


### MATLAB MDMA with GSR ###

subject_num = 9 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_mdma_all_rois_gsr"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)


    data = file['data'][0][3:61]
    rois = file['names'][0][3:61]
    remove = [44, 45, 46, 47, 52, 53, 55]
    data = np.delete(data, remove)
    rois = np.delete(rois, remove)
    rois[-1] = '[RSPXROIS.Medulla (Med)]' # Rename because it's not propperly named.
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

roi_labels = np.array([str(item).split('(')[-1].split(')')[0] for item in rois.flatten()])
all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8, 7))
ax = sns.heatmap(mean_matrix, xticklabels=roi_labels, yticklabels=roi_labels, cmap='jet', vmin=-1, vmax=1, square=True,
                 cbar_kws={"shrink": .8}, fmt=".2f")
ax.tick_params(axis='both', labelsize=x_y_tick_labelsize, length=0)

every_n = 2
ax.set_xticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_xticklabels(roi_labels[::every_n], rotation=90)
ax.set_yticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_yticklabels(roi_labels[::every_n])

cbar = ax.collections[0].colorbar
cbar.set_ticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # choose tick positions
cbar.set_ticklabels([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # custom labels
cbar.ax.tick_params(labelsize=10, rotation=90, length=0)
cbar.set_label("Pearsons's r", rotation=90, labelpad=10)
for label in cbar.ax.get_yticklabels():
    label.set_verticalalignment('center')
plt.tight_layout()
plt.xlabel('ROI', fontsize = x_y_tick_labelsize)
plt.ylabel('ROI', fontsize = x_y_tick_labelsize)
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/MDMA GSR.png', dpi = 400, bbox_inches='tight')

"""
### RABIES ###

subject_num = 18 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_rabies_all_rois_smoothed_0.5"

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

plt.figure(figsize=(8, 7))
ax = sns.heatmap(mean_matrix, cmap='jet', vmin=-1, vmax=1, square=True,
                 cbar_kws={"shrink": .8}, fmt=".2f")
ax.tick_params(axis='both', labelsize=x_y_tick_labelsize, length=0)

every_n = 8
ax.set_xticks(np.arange(0, len(rois), every_n) + 0.5)
ax.set_xticklabels(np.arange(0, len(rois), every_n), rotation=90)
ax.set_yticks(np.arange(0, len(rois), every_n) + 0.5)
ax.set_yticklabels(np.arange(0, len(rois), every_n))

cbar = ax.collections[0].colorbar
cbar.set_ticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # choose tick positions
cbar.set_ticklabels([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # custom labels
cbar.ax.tick_params(labelsize=10, rotation=90, length=0)
cbar.set_label("Pearsons's r", rotation=90, labelpad=10)
for label in cbar.ax.get_yticklabels():
    label.set_verticalalignment('center')
plt.tight_layout()
plt.xlabel('ROI', fontsize = x_y_tick_labelsize, labelpad= 10)
plt.ylabel('ROI', fontsize = x_y_tick_labelsize, labelpad= 10)
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/Matrix AC RABIES.png', dpi = 400, bbox_inches='tight')


### RABIES with GSR ###

subject_num = 18 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_rabies_all_rois_smoothed_0.5_gsr"

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

plt.figure(figsize=(8, 7))
ax = sns.heatmap(mean_matrix, cmap='jet', vmin=-1, vmax=1, square=True,
                 cbar_kws={"shrink": .8}, fmt=".2f")
ax.tick_params(axis='both', labelsize=x_y_tick_labelsize, length=0)

every_n = 8
ax.set_xticks(np.arange(0, len(rois), every_n) + 0.5)
ax.set_xticklabels(np.arange(0, len(rois), every_n), rotation=90)
ax.set_yticks(np.arange(0, len(rois), every_n) + 0.5)
ax.set_yticklabels(np.arange(0, len(rois), every_n))

cbar = ax.collections[0].colorbar
cbar.set_ticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # choose tick positions
cbar.set_ticklabels([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # custom labels
cbar.ax.tick_params(labelsize=10, rotation=90, length=0)
cbar.set_label("Pearsons's r", rotation=90, labelpad=10)
for label in cbar.ax.get_yticklabels():
    label.set_verticalalignment('center')
plt.tight_layout()
plt.xlabel('ROI', fontsize=x_y_tick_labelsize, labelpad=10)
plt.ylabel('ROI', fontsize=x_y_tick_labelsize, labelpad=10)
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/Matrix AC RABIES GSR.png', dpi = 400, bbox_inches='tight')
plt.show()

"""
### unsmoothed ###

subject_num = 22 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_new_sabina_data_unsmoothed"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:61]
    rois = file['names'][0][3:61]
    remove = [44, 45, 46, 47, 52, 53, 55]
    data = np.delete(data, remove)
    rois = np.delete(rois, remove)
    rois[-1] = '[RSPXROIS.Medulla (Med)]' # Rename because it's not propperly named.
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

roi_labels = np.array([str(item).split('(')[-1].split(')')[0] for item in rois.flatten()])
all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8, 7))
ax = sns.heatmap(mean_matrix, xticklabels=roi_labels, yticklabels=roi_labels, cmap='jet', vmin=-1, vmax=1, square=True,
                 cbar_kws={"shrink": .8}, fmt=".2f")
ax.tick_params(axis='both', labelsize=x_y_tick_labelsize, length=0)

every_n = 2
ax.set_xticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_xticklabels(roi_labels[::every_n], rotation=90)
ax.set_yticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_yticklabels(roi_labels[::every_n])

cbar = ax.collections[0].colorbar
cbar.set_ticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # choose your own tick positions
cbar.set_ticklabels([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # custom labels
cbar.ax.tick_params(labelsize=10, rotation=90, length=0)
cbar.set_label("Pearsons's r", rotation=90, labelpad=10)
for label in cbar.ax.get_yticklabels():
    label.set_verticalalignment('center')
plt.tight_layout()
plt.xlabel('ROI')
plt.ylabel('ROI')
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/Marciano unsmoothed.png', dpi = 400, bbox_inches='tight')


### unsmoothed with GSR ###

subject_num = 22 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_new_sabina_data_unsmoothed_gsr"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:61]
    rois = file['names'][0][3:61]
    remove = [44, 45, 46, 47, 52, 53, 55]
    data = np.delete(data, remove)
    rois = np.delete(rois, remove)
    rois[-1] = '[RSPXROIS.Medulla (Med)]' # Rename because it's not propperly named.
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

roi_labels = np.array([str(item).split('(')[-1].split(')')[0] for item in rois.flatten()])
all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8, 7))
ax = sns.heatmap(mean_matrix, xticklabels=roi_labels, yticklabels=roi_labels, cmap='jet', vmin=-1, vmax=1, square=True,
                 cbar_kws={"shrink": .8}, fmt=".2f")
ax.tick_params(axis='both', labelsize=x_y_tick_labelsize, length=0)

every_n = 2
ax.set_xticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_xticklabels(roi_labels[::every_n], rotation=90)
ax.set_yticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_yticklabels(roi_labels[::every_n])

cbar = ax.collections[0].colorbar
cbar.set_ticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # choose your own tick positions
cbar.set_ticklabels([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # custom labels
cbar.ax.tick_params(labelsize=10, rotation=90, length=0)
cbar.set_label("Pearsons's r", rotation=90, labelpad=10)
for label in cbar.ax.get_yticklabels():
    label.set_verticalalignment('center')
plt.tight_layout()
plt.xlabel('ROI')
plt.ylabel('ROI')
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/Marciano unsmoothed GSR.png', dpi = 400, bbox_inches='tight')


### smoothed ###

subject_num = 23 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_new_sabina_data_smoothed"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:61]
    rois = file['names'][0][3:61]
    remove = [44, 45, 46, 47, 52, 53, 55]
    data = np.delete(data, remove)
    rois = np.delete(rois, remove)
    rois[-1] = '[RSPXROIS.Medulla (Med)]' # Rename because it's not propperly named.
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

roi_labels = np.array([str(item).split('(')[-1].split(')')[0] for item in rois.flatten()])
all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8, 7))
ax = sns.heatmap(mean_matrix, xticklabels=roi_labels, yticklabels=roi_labels, cmap='jet', vmin=-1, vmax=1, square=True,
                 cbar_kws={"shrink": .8}, fmt=".2f")
ax.tick_params(axis='both', labelsize=x_y_tick_labelsize, length=0)

every_n = 2
ax.set_xticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_xticklabels(roi_labels[::every_n], rotation=90)
ax.set_yticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_yticklabels(roi_labels[::every_n])

cbar = ax.collections[0].colorbar
cbar.set_ticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # choose your own tick positions
cbar.set_ticklabels([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # custom labels
cbar.ax.tick_params(labelsize=10, rotation=90, length=0)
cbar.set_label("Pearsons's r", rotation=90, labelpad=10)
for label in cbar.ax.get_yticklabels():
    label.set_verticalalignment('center')
plt.tight_layout()
plt.xlabel('ROI', fontsize = x_y_tick_labelsize)
plt.ylabel('ROI', fontsize = x_y_tick_labelsize)
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/Marciano smoothed.png', dpi = 400, bbox_inches='tight')


### smoothed with GSR ###

subject_num = 23 # 1.Enter number of subjects here

path_to_folder = "F:/matlab_conn/project/conn_project_new_sabina_data_smoothed_gsr"

subjects = np.arange(1, subject_num + 1)
all_matrices = []
for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3:61]
    rois = file['names'][0][3:61]
    remove = [44, 45, 46, 47, 52, 53, 55]
    data = np.delete(data, remove)
    rois = np.delete(rois, remove)
    rois[-1] = '[RSPXROIS.Medulla (Med)]' # Rename because it's not propperly named.
    data_reform = np.hstack([roi for roi in data])

    conn_matrix = np.corrcoef(data_reform.T)
    all_matrices.append(conn_matrix)

roi_labels = np.array([str(item).split('(')[-1].split(')')[0] for item in rois.flatten()])
all_matrices = np.stack(all_matrices)
mean_matrix = np.nanmean(all_matrices, axis=0)

plt.figure(figsize=(8, 7))
ax = sns.heatmap(mean_matrix, xticklabels=roi_labels, yticklabels=roi_labels, cmap='jet', vmin=-1, vmax=1, square=True,
                 cbar_kws={"shrink": .8}, fmt=".2f")
ax.tick_params(axis='both', labelsize=x_y_tick_labelsize, length=0)

every_n = 2
ax.set_xticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_xticklabels(roi_labels[::every_n], rotation=90)
ax.set_yticks(np.arange(0, len(roi_labels), every_n) + 0.5)
ax.set_yticklabels(roi_labels[::every_n])

cbar = ax.collections[0].colorbar
cbar.set_ticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # choose your own tick positions
cbar.set_ticklabels([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])  # custom labels
cbar.ax.tick_params(labelsize=10, rotation=90, length=0)
cbar.set_label("Pearsons's r", rotation=90, labelpad=10)
for label in cbar.ax.get_yticklabels():
    label.set_verticalalignment('center')
plt.tight_layout()
plt.xlabel('ROI', fontsize = x_y_tick_labelsize)
plt.ylabel('ROI', fontsize = x_y_tick_labelsize)
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/Marciano smoothed GSR.png', dpi = 400, bbox_inches='tight')

plt.show()
"""