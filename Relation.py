import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head(2))

sns.scatterplot(data=tips,x='total_bill',y='tip', hue='day',style='time',size='size')
plt.legend(loc='center',bbox_to_achor=(1.12,0,5))
plt.show()

