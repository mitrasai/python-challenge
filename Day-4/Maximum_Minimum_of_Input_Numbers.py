def checking_input(user_input):
  try:
    val = float(user_input)
    return val
  except:
    print("Error, please enter an numeric input")
    return None


numbers = []
while True:
  user_input = input("Enter a number: ")
  if user_input.lower() == "done":
    break

  validated_input = checking_input(user_input)
  if validated_input is not None:
    numbers.append(validated_input)

if numbers:
  maxi = max(numbers)
  mini = min(numbers)
  print(f"Maximum number: {maxi}, Minimum number: {mini}")
else:
  print("No valid numbers entered")
