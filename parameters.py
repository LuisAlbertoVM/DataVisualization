import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips)

sns.displot(data=tips, x= 'total_bill')
plt.show()

sns.displot(data=tips, x= 'total_bill', y='tip')
plt.show()

sns.displot(data=tips, x= 'total_bill', y='tip', hue='sex')
plt.show()