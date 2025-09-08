import numpy as np
import glob
import os
import matplotlib.pyplot as plt
import nibabel as nib
from tqdm.auto import tqdm

folder = f"D:/Uni/Master/Masterarbeit/rabies/SaBu_prepro/conf_corr_done/default conf corr smoothing 0.3/recs"

nii_files = glob.glob(os.path.join(folder, '*.nii.gz'))

for i, file in enumerate(nii_files):
    print(f"Loading: {file}")
    img = nib.load(file)
    data = img.get_fdata()

    keep_volumes = 600  # Convert time to number of volumes
    trimmed_data = data[..., :keep_volumes]  # Keep only the first 'keep_volumes'

    # Save the new .nii file
    trimmed_img = nib.Nifti1Image(trimmed_data, img.affine, img.header)

    output_path = f"D:/Uni/Master/Masterarbeit/rabies/SaBu_prepro/conf_corr_done/default conf corr smoothing 0.3/recs/short/sub-{i+1}_bold_cleaned_0.3_short.nii"
    nib.save(trimmed_img, output_path)

    print(f"Trimmed fMRI scan saved as: {output_path}")

