import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from tqdm import tqdm, trange

subjects = np.arange(22,24)

for i in tqdm(subjects):
    if i < 10:
        filename = f'00{i}wrrrFUNC.nii'
    else:
        filename = f'0{i}wrrrFUNC.nii'

    file_path = f"F:/fMRI_rs_Sabina/before_smooth/{filename}"
    img = nib.load(file_path)
    data = img.get_fdata()

    keep_volumes = 600  # Convert time to number of volumes
    trimmed_data = data[..., :keep_volumes]  # Keep only the first 'keep_volumes'

    # Save the new .nii file
    trimmed_img = nib.Nifti1Image(trimmed_data, img.affine, img.header)
    if i < 10:
        output_path = f"F:/fMRI_rs_Sabina/before_smooth/short/00{i}wrrrFUNC_short.nii"
    else:
        output_path = f"F:/fMRI_rs_Sabina/before_smooth/short/0{i}wrrrFUNC_short.nii"

    nib.save(trimmed_img, output_path)

    print(f"Trimmed fMRI scan saved as: {output_path}")
