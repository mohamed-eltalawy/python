# 🛍️ Online Retail EDA & Sales Analysis

This project performs exploratory data analysis (EDA) on transactional data from a UK-based non-store online retail company. The dataset includes customer purchases, product details, quantities, unit prices, countries, and timestamps.

## 📊 Objective
- Understand customer behavior and purchasing patterns
- Visualize product sales and sales trends over time
- Identify top-selling products and busiest periods
- Detect anomalies or outliers that may impact business performance
- Provide actionable insights and recommendations to improve store operations and customer satisfaction

---

## 📁 Dataset Description
The dataset includes transactions from **01/12/2010 to 09/12/2011**. Each row represents a single product purchase.

### 📄 Main Columns:
- `InvoiceNo`: Transaction invoice number
- `StockCode`: Unique product code
- `Description`: Product name
- `Quantity`: Number of units purchased
- `InvoiceDate`: Date and time of the transaction
- `UnitPrice`: Price per unit
- `CustomerID`: Unique customer identifier
- `Country`: Country of the customer

---

## 🧪 Key Analysis Steps

### ✅ 1. Data Loading & Cleaning
- Loaded the dataset using Pandas and displayed the first 7 rows
- Removed duplicates and handled missing values (especially in `CustomerID` and `Description`)
- Converted `InvoiceDate` to datetime format

### ✅ 2. Descriptive Statistics
- Explored mean, median, max, min, and distribution of key features (e.g., Quantity, UnitPrice)

### ✅ 3. Visualizations & Insights

#### 🧍 Customer Distribution
- Histogram showing number of purchases per CustomerID

#### 📈 Sales Over Time
- Line chart of daily total quantity sold
- Identified peaks and dips in sales

#### 🌍 Country-wise Sales
- Bar chart showing total quantity sold per country
- UK dominated most of the transactions

#### 💵 Product Price Distribution
- Histogram of UnitPrice to detect unusually priced items and outliers

#### 🏆 Top-Selling Products
- Bar chart of the top 10 most sold products based on quantity

#### 🗓️ Seasonal Trends
- Analyzed busiest **months** and **days of the week** in terms of sales

#### ⚠️ Outlier Detection
- Identified anomalous prices and extreme quantities that may require business review

---

## 📌 Tools Used
- Python (Pandas, NumPy)
- Seaborn, Matplotlib for data visualization
- Jupyter Notebook / Google Colab

---

## 📈 Key Insights
- Some products had unusually high quantities or prices — possible entry errors or bulk sales
- UK customers make up over 90% of the transactions
- Busiest sales days fall around the holiday seasons
- Few products dominate overall sales volume (Pareto effect)

---

## 📢 Recommendations
- Investigate price/quantity outliers before reporting
- Focus marketing efforts on top-selling items and high-activity periods
- Improve product availability during peak months

---

## 👨‍💻 Author
**Mohamed Elsayed Emam Eltalawy**  
[LinkedIn Profile](https://www.linkedin.com/in/mohamedeltalawy/)  
[GitHub Profile](https://github.com/mohamed-eltalawy)

---

## 📎 License
This project is for educational and demonstration purposes only.
