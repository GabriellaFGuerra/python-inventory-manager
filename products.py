class Product:
    def __init__(self, name, price, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_product(self):
        # Append the current product's details to the file
        with open("products.txt", "a") as file:
            file.write(f"{self.name},{self.price},{self.quantity}\n")
        print(f"Product {self.name} added successfully!")

    @staticmethod
    def remove_product(name):
        # Remove the product from the file based on the name
        with open("products.txt", "r") as file:
            lines = file.readlines()

        with open("products.txt", "w") as file:
            for line in lines:
                if name not in line:  # Only write back lines that don't contain the product name
                    file.write(line)

        print(f"Product {name} removed successfully!")

    @staticmethod
    def update_product(name, new_price, new_quantity):
        # Update the product's details in the file
        updated = False
        with open("products.txt", "r") as file:
            lines = file.readlines()

        with open("products.txt", "w") as file:
            for line in lines:
                if name in line:
                    file.write(f"{name},{new_price},{new_quantity}\n")
                    updated = True
                else:
                    file.write(line)

        if updated:
            print(f"Product {name} updated successfully!")
        else:
            print(f"Product {name} not found!")

    @staticmethod
    def search_product(name):
        # Search for a product by name and print it
        with open("products.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            if name in line:
                print(f"Found product: {line.strip()}")
                break
        else:
            print("Product not found!")

    @staticmethod
    def display_products():
        # Display all products in the file
        with open("products.txt", "r") as file:
            lines = file.readlines()

        print("All products:")
        for line in lines:
            print(line.strip())
