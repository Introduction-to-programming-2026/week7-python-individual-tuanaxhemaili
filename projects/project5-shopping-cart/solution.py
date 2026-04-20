# Project 5 — Mini Shopping Cart
# Author: your name here

menu = {
    1: ("Apple",  0.50),
    2: ("Banana", 0.30),
    3: ("Milk",   1.20),
    4: ("Bread",  2.00),
}

cart  = {}   # { item_name: quantity }
total = 0.0

# TODO: display the menu
print("--- Shop Menu ---")
for number, (name, price) in menu.items():
    print(f"{number}. {name:<10} ${price:.2f}")
print("5. Done")

# TODO: shopping loop
while True:
    try:
        choice = int(input("\nChoose an item (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 5:
        break

    if choice in menu:
        name, price = menu[choice]

        if name in cart:
            cart[name] += 1
        else:
            cart[name] = 1

        total += price
        print(f"Added {name} to cart.")
    else:
        print("Invalid choice, try again.")

# TODO: print the receipt
print("\n--- Receipt ---")
for item, qty in cart.items():
    # Look up the price for the item in the menu dictionary
    for key, (name, price) in menu.items():
        if name == item:
            print(f"{item:<10} x{qty} = ${price * qty:.2f}")
            break

print(f"Total: ${total:.2f}")
print("Thank you!")
