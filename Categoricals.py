import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head(2))

sns.countplot(data=tips,y='day',hue='sex')
plt.show()

sns.stripplot(data=tips,x='day',y='total_bill',hue='sex',dodge=True)
plt.show()