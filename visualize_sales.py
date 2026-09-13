import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 100

# -----------------------------------------------------
# STEP 1: Load the dataset
# -----------------------------------------------------
df = pd.read_csv("sales_data.csv")
print("Dataset loaded successfully.")
print(f"Shape: {df.shape}")
print(df.head())

# -----------------------------------------------------
# STEP 2: Chart 1 - Monthly sales trend (Line chart)
# Question: Is overall sales growing over time?
# -----------------------------------------------------
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales["Month"], monthly_sales["Sales"], marker="o", color="#2E86AB")
plt.title("Monthly Sales Trend (2024-2025)", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart1_monthly_sales_trend.png")
plt.close()

# -----------------------------------------------------
# STEP 3: Chart 2 - Sales by category (Bar chart)
# Question: Which product category sells the most?
# -----------------------------------------------------
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=category_sales.index, y=category_sales.values, hue=category_sales.index,
            palette="viridis", legend=False)
plt.title("Total Sales by Product Category", fontsize=14, fontweight="bold")
plt.xlabel("Category")
plt.ylabel("Total Sales (₹)")
plt.tight_layout()
plt.savefig("chart2_sales_by_category.png")
plt.close()

# -----------------------------------------------------
# STEP 4: Chart 3 - Sales share by region (Pie chart)
# Question: Which region contributes most to sales?
# -----------------------------------------------------
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(6, 6))
plt.pie(region_sales.values, labels=region_sales.index, autopct="%1.1f%%",
        colors=sns.color_palette("pastel"), startangle=90)
plt.title("Sales Share by Region", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("chart3_sales_share_by_region.png")
plt.close()

# -----------------------------------------------------
# STEP 5: Chart 4 - Profit vs Sales relationship (Scatter plot)
# Question: Does higher sales always mean higher profit?
# -----------------------------------------------------
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="Sales", y="Profit", hue="Category", alpha=0.7)
plt.title("Profit vs Sales (by Category)", fontsize=14, fontweight="bold")
plt.xlabel("Sales (₹)")
plt.ylabel("Profit (₹)")
plt.tight_layout()
plt.savefig("chart4_profit_vs_sales.png")
plt.close()

# -----------------------------------------------------
# STEP 6: Chart 5 - Category performance across regions (Heatmap)
# Question: Which category-region combination performs best?
# -----------------------------------------------------
pivot = df.pivot_table(values="Sales", index="Category", columns="Region", aggfunc="sum")

plt.figure(figsize=(7, 5))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlOrRd")
plt.title("Total Sales: Category vs Region", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("chart5_category_region_heatmap.png")
plt.close()

# -----------------------------------------------------
# STEP 7: Combined Dashboard (multiple charts in one image)
# This tells the "full story" in a single view - useful for reports
# -----------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Sales Performance Dashboard", fontsize=18, fontweight="bold")

# Panel 1: Monthly trend
axes[0, 0].plot(monthly_sales["Month"], monthly_sales["Sales"], marker="o", color="#2E86AB")
axes[0, 0].set_title("Monthly Sales Trend")
axes[0, 0].tick_params(axis='x', rotation=45, labelsize=7)

# Panel 2: Category sales
sns.barplot(x=category_sales.index, y=category_sales.values, hue=category_sales.index,
            palette="viridis", legend=False, ax=axes[0, 1])
axes[0, 1].set_title("Sales by Category")
axes[0, 1].tick_params(axis='x', rotation=20)

# Panel 3: Region pie
axes[1, 0].pie(region_sales.values, labels=region_sales.index, autopct="%1.1f%%",
               colors=sns.color_palette("pastel"))
axes[1, 0].set_title("Sales Share by Region")

# Panel 4: Heatmap
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlOrRd", ax=axes[1, 1], cbar=False)
axes[1, 1].set_title("Category vs Region Sales")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("dashboard_sales_overview.png")
plt.close()

# -----------------------------------------------------
# STEP 8: Print key insights (the "data story")
# -----------------------------------------------------
best_category = category_sales.idxmax()
best_region = region_sales.idxmax()
growth_pct = ((monthly_sales["Sales"].iloc[-1] - monthly_sales["Sales"].iloc[0])
              / monthly_sales["Sales"].iloc[0]) * 100

print("\n--- KEY INSIGHTS ---")
print(f"Best-selling category: {best_category}")
print(f"Top-performing region: {best_region}")
print(f"Sales growth from first to last month: {growth_pct:.1f}%")

print("\nVisualization completed! 5 charts + 1 dashboard image saved in this folder.")
