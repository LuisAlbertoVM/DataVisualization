import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips)

sns.histplot(tips, x='tip', bins = 15, cumulative=False, hue='sex', stat='count', multiple='dodge')
plt.show()