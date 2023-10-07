import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
print(plt.style.available)
plt.style.use('dark_background')
print("Plot as Matlab")
fig, axes = plt.subplots(figsize=(8,8))
axes.plot(x,x+1,'r--')
axes.plot(x,x+2,'b-')
axes.plot(x,x+3,'y.-')
axes.plot(x,x+4,'gx:')
plt.show()
print("Plot as Pyplot")
fig, axes = plt.subplots(figsize=(8,8))
axes.plot(x,x+1,color = 'green', alpha = 0.1, linewidth = 5, linestyle = '-')
axes.plot(x,x+2,color = 'blue', linewidth = 8, linestyle = '--')
axes.plot(x,x+3,color = '#66FF66', linewidth = 3, linestyle = 'dashed')
axes.plot(x,x+4,color = '#CCFFCC', linewidth = 2, linestyle = ':')
plt.show()