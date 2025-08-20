import sqlite3
import pandas as pd

# Load dataset
df = pd.read_csv("data/SampleSuperstore.csv", parse_dates=["Order Date", "Ship Date"], encoding="latin1")

# Connect to SQLite
conn = sqlite3.connect("sales.db")

# Save dataframe into database
df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()
print("✅ Data loaded into SQLite successfully!")
