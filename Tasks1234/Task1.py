import numpy as np
import glob
import os
import matplotlib.pyplot as plt

# 1. Paths
data_dir = '/dtu/projects/02613_2025/data/modified_swiss_dwellings/'
output_base = './figures/'

# Ensure base output folder exists
os.makedirs(output_base, exist_ok=True)

# 2. Select the first three floorplans (remove [:3] to process all)
domain_paths = sorted(glob.glob(os.path.join(data_dir, '*_domain.npy')))[:3]

# 3. Loop and save both figures into ID-specific subfolders
for dom_path in domain_paths:
    b_id = os.path.basename(dom_path).split('_')[0]
    out_dir = os.path.join(output_base, b_id)
    os.makedirs(out_dir, exist_ok=True)

    # Load arrays
    domain = np.load(dom_path)
    mask = np.load(os.path.join(data_dir, f'{b_id}_interior.npy'))

    # Save domain figure
    plt.figure(figsize=(6,6))
    im = plt.imshow(domain)
    plt.colorbar(im, label='°C')
    plt.title(f'Building {b_id} — Domain (°C)')
    plt.axis('off')
    plt.savefig(os.path.join(out_dir, 'domain.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # Save mask figure
    plt.figure(figsize=(6,6))
    plt.imshow(mask, cmap='gray', origin='lower')
    plt.title(f'Building {b_id} — Interior Mask')
    plt.axis('off')
    plt.savefig(os.path.join(out_dir, 'mask.png'), dpi=300, bbox_inches='tight')
    plt.close()

    print(f'Created folder {out_dir} with domain.png and mask.png')
