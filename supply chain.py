# ============================================
# INVENTORY MANAGEMENT SYSTEM (FILE BASED)
# ============================================
products = []
sales = []

# ---------- LOAD DATA ----------
def load_data():
    global products, sales

    try:
        with open("products.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 6:
                    data[3] = float(data[3])
                    data[4] = int(data[4])
                    products.append(data)
    except:
        pass

    try:
        with open("sales.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 5:
                    data[2] = int(data[2])
                    data[3] = float(data[3])
                    sales.append(data)
    except:
        pass


# ---------- SAVE PRODUCTS ----------
def save_products():
    with open("products.txt", "w") as f:
        for p in products:
            f.write(f"{p[0]},{p[1]},{p[2]},{p[3]},{p[4]},{p[5]}\n")


# ---------- SAVE SALES ----------
def save_sales():
    with open("sales.txt", "w") as f:
        for s in sales:
            f.write(f"{s[0]},{s[1]},{s[2]},{s[3]},{s[4]}\n")


# -------- ADD PRODUCT --------
def add_product():
    print("\n--- Add Product ---")

    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    supplier = input("Enter Supplier: ")

    products.append([pid, name, category, price, quantity, supplier])
    save_products()

    print("Product Added Successfully")


# -------- VIEW PRODUCTS --------
def view_products():
    print("\n--- View Products ---")

    if not products:
        print("No Products Available")
    else:
        for p in products:
            print("----------------------------")
            print("Product ID   :", p[0])
            print("Name         :", p[1])
            print("Category     :", p[2])
            print("Price        :", p[3])
            print("Quantity     :", p[4])
            print("Supplier     :", p[5])


# -------- SEARCH PRODUCT --------
def search_product():
    print("\n--- Search Product ---")

    pid = input("Enter Product ID: ")

    for p in products:
        if p[0] == pid:
            print("Product Found")
            print("Name:", p[1])
            print("Price:", p[3])
            print("Quantity:", p[4])
            return

    print("Product Not Found")


# -------- UPDATE PRODUCT --------
def update_product():
    print("\n--- Update Product ---")

    pid = input("Enter Product ID: ")

    for p in products:
        if p[0] == pid:
            print("Enter New Details")

            p[1] = input("New Name: ")
            p[2] = input("New Category: ")
            p[3] = float(input("New Price: "))
            p[4] = int(input("New Quantity: "))
            p[5] = input("New Supplier: ")

            save_products()
            print("Product Updated Successfully")
            return

    print("Product Not Found")


# -------- DELETE PRODUCT --------
def delete_product():
    print("\n--- Delete Product ---")

    pid = input("Enter Product ID: ")

    for p in products:
        if p[0] == pid:
            products.remove(p)
            save_products()
            print("Product Deleted Successfully")
            return

    print("Product Not Found")


# -------- SELL PRODUCT --------
def sell_product():
    print("\n--- Sell Product ---")

    invoice = input("Enter Invoice ID: ")
    pid = input("Enter Product ID: ")
    qty = int(input("Enter Quantity Sold: "))
    date = input("Enter Date: ")

    for p in products:
        if p[0] == pid:

            if p[4] >= qty:
                p[4] -= qty
                total = qty * p[3]

                sales.append([invoice, pid, qty, total, date])

                save_products()
                save_sales()

                print("Product Sold Successfully")
                print("Total Amount:", total)

                
                print("Sold Quantity:", qty)
                print("Remaining Stock:", p[4])

                if p[4] <= 5:
                    print("⚠️ LOW STOCK ALERT! Only", p[4], "items left")

                return
            else:
                print("Stock Not Available")
                return

    print("Product Not Found")


# -------- VIEW SALES --------
def view_sales():
    print("\n--- Sales Report ---")

    if not sales:
        print("No Sales Data")
    else:
        for s in sales:
            print("----------------------------")
            print("Invoice ID :", s[0])
            print("Product ID :", s[1])
            print("Quantity   :", s[2])
            print("Amount     :", s[3])
            print("Date       :", s[4])


# -------- PURCHASE STOCK --------
def purchase_stock():
    print("\n--- Purchase Stock ---")

    pid = input("Enter Product ID: ")
    qty = int(input("Enter Quantity to Add: "))

    for p in products:
        if p[0] == pid:
            p[4] += qty
            save_products()

            print("Stock Updated Successfully")

            
            print("Purchased Quantity:", qty)
            print("Current Stock:", p[4])

            if p[4] <= 5:
                print("⚠️ LOW STOCK ALERT! Only", p[4], "items left")

            return

    print("Product Not Found")


# -------- LOW STOCK ALERT --------
def low_stock():
    print("\n--- Low Stock Alert ---")

    
    if not products:
        print("Out of Stock (No Products Available)")
        return

    found = False

    for p in products:
        if p[4] <= 5:
            print("----------------------------")
            print("Product ID:", p[0])
            print("Name      :", p[1])
            print("Quantity  :", p[4])
            found = True

    if not found:
        print("No Low Stock Products")


# -------- MAIN --------
load_data()

while True:

    print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Sell Product")
    print("7. View Sales")
    print("8. Purchase Stock")
    print("9. Low Stock Alert")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_product()
    elif choice == "5":
        delete_product()
    elif choice == "6":
        sell_product()
    elif choice == "7":
        view_sales()
    elif choice == "8":
        purchase_stock()
    elif choice == "9":
        low_stock()
    elif choice == "10":
        print("\nThank You")
        break
    else:
        print("\nInvalid Choice")