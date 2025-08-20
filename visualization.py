import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Seaborn style for professional-looking charts
sns.set_style("whitegrid")

# Connect to SQLite database
conn = sqlite3.connect("sales.db")

# ----------------------------
# Chart 1: Sales by Region (Bar Chart)
# ----------------------------
df_region = pd.read_sql_query("""
    SELECT Region, SUM(Sales) AS Total_Sales
    FROM sales
    GROUP BY Region;
""", conn)

plt.figure(figsize=(8, 5))
sns.barplot(data=df_region, x="Region", y="Total_Sales", palette="Blues_d")
plt.title("Total Sales by Region", fontsize=14)
plt.xlabel("Region", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.tight_layout()
plt.savefig("chart_sales_by_region.png", dpi=300)
plt.close()
print("✅ Chart saved: chart_sales_by_region.png")

# ----------------------------
# Chart 2: Monthly Sales Trend (Line Chart)
# ----------------------------
df_month = pd.read_sql_query("""
    SELECT strftime('%Y-%m', "Order Date") AS Month,
           SUM(Sales) AS Total_Sales
    FROM sales
    GROUP BY strftime('%Y-%m', "Order Date")
    ORDER BY Month;
""", conn)

plt.figure(figsize=(10, 5))
sns.lineplot(data=df_month, x="Month", y="Total_Sales", marker="o", color="green")
plt.title("Monthly Sales Trend", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("chart_monthly_sales.png", dpi=300)
plt.close()
print("✅ Chart saved: chart_monthly_sales.png")

# ----------------------------
# Chart 3: Quarterly Sales (Bar Chart)
# ----------------------------
df_quarter = pd.read_sql_query("""
    SELECT
        strftime('%Y', "Order Date") || '-Q' ||
        CAST(((CAST(strftime('%m', "Order Date") AS INTEGER) - 1) / 3 + 1) AS TEXT) AS Quarter,
        SUM(Sales) AS Total_Sales
    FROM sales
    GROUP BY strftime('%Y', "Order Date"),
             ((CAST(strftime('%m', "Order Date") AS INTEGER) - 1) / 3 + 1)
    ORDER BY strftime('%Y', "Order Date"),
             ((CAST(strftime('%m', "Order Date") AS INTEGER) - 1) / 3 + 1);
""", conn)

plt.figure(figsize=(10, 5))
sns.barplot(data=df_quarter, x="Quarter", y="Total_Sales", palette="Oranges_d")
plt.title("Total Sales by Quarter", fontsize=14)
plt.xlabel("Quarter", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("chart_quarterly_sales.png", dpi=300)
plt.close()
print("✅ Chart saved: chart_quarterly_sales.png")

# ----------------------------
# Chart 4: Yearly Sales (Bar Chart)
# ----------------------------
df_year = pd.read_sql_query("""
    SELECT strftime('%Y', "Order Date") AS Year,
           SUM(Sales) AS Total_Sales
    FROM sales
    GROUP BY strftime('%Y', "Order Date")
    ORDER BY Year;
""", conn)

plt.figure(figsize=(8, 5))
sns.barplot(data=df_year, x="Year", y="Total_Sales", palette="Purples_d")
plt.title("Total Sales by Year", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.tight_layout()
plt.savefig("chart_yearly_sales.png", dpi=300)
plt.close()
print("✅ Chart saved: chart_yearly_sales.png")

# Close database connection
conn.close()