import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head(2))

plt.figure(figsize=(8,6))
sns.scatterplot(data=tips,x='total_bill',y='tip', hue='day',style='time',size='size')
plt.legend(loc='center',bbox_to_anchor=(1.12,0.5))
plt.show()

plt.figure(figsize=(8,6))
markers = {"Lunch":"D","Dinner":"s"}
sns.scatterplot(data=tips,x='total_bill',y='tip', hue='day',style='time',size='size',markers=markers)
plt.legend(loc='center',bbox_to_anchor=(1.12,0.5))
plt.show()