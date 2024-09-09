menu = {"Pizza":40,"Burger":50,"Coffee":60,"Biryani":80,"Sandwich":90,"Mojito":100}

print("Welcome to the restaurant")
print("Pizza:40\nBurger:50\nCoffee:60\nBiryani:80\nSandwich:90\nMojito:100")

total=0

while True:
    item_1=input("enter the item name: ")
    if item_1 in menu:
        total+=menu[item_1]
        print(f"your order {item_1} is placed")

    else:
        print("your order item is not available")
        
    add_order=input("Do you want another item? (Yes/No) ")
    if add_order!="Yes":
        break
print(f"the total amount to pay is: {total}")