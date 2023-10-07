import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x=['A','B','C'], y=[1,3,2])
plt.show()

sns.set(style='darkgrid',palette='muted', font='Verdana', font_scale=1)
sns.barplot(x=['A','B','C'], y=[1,3,2])
plt.show()