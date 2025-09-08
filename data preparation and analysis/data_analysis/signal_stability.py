import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat


subject_num = 9 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_mdma_all_rois" # 2.Change folder directory to your conn project folder

subjects = np.arange(1, subject_num + 1)
corrs_r = []
corrs_r2 = []
mean_data_all = []
std_data_all = []

for i in subjects:
    if i < 10:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject00{i}_Condition001.mat"
    else:
        path = f"{path_to_folder}/results/preprocessing/ROI_Subject0{i}_Condition001.mat"
    file = loadmat(path)

    data = file['data'][0][3::]
    rois = file['names'][0][3::]
    for j, k in enumerate(rois):
        print(j, k)
    mean_data = np.mean(data, axis=0)[20::]
    std_data = np.std(data, axis=0)[20::].flatten()
    mean_data_all.append(mean_data)
    std_data_all.append(std_data)

    time = np.arange(len(mean_data))/30

    fig, ax = plt.subplots()
    ax.plot(time, mean_data, linewidth=0.8)
    ax.plot(time, std_data, color='grey', linewidth=0.8)
    ax.plot(time, -std_data, color='grey', linewidth=0.8)
    plt.fill_between(time, -std_data, std_data, color='grey', alpha=0.4, label='± Standard Deviation')
    ax.set_ylabel('% signal change')
    ax.set_xlabel('time [min]')
    #ax.legend()
    plt.show()

mean_mean_data = np.mean(mean_data_all, axis=0)
mean_std_data = np.mean(std_data_all, axis=0).flatten()

fig2, ax2 = plt.subplots()
ax2.plot(time, mean_mean_data, linewidth=0.8)
ax2.plot(time, mean_std_data, color = 'grey', linewidth=0.8)
ax2.plot(time, -mean_std_data,color = 'grey', linewidth=0.8)
plt.fill_between(time, -mean_std_data, mean_std_data, color = 'grey', alpha=0.4, label='± Standard Deviation')
ax2.set_ylabel('% signal change')
ax2.set_xlabel('time [min]')
#ax.legend()
plt.show()