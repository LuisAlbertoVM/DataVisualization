import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head(2))

sns.jointplot(data=tips,x='total_bill',y='tip',hue='sex',kind='hist',marginal_ticks=True,marginal_kws=dict(bins=25,fill=False,multiple='dodge'))
plt.show()

sns.pairplot(data=tips, hue='sex',palette='coolwarm',corner=True)
plt.show()