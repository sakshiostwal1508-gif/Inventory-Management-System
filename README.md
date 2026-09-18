# Inventory-Management-System
A Python-based File Inventory Management System for managing products, stock, sales, suppliers, and low-stock alerts. It supports CRUD operations, product search, stock purchasing, sales tracking, invoice management, and file-based data storage using products.txt and sales.txt.
# 📦 Inventory Management System

A **File-Based Inventory Management System** developed in **Python** for managing products, stock, sales, suppliers, and low-stock alerts.

The project uses **text files (`products.txt` and `sales.txt`)** for persistent data storage, making it simple, lightweight, and easy to understand for beginners learning Python file handling and CRUD operations.

---

## 🚀 Features

* ➕ Add new products
* 📋 View all products
* 🔍 Search products by Product ID
* ✏️ Update product information
* 🗑️ Delete products
* 🛒 Sell products
* 📊 View sales reports
* 📦 Purchase and update stock
* ⚠️ Low-stock alerts
* 💾 File-based data persistence
* 🔄 Automatic loading and saving of data
* 🧾 Invoice ID tracking
* 💰 Automatic sales amount calculation

---

## 🛠️ Technologies Used

| Technology               | Purpose                      |
| ------------------------ | ---------------------------- |
| 🐍 Python                | Core programming language    |
| 📄 TXT Files             | Data storage                 |
| 🔤 File Handling         | Reading and writing data     |
| 📋 Lists                 | Storing products and sales   |
| 🔄 Functions             | Modular program structure    |
| 🧮 Arithmetic Operations | Sales and stock calculations |

---

## 📁 Project Structure

```text
Inventory-Management-System/
│
├── inventory_management.py
├── products.txt
├── sales.txt
└── README.md
```

### 📄 File Description

**`inventory_management.py`**
Main Python application containing all inventory operations.

**`products.txt`**
Stores product information such as:

```text
Product ID,Product Name,Category,Price,Quantity,Supplier
```

**`sales.txt`**
Stores sales transaction information:

```text
Invoice ID,Product ID,Quantity,Total Amount,Date
```

**`README.md`**
Project documentation and instructions.

---

# ⚙️ System Modules

## 1️⃣ Add Product

Allows the user to add a new product.

The system accepts:

* Product ID
* Product Name
* Category
* Price
* Quantity
* Supplier

Example:

```text
--- Add Product ---

Enter Product ID: P101
Enter Product Name: Laptop
Enter Category: Electronics
Enter Price: 55000
Enter Quantity: 10
Enter Supplier: Dell

Product Added Successfully
```

---

## 2️⃣ View Products

Displays all products currently stored in the inventory.

Example:

```text
--- View Products ---

----------------------------
Product ID   : P101
Name         : Laptop
Category     : Electronics
Price        : 55000.0
Quantity     : 10
Supplier     : Dell
```

---

## 3️⃣ Search Product

Searches for a product using its Product ID.

Example:

```text
--- Search Product ---

Enter Product ID: P101

Product Found
Name: Laptop
Price: 55000.0
Quantity: 10
```

If the product does not exist:

```text
Product Not Found
```

---

## 4️⃣ Update Product

Allows the user to modify existing product information.

The following fields can be updated:

```text
Name
Category
Price
Quantity
Supplier
```

Example:

```text
--- Update Product ---

Enter Product ID: P101

Enter New Details
New Name: Dell Laptop
New Category: Electronics
New Price: 58000
New Quantity: 15
New Supplier: Dell India

Product Updated Successfully
```

---

## 5️⃣ Delete Product

Removes a product from the inventory using its Product ID.

Example:

```text
--- Delete Product ---

Enter Product ID: P101

Product Deleted Successfully
```

---

# 🛒 6️⃣ Sell Product

The selling module records sales transactions and automatically updates the available stock.

The system accepts:

* Invoice ID
* Product ID
* Quantity Sold
* Date

The total amount is calculated automatically:

```text
Total Amount = Quantity × Product Price
```

Example:

```text
--- Sell Product ---

Enter Invoice ID: INV001
Enter Product ID: P101
Enter Quantity Sold: 2
Enter Date: 18-09-2026

Product Sold Successfully
Total Amount: 116000.0
Sold Quantity: 2
Remaining Stock: 13
```

### ⚠️ Low Stock Alert

If stock becomes **5 or fewer items**, the system displays:

```text
⚠️ LOW STOCK ALERT! Only 5 items left
```

---

# 📊 7️⃣ View Sales

Displays recorded sales transactions.

Example:

```text
--- Sales Report ---

----------------------------
Invoice ID : INV001
Product ID : P101
Quantity   : 2
Amount     : 116000.0
Date       : 18-09-2026
```

---

# 📦 8️⃣ Purchase Stock

Allows additional stock to be added to an existing product.

Example:

```text
--- Purchase Stock ---

Enter Product ID: P101
Enter Quantity to Add: 20

Stock Updated Successfully
Purchased Quantity: 20
Current Stock: 33
```

---

# ⚠️ 9️⃣ Low Stock Alert

Displays products whose available quantity is **5 or less**.

Example:

```text
--- Low Stock Alert ---

----------------------------
Product ID: P102
Name      : Keyboard
Quantity  : 4
```

If there are no low-stock products:

```text
No Low Stock Products
```

---

# 🧭 Main Menu

The application provides the following menu:

```text
========== INVENTORY MANAGEMENT SYSTEM ==========

1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Sell Product
7. View Sales
8. Purchase Stock
9. Low Stock Alert
10. Exit

Enter your choice:
```

---

# 💾 Data Persistence

This project uses Python file handling to permanently store inventory information.

### Products

Data is saved in:

```text
products.txt
```

### Sales

Sales transactions are saved in:

```text
sales.txt
```

When the application starts, the `load_data()` function reads the existing files and loads the information into memory.

When changes are made, functions such as:

```python
save_products()
save_sales()
```

update the corresponding files.

---

# 🔄 CRUD Operations

The project demonstrates the basic **CRUD** operations:

| Operation | Function           |
| --------- | ------------------ |
| Create    | `add_product()`    |
| Read      | `view_products()`  |
| Update    | `update_product()` |
| Delete    | `delete_product()` |

Additional business operations include:

```text
Search Product
Sell Product
Purchase Stock
View Sales
Low Stock Alert
```

---

# 🧠 Python Concepts Demonstrated

This project demonstrates several important Python concepts:

### Variables

```python
products = []
sales = []
```

### Lists

Product and sales records are stored using Python lists.

### Functions

The application is divided into reusable functions:

```python
add_product()
view_products()
search_product()
update_product()
delete_product()
sell_product()
view_sales()
purchase_stock()
low_stock()
```

### File Handling

```python
with open("products.txt", "r") as f:
```

and:

```python
with open("products.txt", "w") as f:
```

### Exception Handling

```python
try:
    ...
except:
    pass
```

### Conditional Statements

```python
if choice == "1":
    add_product()
```

### Loops

```python
while True:
```

and:

```python
for p in products:
```

---

# ▶️ How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/Inventory-Management-System.git
```

## 2. Open the Project

```bash
cd Inventory-Management-System
```

## 3. Run the Python Program

```bash
python inventory_management.py
```

If your system uses `python3`:

```bash
python3 inventory_management.py
```

---

# 📋 Requirements

You only need:

* Python 3.x
* VS Code / PyCharm / any Python IDE
* Command Prompt / PowerShell / Terminal

No external Python libraries are required.

---

# 🔐 Input Validation

The current version expects valid numeric input for fields such as:

```text
Price
Quantity
Quantity Sold
```

For example:

```python
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))
```

Future versions can add stronger validation for invalid input.

---

# 📈 Future Improvements

Possible upgrades for future versions:

* 🔐 User login and authentication
* 👥 Multiple user roles
* 🗄️ MySQL / SQLite database integration
* 📊 Graphical dashboard
* 📈 Sales analytics
* 🔎 Advanced product filtering
* 🧾 Printable invoices
* 📧 Email notifications
* 📱 GUI application using Tkinter
* 🌐 Web version using Flask or Django
* 📦 Automatic stock-reorder functionality
* 📊 Export reports to Excel/CSV
* 🔒 Better input validation
* 📝 Transaction history

---

# 🎯 Learning Objectives

This project is useful for practicing:

```text
Python Programming
       ↓
Functions
       ↓
Lists & Data Structures
       ↓
File Handling
       ↓
CRUD Operations
       ↓
Exception Handling
       ↓
Inventory Logic
       ↓
Sales Management
```

---

# 👩‍💻 Author

**Sakshi Ravindra Ostwal**

🎓 Dr. Babasaheb Ambedkar Technological University, Lonere, Raigad
🏫 K.K. Wagh College of Pharmacy, Nashik

### Skills

* Python
* C Programming
* File Handling
* Data Management
* Problem Solving

---

# ⭐ Project Highlights

```text
📦 Inventory Management
💾 File-Based Storage
🛒 Sales Management
📊 Sales Reports
📦 Stock Management
⚠️ Low Stock Detection
🔍 Product Search
✏️ Product Update
🗑️ Product Deletion
🧾 Invoice Tracking
```

---

## 📜 License

This project is created for **educational and learning purposes**.

If you find this project useful, consider giving the repository a ⭐ on GitHub.
