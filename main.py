import products

def menu():
    print("1. Add product")
    print("2. Remove product")
    print("3. Update product")
    print("4. Search product")
    print("5. Display products")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    return choice

while True:
    choice = menu()
    
    match choice:
        case "1":  # Needs to be a string since input returns a string
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = products.Product(name, price, quantity)
            product.add_product()
        case "2":
            name = input("Enter product name to remove: ")
            products.Product.remove_product(name)
        case "3":
            name = input("Enter product name to update: ")
            new_price = float(input("Enter new price: "))
            new_quantity = int(input("Enter new quantity: "))
            products.Product.update_product(name, new_price, new_quantity)
        case "4":
            name = input("Enter product name to search: ")
            products.Product.search_product(name)
        case "5":
            products.Product.display_products()
        case "6":
            print("Exiting...")
            break  # Exits the loop when user chooses to exit
        case _:
            print("Invalid choice. Please try again.")
