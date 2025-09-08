import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from tqdm import tqdm, trange

subs = np.arange(2,8)

for i in tqdm(subs):

    file_path = f"E:/fMRI/Old_Pipeline/WorkingDirectory/GFP_Rat_00{i}/rp_FUNC.txt"
    data = np.loadtxt(file_path)

    keep_volumes = 600  # Convert time to number of volumes
    trimmed_data = data[:keep_volumes]  # Keep only the first 'keep_volumes'

    output_path = f"E:/fMRI/Old_Pipeline/WorkingDirectory/cut/cut_rp/00{i}_GFP_rp_FUNC.txt"


    np.savetxt(output_path, trimmed_data)

    print(f"Trimmed rp saved as: {output_path}")
