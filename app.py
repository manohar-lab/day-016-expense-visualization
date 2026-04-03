import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("expenses.csv")

# Group data
category_sum = df.groupby("category")["amount"].sum()

print("Category-wise Spending:")
print(category_sum)


# 🔹 BAR CHART
plt.figure()
category_sum.plot(kind="bar")
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()


# 🔹 PIE CHART
plt.figure()
category_sum.plot(kind="pie", autopct="%1.1f%%")
plt.title("Expense Distribution")
plt.ylabel("")
plt.show()