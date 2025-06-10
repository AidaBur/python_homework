import pandas as pd
import sqlite3

# Connect to the database and define SQL query
with sqlite3.connect("../db/lesson.db") as conn:
    sql = """
    SELECT 
        li.line_item_id,
        li.quantity,
        p.product_id,
        p.product_name,
        p.price
    FROM line_items li
    JOIN products p ON li.product_id = p.product_id
    """

    # Read into DataFrame
    df = pd.read_sql_query(sql, conn)
    print("Data loaded from database:")
    print(df.head())

    # Add 'total' column
    df['total'] = df['quantity'] * df['price']
    print("\n Data with 'total' column:")
    print(df.head())

    # Group by product and summarize
    summary = df.groupby('product_id').agg({
        'line_item_id': 'count',
        'total': 'sum',
        'product_name': 'first'
    })

    # Sort by product name
    summary = summary.sort_values(by='product_name')
    print("\n Grouped summary:")
    print(summary.head())

    # Export to CSV
    summary.to_csv("order_summary.csv")
    print("\n order_summary.csv written successfully.")
