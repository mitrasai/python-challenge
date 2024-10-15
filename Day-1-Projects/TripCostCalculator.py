# Write a program which calcualtes trip cost for an user
# 1. create a greeting for your program
# 2. ask the user for number of days
# 3. ask the user for hotel price
# 4. ask the user for flight price
# 5. ask the user for rental car price
# 6. ask for other expenses
# 7. combine all the expenses together and print with 2 digits after decimal places.

print("Welcome to the Trip Cost Calculator!")
totalDays = input("How many days will you stay? ")
costPerNight = input("How much does hotel cost per night? $")
flightCost = input("How much does flight cost? $")
carPrice = input(
    "If you need rental car please enter the price otherwise enter zero: $")
otherExpenses = input("Enter other possible expenses: $")
totalExpense = (float(totalDays) * (float(costPerNight) + float(carPrice))
                ) + float(flightCost) + float(otherExpenses)

print(f"Total Cost: ${round(totalExpense, 2)}")
