import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

fig, axes = plt.subplots()
axes.plot(x,y,'b')
plt.show()

fig, axes = plt.subplots(nrows = 1, ncols=2)
axes[0].plot(x,y,'b')
axes[1].plot(y,x,'b')

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols=2)
ax1.plot(x,y,'b')
ax2.plot(y,x,'b')