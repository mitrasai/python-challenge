print("Welcome to Burger Shop!")
print(
    "Price List\nMini Burger(M): $5\nNormal Burger(N): $9\nLarge Burger(L): $10"
)

burger_size = input("What size Burger do you want? M, N or L: ")
add_mushroom = input("Do you want mushroom? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

base_price = 0
mushroom_price = 0
cheese_price = 0

if burger_size == "M":
    base_price = 5
elif burger_size == "N":
    base_price = 8
elif burger_size == "L":
    base_price = 10

if (burger_size == "M" or burger_size == "N") and add_mushroom == "Y":
    mushroom_price = 1
elif burger_size == "L" and add_mushroom == "Y":
    mushroom_price = 2

if extra_cheese == "Y":
    cheese_price = 1

total_bill = base_price + mushroom_price + cheese_price

print(f"Your final bill is: ${total_bill}")
