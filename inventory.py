inventory = {
    "Rice": {
        "price": 60,
        "stock": 25
    }
}

def add_product():
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    inventory[name] = {"price": price, "stock": stock}
    print(f"{name} added successfully!")

def view_products():
    for product, details in inventory.items():
        print(f"{product} - Price: {details['price']}, Stock: {details['stock']}")

def search_product():
    name = input("Enter product name to search: ")
    if name in inventory:
        print(f"{name} - Price: {inventory[name]['price']}, Stock: {inventory[name]['stock']}")
    else:
        print("Product not found!")

def update_stock():
    name = input("Enter product name to update: ")
    if name in inventory:
        stock = int(input("Enter new stock: "))
        inventory[name]['stock'] = stock
        print(f"Stock updated for {name}!")
    else:
        print("Product not found!")

def sell_product():
    name = input("Enter product name to sell: ")
    if name in inventory:
        qty = int(input("Enter quantity to sell: "))
        if qty <= inventory[name]['stock']:
            inventory[name]['stock'] -= qty
            print(f"Sold {qty} units of {name}.")
        else:
            print("Not enough stock!")
    else:
        print("Product not found!")

def delete_product():
    name = input("Enter product name to delete: ")
    if name in inventory:
        del inventory[name]
        print(f"{name} deleted successfully!")
    else:
        print("Product not found!")

def total_products():
    print(f"Total products: {len(inventory)}")

while True:
    print("\n1. Add Product\n2. View Products\n3. Search Product\n4. Update Stock\n5. Sell Product\n6. Delete Product\n7. Total Products\n8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_stock()
    elif choice == "5":
        sell_product()
    elif choice == "6":
        delete_product()
    elif choice == "7":
        total_products()
    elif choice == "8":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
