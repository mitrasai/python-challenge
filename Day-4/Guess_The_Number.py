import math
import random


def input_checker(user_input):
  try:
    val = int(user_input)
    return val
  except:
    print("Error, please enter a numeric input")
    return None

def number_guessing():
  lower = input("Enter Lower bound: ")
  val_lower = input_checker(lower)
  upper = input("Enter Upper bound: ")
  val_upper = input_checker(upper)

  if val_lower is not None and val_upper is not None:
    rand_number = random.randint(val_lower, val_upper)
    total_chances = int(math.log(val_upper - val_lower + 1, 2))
    print(f"\n\tYou've only {total_chances} chances to guess the integer!\n")

    count = 0
    while count < total_chances:
      count += 1
      # loop will continue based on the calculated number of chances
      user_res = input_checker(input("Guess a number: "))
      if user_res is None:
        continue
      if user_res > rand_number:
        print("You guessed too high")
      elif user_res < rand_number:
        print("You guessed too small!")
      else:
        print(f"Congratulations, you did it in {count} try")

  print(f"\nThe number is: {rand_number}") 
  print("\tBetter luck next time")

number_guessing()