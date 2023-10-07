import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head(2))

sns.scatterplot(data=tips,x='total_bill',y='tip')
plt.show()