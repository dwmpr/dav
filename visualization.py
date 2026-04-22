import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset 
tips = sns.load_dataset("tips")

# 1. Bar Chart: Average Bill by Day 
plt.figure(figsize=(8, 5))
sns.barplot(x='day', y='total_bill', data=tips)
plt.title("Average Total Bill per Day")
plt.show()

# 2. Scatter Plot: Total Bill vs Tip 
plt.figure(figsize=(8, 5))
sns.scatterplot(x='total_bill', y='tip', hue='time', data=tips)
plt.title("Total Bill vs Tip (Color by Time)")
plt.show()