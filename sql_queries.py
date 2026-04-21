import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv('ecommerce.csv')
df['total_purchase'] = df['quantity'] * df['price']

# Create in-memory database
conn = sqlite3.connect(':memory:')
df.to_sql('purchases', conn, index=False)

# Task 1 - Display all purchase records
print("=== All Purchase Records (first 10) ===")
result1 = pd.read_sql("""
    SELECT customer_id, customer_name, city, product, quantity, price,
           (quantity * price) AS total_purchase
    FROM purchases
    ORDER BY customer_id
    LIMIT 10
""", conn)
print(result1)

# Task 2 - Total spending per customer
print("\n=== Total Spending per Customer (Top 10) ===")
result2 = pd.read_sql("""
    SELECT customer_name,
           SUM(quantity * price) AS total_spending
    FROM purchases
    GROUP BY customer_name
    ORDER BY total_spending DESC
    LIMIT 10
""", conn)
print(result2)

# Task 3 - Most purchased product
print("\n=== Most Purchased Product ===")
result3 = pd.read_sql("""
    SELECT product,
           SUM(quantity) AS total_units_sold,
           SUM(quantity * price) AS total_revenue
    FROM purchases
    GROUP BY product
    ORDER BY total_units_sold DESC
""", conn)
print(result3)

# Task 4 - City-wise revenue
print("\n=== City-wise Revenue ===")
result4 = pd.read_sql("""
    SELECT city,
           SUM(quantity * price) AS city_revenue,
           COUNT(*) AS total_orders
    FROM purchases
    GROUP BY city
    ORDER BY city_revenue DESC
""", conn)
print(result4)

conn.close()
print("\n✓ All SQL queries executed successfully!")