import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('ecommerce.csv')

# Create total_purchase column
df['total_purchase'] = df['quantity'] * df['price']

# Top customers
top_customers = df.groupby('customer_name')['total_purchase'].sum().sort_values(ascending=False).head(10)
print("Top 10 Customers:\n", top_customers)

# Product popularity
product_pop = df.groupby('product')['quantity'].sum().sort_values(ascending=False)
print("\nProduct Popularity:\n", product_pop)

# City revenue
city_rev = df.groupby('city')['total_purchase'].sum().sort_values(ascending=False)
print("\nCity Revenue:\n", city_rev)

# Bar Chart – Product Sales
plt.figure(figsize=(10, 5))
product_pop.plot(kind='bar', color='steelblue')
plt.title('Product Sales by Quantity')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.savefig('product_sales.png')
plt.show()

# Pie Chart – City Revenue
plt.figure(figsize=(8, 8))
city_rev.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('City-wise Revenue Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig('city_revenue.png')
plt.show()

# Export to Excel for WPS
df.to_excel('ecommerce_output.xlsx', index=False)
print("\n✓ Excel file exported!")