# Inventory Management System in Python
class Inventory:
    def __init__(self):
        self.products = {}

def add_product(self, product_name, quantity, price):
    if product_name in self.products:
        self.products[product_name]['quantity'] += quantity
    else:
        self.products[product_name] = {'quantity': quantity, 'price': price}
    print(f"Added {quantity} of {product_name}.")

def view_inventory(self):
    if not self.products:
        print("Inventory is empty.")
        return
    
    print("\nInventory:")
    for product_name, details in self.products.items():
        print(f"{product_name} - Quantity: {details['quantity']}, Price: {details['price']}")
        
def update_product(self, product_name, quantity=None, price=None):
    if product_name in self.products:
        if quantity is not None:
            self.products[product_name]['quantity'] = quantity
        if price is not None:
            self.products[product_name]['price'] = price
        print(f"Updated {product_name}.")
    else:
        print(f"Product {product_name} not found in inventory.")

def delete_product(self, product_name):
    if product_name in self.products:
        del self.products[product_name]
        print(f"Deleted {product_name} from inventory.")
    else:
        print(f"Product {product_name} not found in inventory.")

# Menu to interact with the system
def main():
    inventory = Inventory()

    while True:
        print("\n--- Inventory Management ---")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory.add_product(product_name, quantity, price)

        elif choice == '2':
            inventory.view_inventory()

        elif choice == '3':
            product_name = input("Enter product name: ")
            quantity = input("Enter new quantity (leave blank to skip): ")
            price = input("Enter new price (leave blank to skip): ")

            quantity = int(quantity) if quantity else None
            price = float(price) if price else None

            inventory.update_product(product_name, quantity, price)

        elif choice == '4':
            product_name = input("Enter product name: ")
            inventory.delete_product(product_name)

        elif choice == '5':
            print("Exiting...")
        break

    else:
        print("Invalid choice, please try again.")
    
if __name__ == "__main__":
    main()