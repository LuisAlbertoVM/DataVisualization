import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head(2))

print(tips.drop(columns=['sex','smoker','day','time']).corr())

sns.heatmap(tips.drop(columns=['sex','smoker','day','time']).corr(),annot=True,cmap='coolwarm',linewidths=5,linecolor='black',vmin=0,vmax=1,cbar=True)
plt.show()