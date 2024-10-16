# leap year - 366 days -> 365 d, 5 hrs, 48 mins, 45 sec

# rule-1: should be evenly divisible by 4, and not evenly divisbile by 100 -> leap year
# rule-2: evenly divisible by 4 and evenly divisible by 100 and evenly divisible by 400

year = int(input("Enter an year: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not a Leap year.")
  else:
    print("Leap year.")
else:
  print("Not a Leap year.")
