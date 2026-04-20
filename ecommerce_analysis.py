import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv('ecommerce_purchases.csv')

# Step 2: Create total_purchase column
df['total_purchase'] = df['quantity'] * df['price']
print("Dataset with Total Purchase:\n", df)

# Step 3: Identify top customers (by total spending)
top_customers = df.groupby(['customer_id', 'customer_name', 'city'])['total_purchase'].sum() \
                  .reset_index().sort_values('total_purchase', ascending=False)
print("\nTop Customers:\n", top_customers.head(5))

# Step 4: Analyze product popularity
product_popularity = df.groupby('product').agg({
    'quantity': 'sum',
    'total_purchase': 'sum'
}).reset_index().sort_values('quantity', ascending=False)
print("\nProduct Popularity:\n", product_popularity)

# Step 5: City-wise revenue
city_revenue = df.groupby('city')['total_purchase'].sum().reset_index().sort_values('total_purchase', ascending=False)
print("\nCity-wise Revenue:\n", city_revenue)

# ===================== VISUALIZATIONS =====================

# Bar chart → Product sales (by total revenue)
plt.figure(figsize=(10, 6))
plt.bar(product_popularity['product'], product_popularity['total_purchase'], color='skyblue')
plt.title('Product Sales by Revenue')
plt.xlabel('Product')
plt.ylabel('Total Revenue (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('product_sales_bar.png')
plt.show()

# Pie chart → City sales distribution
plt.figure(figsize=(8, 8))
plt.pie(city_revenue['total_purchase'], labels=city_revenue['city'], 
        autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('City-wise Revenue Distribution')
plt.savefig('city_sales_pie.png')
plt.show()

print("\n✅ Visualizations saved as product_sales_bar.png and city_sales_pie.png")