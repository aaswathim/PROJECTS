# 📊 Retail Sales Dashboard

## 📌 Project Overview

The **Retail Sales Dashboard** project analyzes sales transactions and product information to generate meaningful business insights.

The dashboard helps businesses understand **sales performance, product demand, category performance, and profit margins** using interactive visualizations.

The project combines **sales transaction data and product information** to provide a complete view of retail performance.

---

# 🎯 Project Objectives

* Analyze overall **sales performance**
* Identify **top-selling products**
* Evaluate **category-wise sales**
* Study **payment methods used by customers**
* Calculate **profit using buying price and selling price**

---

# 📂 Datasets Used

## 1️⃣ Product Dataset

Contains information about products available for sale.

| Column        | Description                           |
| ------------- | ------------------------------------- |
| Product ID    | Unique product identifier             |
| Product       | Product name                          |
| Category      | Product category                      |
| UOM           | Unit of Measurement (Kg, Lt, Ft, No.) |
| Buying Price  | Cost price of the product             |
| Selling Price | Price at which product is sold        |

This dataset contains **45 products across multiple categories**.

---

## 2️⃣ Sales Transactions Dataset

Contains details of each sales transaction.

| Column       | Description                                     |
| ------------ | ----------------------------------------------- |
| Date         | Date of transaction                             |
| Product ID   | Product sold                                    |
| Quantity     | Number of units sold                            |
| Sale Type    | Type of sale (Direct Sales, Online, Wholesaler) |
| Payment Mode | Payment method (Cash / Online)                  |
| Discount %   | Discount applied                                |

This dataset helps analyze **sales trends and customer purchasing behavior**.

---

# 🔗 Data Relationship

The datasets are connected using the **Product ID** column.

```text
Product Dataset
        │
        │ (Product ID)
        ▼
Sales Transactions Dataset
```

This relationship allows the dashboard to combine **product information with sales data**.

---

# 📊 Dashboard KPIs

The dashboard displays important metrics such as:

* 💰 Total Sales Revenue
* 📦 Total Quantity Sold
* 📈 Total Profit
* 🏆 Top Selling Products
* 📊 Category-wise Sales
* 💳 Payment Mode Distribution
* 🛒 Sales Type Distribution

---

# 📉 Dashboard Visualizations

The dashboard includes visualizations such as:

* Sales trend over time
* Category-wise sales comparison
* Top products by revenue
* Payment mode usage
* Profit analysis
* Sales channel performance

---

# 🛠 Tools & Technologies

* **Power BI / Tableau** – Dashboard creation
* **Python** – Data preprocessing
* **Pandas** – Data analysis
* **NumPy** – Numerical operations
* **Excel / CSV** – Data storage

---

# 🔍 Project Workflow

1. Import product and sales datasets
2. Clean and preprocess the data
3. Create relationships between tables
4. Calculate KPIs such as sales and profit
5. Build interactive dashboard visuals
6. Analyze business insights

---

# 📈 Key Insights

The dashboard helps answer important business questions:

* Which products generate the **highest revenue**?
* Which category has the **highest sales**?
* What is the **profit margin per product**?
* Which **payment method is most popular**?
* Which **sales channel performs best**?

---

# 👩‍💻 Author

**Aswathi**

---

# 📜 License

This project is created for **educational and data analytics learning purposes**.
