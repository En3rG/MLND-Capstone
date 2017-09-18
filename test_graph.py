import matplotlib.pyplot as plt
from numpy.random import random
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd


df = pd.DataFrame.from_csv("training_data/all_processed_data.csv")

x1 = df["Open_pc"].where(df["Close_pc"] > 1)
x1 = x1.dropna(axis=0, how='all')

y1 = df["High_pc"].where(df["Close_pc"] > 1)
y1 = y1.dropna(axis=0, how='all')

z1 = df["Low_pc"].where(df["Close_pc"] > 1)
z1 = z1.dropna(axis=0, how='all')

x0 = df["Open_pc"].where(df["Close_pc"] < 1)
x0 = x0.dropna(axis=0, how='all')

y0 = df["High_pc"].where(df["Close_pc"] < 1)
y0 = y0.dropna(axis=0, how='all')

z0 = df["Low_pc"].where(df["Close_pc"] < 1)
z0 = z0.dropna(axis=0, how='all')

colors=['b', 'r']

ax = plt.subplot(111, projection='3d')

ax.plot(x1, y1, z1, 'o', color=colors[0], label='Buy')
ax.plot(x0, y0, z0, 'o', color=colors[1], label='Sell')

ax.set_xlabel('Open')
ax.set_ylabel('High')
ax.set_zlabel('Low')

plt.legend(loc='upper left', numpoints=1, ncol=3, fontsize=8, bbox_to_anchor=(0, 0))
plt.savefig("test.svg", format='svg', dpi=1200)
plt.show()
