import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from matplotlib.gridspec import GridSpec
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

"""
### SaBu Rabies ###

subject_num = 16 # 1.Enter number of subjects here

path_to_folder = "E:/conn/conn_project_raclo_new_pipeline" # 2.Change folder directory to your conn project folder

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
    s1bfr = data[29][20::].flatten()
    s1bfl = data[30][20::].flatten()

    time = np.arange(len(s1bfl))/30

    r = np.corrcoef(s1bfl, s1bfr)[0, 1]
    r2 = np.corrcoef(s1bfl, accl)[0, 1]
    corrs_r.append(r)
    corrs_r2.append(r2)

np.save('corrs_r_raclo_new.npy', corrs_r)
np.save('corrs_r2_raclo_new.npy', corrs_r2)
"""


corrs_r_raclo_new = np.load('corrs_r_raclo_new.npy')
corrs_r2_raclo_new = np.load('corrs_r2_raclo_new.npy')

corrs_r_raclo_old = np.load('corrs_r_raclo_old.npy')
corrs_r2_raclo_old = np.load('corrs_r2_raclo_old.npy')

data_x_kde = [corrs_r_raclo_new, corrs_r_raclo_old]
data_y_kde = [corrs_r2_raclo_new, corrs_r2_raclo_old]
kdes_x = []
kdes_y = []

xmin = -1
xmax = 1
ymin = -1
ymax = 2
dx = 0.0005
x = np.arange(xmin, xmax, dx)
y = np.arange(ymin, ymax, dx)


for i in range(len(data_x_kde)):
    kernel = gaussian_kde(data_x_kde[i], bw_method = 0.6)
    gkde = kernel(x)
    kdes_x.append(gkde)

for i in range(len(data_y_kde)):
    kernel = gaussian_kde(data_y_kde[i], bw_method = 0.6)
    gkde = kernel(y)
    kdes_y.append(gkde)

fig = plt.figure(figsize = (7,6), tight_layout = True)
gs = GridSpec(2,2, figure = fig, height_ratios= [1,5], width_ratios = [5,1])

ax0 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])

for i in range(len(data_x_kde)):
    ax0.plot(x, kdes_x[i], alpha=0.5)
    ax0.fill_between(x, kdes_x[i], alpha = 0.2)

ax0.set_xlim([-0.2, 1])

for i in range(len(data_y_kde)):
    ax3.plot(kdes_y[i], y, alpha=0.5)
    ax3.fill_between(kdes_y[i], y, alpha = 0.2)

ax2.set_ylim([-0.7, 1])
ax3.set_ylim([-0.7, 1])

ax2.plot(corrs_r_raclo_new, corrs_r2_raclo_new, linestyle='', marker = 'o', label = 'Raclo New Pipeline')
ax2.plot(corrs_r_raclo_old, corrs_r2_raclo_old, linestyle='', marker = 'o', label = 'Raclo Old Pipeline')
ax2.set_xlabel('Correlation S1bf left to right (r)')
ax2.set_ylabel('Correlation S1bf left to ACA (r)')
ax2.set_xlim([-0.3, 1])
ax2.set_ylim([-0.7, 1])
ax2.legend(fontsize = 8, markerscale = 0.75, frameon = False, title = 'Dataset', title_fontsize = 9, labelspacing = 0.2, handlelength = 0, borderaxespad = 2, draggable = True)
ax2.hlines(y = 0.1, xmin=-0.1, xmax=0.8, linestyle='--', color='k')
ax2.vlines(x = 0.1, ymin=-0.4, ymax=0.8, linestyle='--', color='k')
ax2.hlines(y = -0.1, xmin=-0.1, xmax=0.1, linestyle='--', color='k')
ax2.vlines(x = -0.1, ymin=-0.1, ymax=0.1, linestyle='--', color='k')
ax2.set_xticks([-0.2, 0, 0.2, 0.4, 0.6, 0.8], labels = [-0.2, 0, 0.2, 0.4, 0.6, 0.8])
ax2.set_yticks([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], labels = [-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8])

ax0.axis('off')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax3.axis('off')

plt.show()