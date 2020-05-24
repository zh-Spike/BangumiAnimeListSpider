import pandas as pd
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

df = pd.read_csv('Ex_Final.csv', nrows=50)
alt = array(df[['ranking', 'score_num', 'chinese_name']])

x0 = []
y0 = []
label = []
print(alt)
for a in alt:
    x0.append(a[0])
    y0.append(a[1])
    label.append(a[2])

x0, y0 = array(x0), array(y0)

fig, ax = plt.subplots()
ax.scatter(x0, y0, c='r')
n = np.arange(50)
for i, label in enumerate(n):
    ax.annotate(label, (x0[i], y0[i]))

plt.xlabel('Ranking')
plt.ylabel('Popularity')
plt.title('Rank&Popularity')
plt.show()
