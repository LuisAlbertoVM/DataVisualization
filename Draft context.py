import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

fig, axes = plt.subplots(1,2,figsize=(5,5))
axes[0].plot(x,y,label='$sin(x)$')
axes[0].set_title('Relation X-Y')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].legend()
axes[1].plot(y,x)
axes[1].set_title('Relation Y-X')
axes[1].set_xlabel('Y')
axes[1].set_ylabel('X')
plt.show()

# without object methods
plt.plot(x,y,label='$sin(x)$')
plt.title('This is the title')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='lower left', bbox_to_anchor=(0.5,0.9))
plt.show()