import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from tqdm import tqdm, trange

subjects = np.arange(1, 19)

for i in tqdm(subjects):
    if i < 10:
        filename = f'00{i}rp_FUNC.txt'
    else:
        filename = f'0{i}rp_FUNC.txt'

    file_path = f"E:/matlab_conn/data/ChR/{filename}"
    data = np.loadtxt(file_path)

    keep_volumes = 600  # Convert time to number of volumes
    trimmed_data = data[:keep_volumes]  # Keep only the first 'keep_volumes'

    if i < 10:
        output_path = f"E:/matlab_conn/data/ChR/00{i}rp_FUNC_short.txt"
    else:
        output_path = f"E:/matlab_conn/data/ChR/0{i}rp_FUNC_short.txt"

    np.savetxt(output_path, trimmed_data)

    print(f"Trimmed rp saved as: {output_path}")
