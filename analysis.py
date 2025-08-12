import pandas as pd
import matplotlib.pyplot as plt

file_path = "sales.csv"
try:
    df = pd.read_csv(file_path)
    print(" CSV loaded successfully!")
except FileNotFoundError:
    print("File not found! Please check the file path.")
    exit()

print("\n First 5 rows of data:")
print(df.head())


print("\n Dataset Info:")
print(df.info())


if 'Category' in df.columns and 'Sales' in df.columns:
    category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    print("\n Total Sales by Category:")
    print(category_sales)

  
    category_sales.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Total Sales by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Sales')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
else:
    print(" 'Category' or 'Sales' column not found in CSV!")


if 'Order Date' in df.columns and 'Sales' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df.dropna(subset=['Order Date'], inplace=True)
    df['Month'] = df['Order Date'].dt.to_period('M')

    monthly_sales = df.groupby('Month')['Sales'].sum()
    print("\n Monthly Sales Summary:")
    print(monthly_sales)

   
    monthly_sales.plot(kind='line', marker='o', color='green')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
else:
    print(" 'Order Date' or 'Sales' column not found in CSV!")


if 'Product' in df.columns and 'Sales' in df.columns:
    top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)
    print("\n Top 5 Products by Sales:")
    print(top_products)

   
    top_products.plot(kind='barh', color='orange', edgecolor='black')
    plt.title('Top 5 Products by Sales')
    plt.xlabel('Total Sales')
    plt.ylabel('Product')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
else:
    print("'Product' or 'Sales' column not found in CSV!")
