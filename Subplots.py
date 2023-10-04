import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

fig, axes = plt.subplots()
axes.plot(x,y,'b')
plt.show()

fig, axes = plt.subplots(nrows = 1, ncols=2)
#axes.plot(x,y,'b')