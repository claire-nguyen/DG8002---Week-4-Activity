# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: Claire Nguyen
# Date: 06 Oct 2026

# SCENARIO
# A restauraunt wants a simple ordering system that allows customers to browse a menu, select items, and calculate their total bill.

menu  = {
    "Burger" : 12.00,
    "Pizza" : 15.00,
    "Salad" : 9.00,
    "Fries" : 5.00,
    "Drink" : 3.00
}

order = []

# TODO 1: Print out the entire menu and the price of each item

# TODO 2: Start a loop, asking the customer which item they would like to order

    # TODO 3: If the customer types a word check whether the requested item exists

    # TODO 4: Add valid items to the customer's order and let the loop continue

    # TODO 5: if the customer types "Done", end the loop and move to end of order

# TODO 6: Print out an itemized receipt for the user showing item and cost

# TODO 7: Print out the subtotal of the entire order

print ("MENU:")
for item, price in menu.items():
    print(f"{item:<8} - ${price:.2f}")
while True:
    item = input("What would you like to order? (Type 'Done' when finished): ")
    if item == "Done":
        break

    if item in menu:
        order.append(item)
        print(f"{item} added sucessfully!") 
    else:
        print(f"Sorry, we don't serve {item} here. Please select an item from the menu.")
        continue

subtotal = 0.0

for i in range(len(order)):
    item_name = order[i]
    item_price = menu[item_name]
    subtotal += item_price
    if i == 0:
        print(f"Order: {item_name:<6} - {item_price:5.2f}")
    else:
        print(f"       {item_name:<6} - {item_price:5.2f}")

print(f"TOTAL: ${subtotal:.2f}")

# EXPECTED OUTPUT
# Order: Burger - 12.00
#        Fries  -  5.00
#        Drink  -  3.00
#         TOTAL: $20.00
