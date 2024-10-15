# Write a program to prompt the user for hours and rate per hour to compute gross pay. You need to take into account that the result has exactly two digits place.

hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hour) * float(rate)
print(f"Pay: {round(pay, 2)}")
