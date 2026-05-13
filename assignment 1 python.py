# Initial inventory dictionary
inventory = {
    '101': ['Laptop', 18, 49000],
    '102': ['Phone', 23, 12000],
    '103': ['Speaker', 50, 4500],
    '109': ['Cell Phone', 30, 9000]
    # Add more items as needed
}

# List to store purchases
purchases = []

# Loop to input item codes and quantities
print("Enter item codes and quantities. Leave item code blank to finish.")
while True:
    code = input("item code: ").strip()
    if not code:
        break
    try:
        qty = int(input("qty: "))
        if qty <= 0:
            print("Quantity must be positive.")
            continue
    except ValueError:
        print("Invalid quantity.")
        continue

    if code in inventory:
        name, stock, price = inventory[code]
        if qty > stock:
            print(f"Not enough stock for {name}. Available: {stock}")
            continue
        purchases.append([name, qty, price])
        inventory[code][1] -= qty  # Update inventory count
    else:
        print("Invalid item code.")

# If no purchases, exit
if not purchases:
    print("No items purchased.")
else:
    # Calculate totals
    total_qty = sum(q for _, q, _ in purchases)
    total_amount = sum(q * p for _, q, p in purchases)

    # Print bill
    print("=" * 41)
    print("    ABC ELECTRONICS MART")
    print("=" * 41)
    print("SNO   ITEM NAME           QTY     PRICE")
    print("-" * 41)
    for i, (name, qty, price) in enumerate(purchases, 1):
        line_amount = qty * price
        print(f"{i:<6}{name:<20}{qty:<8}{line_amount:<8}")
    print("-" * 41)
    print(f"     TOTAL                 {total_qty:<8}{total_amount:<8}")
    print("=" * 41)