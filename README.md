# Product Management System

This Python-based Product Management System allows you to manage a list of products using a simple text file (`products.txt`). It provides functionality to add, remove, update, search, and display products via a console-based menu.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Features
- **Add Product:** Adds a new product with name, price, and quantity to the product list.
- **Remove Product:** Removes a product by name from the product list.
- **Update Product:** Updates the price and quantity of an existing product.
- **Search Product:** Finds and displays a product by name.
- **Display Products:** Shows all products currently stored.
- **Data Persistence:** All product information is saved in a text file (`products.txt`).

## Installation

### Prerequisites
- Python 3.x installed on your machine.

### Steps
1. Clone the repository or download the source code:
   ```bash
   git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd product-management-system
    ```
3. No additional dependencies are required, as the project uses Python’s built-in libraries for file handling.

## Usage

## Running the Program
1. Start the main script by running:

```bash
python main.py
```
2. You will see a menu with the following options:

```markdown
1. Add product
2. Remove product
3. Update product
4. Search product
5. Display products
6. Exit
```
3. Enter the corresponding number to perform the desired action.

## Example
- To add a product:
    - Select option 1 and enter the product name, price, and quantity when prompted.
- To remove a product:
    - Select option 2 and enter the product name to remove.
- File Storage
    - Product data is stored in a file named products.txt. Each product is saved as a comma-separated line in the format:
```
product_name,price,quantity
```

## Project Structure
```bash
├── main.py              # Main script for running the menu
├── products.py          # Product class definition
├── products.txt         # File for storing product information (created automatically)
└── README.md            # Project documentation
```
- main.py: Contains the logic for the interactive menu and user input.
- products.py: Contains the Product class with methods for adding, removing, updating, and displaying products.
- products.txt: Stores the product data in a plain text format.