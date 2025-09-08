import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat


subject_num = 30 # 1.Enter number of subjects here

path_to_folder = "E:/matlab_conn/project/conn_project_schifer_three_rois" # 2.Change folder directory to your conn project folder

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

    s1bfr = data[3][20::].flatten()
    accl  = data[4][20::].flatten()
    s1bfl = data[5][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)

x_rect = [0.5, 0.5, 0.1, 0.1, 0.5]
y_rect = [-0.5, 0.1, 0.1, -0.5, -0.5]

fig2, ax2 = plt.subplots()
ax2.plot(corrs_r, corrs_r2, linestyle='', marker = 'o')
ax2.axhline(0.1)
ax2.axvline(0.1)
ax2.fill(x_rect, y_rect, color = 'green', alpha = 0.3)
ax2.set_ylabel('Corr S1BFl - Accl')
ax2.set_xlabel('Corr S1BFl - S1BFr')
ax2.set_title('matlab')

good_r = []
for i in range(len(corrs_r)):
    if corrs_r[i] > 0.1 and corrs_r2[i] < 0.1:
        good_r.append(i)
print(f'for matlab, {len(good_r)} good animals out of {len(corrs_r)}')

plt.show()

