import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head(2))

print(tips.drop(columns=['sex','smoker','day','time']).corr())

sns.heatmap(tips.drop(columns=['sex','smoker','day','time']).corr())
plt.show()