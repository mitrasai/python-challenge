# wkt, bmi = weight in kg / (height in m)^2

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / (height * height), 2)

if bmi < 18.5:
  print(f"Your bmi is {bmi}, your underweight.")
elif bmi >= 18.5 or bmi < 25:
  print(f"Your bmi is {bmi}, your weight is normal.")
elif bmi >= 25 or bmi < 30:
  print(f"Your bmi is {bmi}, your overweight.")
elif bmi >= 30 or bmi < 35:
  print(f"Your bmi is {bmi}, your obese.")
else:
  print(f"Your bmi is {bmi}, your several obese.")
