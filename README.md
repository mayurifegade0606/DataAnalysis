

---

# Sales Data Analysis Project

This project performs basic data analysis on sales data using Python and Pandas.
It loads sales data from a CSV file, summarizes key insights, and displays charts for visualization.

---

## 🚀 Features

* Load sales data from CSV
* Summarize sales by category, month, and product
* Visualize sales trends using bar and line charts
* Handle missing or malformed data gracefully

---

## 🛠️ How to Run

1. Clone or download this repository to your system.
2. Open a terminal and navigate to the project directory:

   ```bash
   cd DataAnalysisProject
   ```
3. Install dependencies (only required once):

   ```bash
   pip install pandas matplotlib
   ```
4. Run the analysis script:

   ```bash
   python data_analysis.py
   ```
5. Make sure the `sales.csv` file is in the same directory.

---

## 💻 Sample Output

```
✅ CSV loaded successfully!

📊 First 5 rows of data:
   Order Date     Product     Category  Sales  Quantity
0  2025-01-05      Laptop  Electronics  75000         2
1  2025-01-10       Phone  Electronics  45000         3
2  2025-02-03       Shirt     Clothing   1500         5
3  2025-02-07       Shoes     Clothing   2500         2
4  2025-03-01        Book   Stationery    500        10

ℹ️ Dataset Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 5 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Order Date  10 non-null     object
 1   Product     10 non-null     object
 2   Category    10 non-null     object
 3   Sales       10 non-null     int64 
 4   Quantity    10 non-null     int64 
dtypes: int64(2), object(3)
memory usage: 528.0+ bytes
None

💰 Total Sales by Category:
Category
Electronics    150500
Clothing         4000
Stationery       1850
Accessories      7000
Name: Sales, dtype: int64

[Displays bar chart for Total Sales by Category]

📅 Monthly Sales Summary:
Month
2025-01    120000
2025-02     4000
2025-03     1500
2025-04     35000
2025-05     2250
Freq: M, Name: Sales, dtype: int64

[Displays line chart for Monthly Sales Trend]

🏆 Top 5 Products by Sales:
Product
Laptop       75000
Phone        45000
Tablet       30000
Watch         5000
Bag           2000
Name: Sales, dtype: int64

[Displays horizontal bar chart for Top 5 Products by Sales]
```

---

## 📁 Project Structure

```
DataAnalysis/
├── analysis.py
├── sales.csv
└── README.md
```

---

## ✍️ Author

Created by **Mayuri Fegade**

---


