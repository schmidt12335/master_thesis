import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.ndimage import gaussian_filter1d
from scipy.interpolate import interp1d

subject_num = 2 # 1.Enter number of subjects here

path = f"F:/matlab_conn/project/conn_project_schifer_all_rois/results/preprocessing/ROI_Subject00{subject_num}_Condition001.mat" # 2.Change folder directory to your conn project folder

file = loadmat(path)

data = file['data'][0]
rois = file['names'][0]
for j, k in enumerate(rois):
    print(j, k)
accl = data[11][20::].flatten()
s1bfr = data[29][20::].flatten()
s1bfl = data[30][20::].flatten()

time = np.arange(len(s1bfl))/30


# Original signal
x = np.arange(len(s1bfl))
f_l = interp1d(x, s1bfl, kind='cubic')  # or 'quadratic', 'linear'
f_r = interp1d(x, s1bfr, kind='cubic')
f_a = interp1d(x, accl, kind='cubic')

# New denser x values
time_interpol = np.linspace(0, len(s1bfl) - 1, 10 * len(s1bfl))
s1bfl_interpol = f_l(time_interpol)
s1bfr_interpol = f_r(time_interpol)
accl_interpol = f_a(time_interpol)

frame_start_time = 0
frame_end_time = 1500

frame_start = 1000
frame_end = 2500

fig, ax = plt.subplots()
ax.plot(time_interpol[frame_start_time:frame_end_time], s1bfl_interpol[frame_start:frame_end], label = 'Seed (S1bfl)', c = 'deepskyblue')
ax.plot(time_interpol[frame_start_time:frame_end_time], s1bfr_interpol[frame_start:frame_end], label = 'Specific ROI (s1bfr)', c = 'royalblue')
ax.plot(time_interpol[frame_start_time:frame_end_time], accl_interpol[frame_start:frame_end], label = 'Non-specific ROI (ACA)', c = 'palevioletred')
ax.set_ylabel('Bold Signal (a.u.)', fontsize = 13)
ax.set_xlabel('time (s)', fontsize = 13)
ax.set_ylim([-1, 1])
ax.set_xlim([0, 150])
ax.set_xticks(np.arange(0,151, 25))
ax.legend(fontsize='11', loc='upper right', frameon=False, labelspacing = 0.2, handlelength = 0.8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('D:/Uni/Master/Masterarbeit/figures/thesis figures/bold_signal_example.png', dpi = 400, bbox_inches='tight')
plt.show()
