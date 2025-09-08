import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from matplotlib.gridspec import GridSpec
from IPython import embed
from cycler import cycler


colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
colors[7] = 'lightskyblue'
colors[5] = 'mediumseagreen'
plt.rcParams['axes.prop_cycle'] = cycler(color=colors)

fig, ax = plt.subplots()

for i in range(8):
    ax.hlines(y = i, xmin = 0, xmax = 8, colors = colors[i], linewidth = 15)
plt.show()
