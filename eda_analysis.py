import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display dataset
print("=== Dataset ===")
print(df)

# Statistical Summary
print("\n=== Statistical Summary ===")
print(df.describe())

# Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum()

print("\n=== Total Sales by Category ===")
print(category_sales)

# Correlation
print("\n=== Correlation ===")
print(df[["Sales", "Profit"]].corr())

# Bar Chart
plt.figure(figsize=(6,4))
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()