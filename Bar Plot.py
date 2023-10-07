import matplotlib.pyplot as plt
import numpy as np

country = ['India', 'Japan', 'Mexico', 'Colombia', 'Germany']
population = [1000, 800, 900, 1000, 300]

plt.bar(country, population, width=0.5, color = ['red', 'blue'])
plt.xticks(np.arange(5),('India', 'Japon', 'Mexico', 'Colombia', 'Alemania'),rotation = 45)
plt.show()

plt.barh(country, population)
plt.show()