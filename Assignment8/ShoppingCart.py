class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0,item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_cost = item_price * item_quantity
        self.item_description = item_description
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_cost}")

class ShoppingCart:
    def __init__(self, customer_name="None", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, cart_item):
        self.cart_items.append(cart_item)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")
        
    def modify_item(self, item_to_modify):
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0.0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                item.item_cost = item.item_price * item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self): 
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.item_cost
        return total_cost
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY\n")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu(cart) :
    option = ""
    while option != "q":
        print("\nMENU") 
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        option = input("\nChoose an option:\n")
        while option not in ["a", "r", "c", "i", "o", "q"]: option = input("Choose an option:\n")
        if option == "a":
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = int(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(ItemToPurchase(name, price, quantity, description))

        elif option == "r":
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif option == "c":
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            cart.modify_item(ItemToPurchase(item_name=name, item_quantity=quantity))

        elif option == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif option == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()
    
def main():
        customer_name = input("Enter customer's name:")
        current_date = input("Enter today's date:")
        cart = ShoppingCart(customer_name, current_date)
        print_menu(cart)


if __name__ == "__main__":
    main()
