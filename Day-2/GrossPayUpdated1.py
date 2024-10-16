# Gross Pay with Overtime

# give 1.5 times the hourly rate for hours worked above 40hrs

hour = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hour > 40:
    overtime = hour - 40
    regular_hours = 40
    regular_pay = regular_hours * rate
    overtime_pay = overtime * rate * 1.5
    pay = regular_pay + overtime_pay
else:
    pay = round(hour * rate, 2)

print(f"Pay: ${pay}")