import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

fig, axes = plt.subplots(1,2)
axes[0].plot(x,y)
axes[0].set_title('Relation X-Y')
axes[1].plot(y,x)
axes[1].set_title('Relation Y-X')
plt.show()