import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import seaborn as sns

cons = ['b', 'c', 'ch', 'd', 'f']
N = len(cons)

ncmC1 = np.abs(np.identity(N) - np.random(0.0, 5, (N, N)) ** 2)

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(ncmC1, mask=ncmC1 > 0.5,
            cmap='Oranges', norm=colors.LogNorm(vmin=0.001, vmax=0.5), vmin=0.001, vmax=2.5,
            annot=True, fmt='.2f', annot_kws={"size": 6},
            xticklabels=[], yticklabels=[], ax=ax)
sns.heatmap(ncmC1, mask=ncmC1 <= 0.5,
            cmap='Blues', norm=colors.Normalize(vmin=0, vmax=1), vmin=2.5, vmax=5, cbar=False,
            annot=True, fmt='.2f', annot_kws={"size": 6},
            xticklabels=cons, yticklabels=cons, ax=ax)
plt.show()

#print(ncmC1)