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
plt.show()

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols=2)
ax1.plot(x,y,'b')
ax2.plot(y,x,'b')
plt.show()

fig, axes = plt.subplots(2,4)
axes[0,0].plot(x,np.cos(x))
axes[0,1].plot(x,np.sin(x), 'r')
axes[0,2].plot(x,np.tan(x), 'y')
axes[0,3].plot(x,np.cos(x)**2)
plt.show()

fig, ((ax1, ax2, ax3, ax4),(ax5, ax6, ax7, ax8)) = plt.subplots(2,4)
ax1.plot(x,np.cos(x))
ax2.plot(x,np.sin(x), 'r')
ax3.plot(x,np.tan(x), 'y')
ax4.plot(x,np.cos(x)**2)
fig.tight_layout()
plt.show()