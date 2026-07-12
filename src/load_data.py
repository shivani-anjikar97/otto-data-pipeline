import sqlite3
import pandas as pd

DATABASE = "database.db"


def load_data():
    # Read CSV files
    product_df = pd.read_csv("data/product.csv")
    sales_df = pd.read_csv("data/sales.csv")

    # Create SQLite database
    conn = sqlite3.connect(DATABASE)

    # Load data into SQLite tables
    product_df.to_sql(
        "product",
        conn,
        if_exists="replace",
        index=False,
    )

    sales_df.to_sql(
        "sales",
        conn,
        if_exists="replace",
        index=False,
    )

    conn.close()

    print("Data loaded successfully!")


if __name__ == "__main__":
    load_data()