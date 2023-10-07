import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1, 50, 100)

print('Histogram')
plt.hist(data, bins=10,histtype='bar')
plt.show()

plt.hist(data, bins=10,histtype='step')
plt.show()