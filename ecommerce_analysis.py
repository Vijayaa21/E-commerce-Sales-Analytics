import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ecommerce_sales_sample.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.month
df["Year"] = df["Order Date"].dt.year

# Age groups
df["AgeGroup"] = pd.cut(df["Customer Age"], bins=[18,25,35,50,70], labels=["18-25","26-35","36-50","51+"])

# --- Insights ---
print("\n✅ Top Categories by Sales:")
print(df.groupby("Category")["Sales"].sum())

print("\n✅ Monthly Sales Trend:")
print(df.groupby("Month")["Sales"].sum())

print("\n✅ Sales by Age Group:")
print(df.groupby("AgeGroup")["Sales"].sum())

# --- Visuals ---
sns.barplot(x="Category", y="Sales", data=df, estimator=sum, palette="viridis")
plt.title("Top Categories by Sales")
plt.savefig("assets/top_categories.png")
plt.show()

sns.lineplot(x="Month", y="Sales", data=df, estimator=sum, marker="o")
plt.title("Monthly Sales Trend")
plt.savefig("assets/monthly_sales.png")
plt.show()

sns.barplot(x="AgeGroup", y="Sales", data=df, estimator=sum, palette="coolwarm")
plt.title("Sales by Age Group")
plt.savefig("assets/age_sales.png")
plt.show()
