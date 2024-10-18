def max_of_three(num1, num2, num3):
  """This function takes 3 inputs and finds maximum from it"""
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num3 and num2 > num1:
    return num2
  else:
    return num3


def validate_number(user_input):
  """This function checks for right integer input"""
  try:
    result = int(user_input)
    return result
  except ValueError:
    print("Invalid input, please enter valid numeric.")
    quit()


n1 = validate_number(input("Enter first number: "))
n2 = validate_number(input("Enter second number: "))
n3 = validate_number(input("Enter third number: "))

output = max_of_three(n1, n2, n3)
print(output)
