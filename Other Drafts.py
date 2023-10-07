import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1, 50, 100)

print('Histogram')
plt.hist(data, bins=10,histtype='bar')
plt.show()

print('Boxplot')
data = np.append(data,200)
plt.boxplot(data, vert= False, patch_artist = True,notch=True, showfliers = True)
plt.show()

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
area = (30 * np.random.rand(N)) ** 2
colors = np.random.rand(N)

plt.scatter(x,y, s=area, c = colors, marker='o', alpha=0.5)
plt.show()