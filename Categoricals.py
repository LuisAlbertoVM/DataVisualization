import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head(2))

sns.countplot(data=tips,x='day',hue='sex')
plt.show()