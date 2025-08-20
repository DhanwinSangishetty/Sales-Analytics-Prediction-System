import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")

def run_query(query):
    return pd.read_sql_query(query, conn)

# Example queries
queries = {
    "sales_by_region": """
        SELECT Region, SUM(Sales) AS Total_Sales
        FROM sales
        GROUP BY Region;
    """,
    "top_customers": """
        SELECT [Customer Name], SUM(Sales) AS Revenue
        FROM sales
        GROUP BY [Customer Name]
        ORDER BY Revenue DESC
        LIMIT 10;
    """,
    "avg_profit_category": """
        SELECT Category, AVG(Profit) AS Avg_Profit
        FROM sales
        GROUP BY Category;
    """,
    "monthly_sales": """
        SELECT strftime('%Y-%m', "Order Date") AS Month,
            SUM(Sales) AS Total_Sales,
            SUM(Profit) AS Total_Profit,
            COUNT(*) AS Orders
        FROM sales
        GROUP BY strftime('%Y-%m', "Order Date")
        ORDER BY Month;
    """,
    "negative_profit_products": """
        SELECT [Product Name], SUM(Profit) AS Total_Profit
        FROM sales
        GROUP BY [Product Name]
        HAVING Total_Profit < 0;
    """,
    "query_quarter" : """
    SELECT 
        strftime('%Y', "Order Date") || '-Q' || 
        CAST(((CAST(strftime('%m', "Order Date") AS INTEGER) - 1) / 3 + 1) AS TEXT) AS Quarter,
        SUM(Sales) AS Total_Sales,
        SUM(Profit) AS Total_Profit,
        COUNT(*) AS Orders
    FROM sales
    GROUP BY strftime('%Y', "Order Date"), 
             ((CAST(strftime('%m', "Order Date") AS INTEGER) - 1) / 3 + 1)
    ORDER BY strftime('%Y', "Order Date"), 
             ((CAST(strftime('%m', "Order Date") AS INTEGER) - 1) / 3 + 1);
    """,

    "query_year" : """
    SELECT strftime('%Y', "Order Date") AS Year,
        SUM(Sales) AS Total_Sales,
        SUM(Profit) AS Total_Profit,
        COUNT(*) AS Orders
    FROM sales
    GROUP BY strftime('%Y', "Order Date")
    ORDER BY Year;
    """


}

# Run and save all queries
for name, query in queries.items():
    df = run_query(query)
    df.to_excel(f"{name}.xlsx", index=False)
    print(f"✅ Query result saved: {name}.xlsx")

conn.close()
