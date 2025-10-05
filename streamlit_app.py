import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 E-commerce Sales Analytics Dashboard")

# Load dataset
df = pd.read_csv("data/ecommerce_sales_sample.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.month
df["AgeGroup"] = pd.cut(df["Customer Age"], bins=[18,25,35,50,70], labels=["18-25","26-35","36-50","51+"])

# --- Filters ---
category = st.selectbox("Select Category", df["Category"].unique())

# --- Filtered Data ---
filtered = df[df["Category"] == category]

st.subheader(f"Sales Breakdown for {category}")
st.write(filtered.groupby("Sub-Category")["Sales"].sum())

# --- Visualizations ---
st.subheader("Sales by Sub-Category")
fig, ax = plt.subplots()
sns.barplot(x="Sub-Category", y="Sales", data=filtered, estimator=sum, palette="viridis", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Monthly Sales Trend")
monthly = df.groupby("Month")["Sales"].sum()
fig, ax = plt.subplots()
sns.lineplot(x=monthly.index, y=monthly.values, marker="o", ax=ax)
st.pyplot(fig)

st.subheader("Sales by Age Group")
age_sales = df.groupby("AgeGroup")["Sales"].sum()
fig, ax = plt.subplots()
sns.barplot(x=age_sales.index, y=age_sales.values, palette="coolwarm", ax=ax)
st.pyplot(fig)
