import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
print(plt.style.available)
plt.style.use('dark_background')
fig, axes = plt.subplots(figsize=(8,8))
axes.plot(x,x+1,'r')
plt.show()