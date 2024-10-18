def input_checker(user_input):
  try:
    val = int(user_input)
    return val
  except:
    print("Error, please enter an numeric input")
    return None

def fizzBuzz():
  """This function prints each number from 1 and 100 in turn"""
  user_input = input("How many numbers do you want? ")
  validate_input = input_checker(user_input)
  if validate_input is not None:
    for i in range(1, validate_input+1):
      if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
      elif i % 5 == 0:
        print("Fizz")
      elif i % 7 == 0:
        print("Buzz")
      else:
        print(i)

fizzBuzz()