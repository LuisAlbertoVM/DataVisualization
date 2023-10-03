import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2
print(x)
print(y)

print()
plt.plot(x,y)
plt.plot(x,y,'bo')
plt.plot(x,y,'rx')
plt.plot(x,y,'rs-')
plt.plot(x,y,'yD:')
plt.show()

plt.hist(x)
plt.show()

plt.pie(x)
plt.show()

plt.scatter(x,y)
plt.show()

plt.boxplot(x)
plt.show()