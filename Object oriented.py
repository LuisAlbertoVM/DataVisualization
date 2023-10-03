import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.5,0.9])
axes.plot(x,y,'b')
plt.show()