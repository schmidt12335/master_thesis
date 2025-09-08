import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Assume data is (timepoints, n_rois)
# Example fake data
timepoints = 300
n_rois = 10
data = np.random.randn(timepoints, n_rois)

# 1. Calculate the correlation matrix
conn_matrix = np.corrcoef(data.T)  # (n_rois, n_rois)

# 2. Plot it nicely
plt.figure(figsize=(8,6))
sns.heatmap(conn_matrix, cmap='coolwarm', vmin=-1, vmax=1, square=True,
            cbar_kws={"shrink": .8}, fmt=".2f")

plt.xlabel('ROI')
plt.ylabel('ROI')
plt.show()