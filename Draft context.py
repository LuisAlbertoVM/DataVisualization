import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

fig, axes = plt.subplots(1,2)
axes[0].plot(x,y)
axes[1].plot(y,x)

plt.show()