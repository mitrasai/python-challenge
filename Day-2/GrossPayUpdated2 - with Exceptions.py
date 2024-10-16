# Gross Pay with Exceptions
try:
  hour = float(input("Enter Hours: "))
  rate = float(input("Enter Rate: "))
except ValueError as e:
  print(f"Error: {e}")
  quit()
else:
  if hour > 40:
    overtime = hour - 40
    regular_hours = 40
    regular_pay = regular_hours * rate
    overtime_pay = overtime * rate * 1.5
    pay = round(overtime_pay + regular_pay, 2)
  else:
    pay = round(hour * rate, 2)

print(f"Your pay is ${pay}")
