#Define ItemToPurchase class
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_cost = item_price * item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_cost}")


#Example usage:
item_data= []
for i in range(2):
    print(f"Item {i+1}")
    item = ItemToPurchase(
    input("Enter the item name:\n"),
    float(input("Enter the item price:\n")),
    int(input("Enter the item quantity:\n")))
    item_data.append(item)

print("\nTOTAL COST")
total_cost = 0.0
for item in item_data:
    item.print_item_cost()
    total_cost += item.item_cost

print(f"Total: ${total_cost}")