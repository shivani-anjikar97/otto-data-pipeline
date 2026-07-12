import sqlite3
import pandas as pd

DATABASE = "product_sales.db"

conn = sqlite3.connect(DATABASE)

with open("sql/revenue.sql") as f:
    conn.executescript(f.read())

conn.commit()

df = pd.read_sql("SELECT * FROM revenue", conn)
print(df)

conn.close()