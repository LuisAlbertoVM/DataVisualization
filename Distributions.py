import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips)

sns.histplot(tips, x='tip', bins = 15, cumulative=False, hue='sex', stat='count', multiple='dodge')
plt.show()

sns.kdeplot(data=tips, x='tip', hue='sex', cumulative=False,shade='True',bw_adjust=1)
plt.show()

sns.ecdfplot(data=tips, x='tip', hue='sex',stat='count')
plt.show()

sns.displot(data=tips, x='tip', hue='sex',kind='kde',multiple='stack')
plt.show()