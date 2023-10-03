import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.5,0.9])
axes.plot(x,y,'b')
plt.show()

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.9])
axes2 = fig.add_axes([0.2,0.55,0.4,0.3])
axes.plot(x,y,'b')
axes2.plot(y,x,'r')
axes2.set_facecolor('gray')
plt.show()