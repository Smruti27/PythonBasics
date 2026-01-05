price = float(input('Please enter the price of meal : '))
print(f"{'Description' :<15} {'Price' :>10}")
print('-'*30)
print(f"{'Meal' :<15} {f'${price:.2f}':>10}")
tip = 0.18 * price
print(f"{'Tip' :<15} {f'${tip:.2f}':>10}")
salesTax = 0.07 * price
print(f"{'Sales Tax' :<15} {f'${salesTax:.2f}':>10}")
print('-'*30)
total = price + tip + salesTax
print(f"{'Total' :<15} {f'${total:.2f}':>10}")
    