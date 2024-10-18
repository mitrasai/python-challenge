# Sum, Count and Average of Entered Numbers
# Write a program which repeatedly reads numbers until the user enters "done". Once “done” is entered, print out the total, count, and average of the numbers.

# If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

# Step 1 - Create a function which checks for numbers using try and except block.

# Step 2 - Inside while loop ask for input

# Step 3 - Calculate count, sum and average

# Enter a number: 2
# Enter a number: 4
# Enter a number: six
# Error, please enter numeric input
# Enter a number: 6
# Enter a number: done
# 12.0 3 4.0


def checking_input(user_input):
  try:
    user_input = float(user_input)
    return user_input
  except:
    print("Error, please enter numeric input")
    return None


total_sum = 0
count = 0

while True:
  user_input = input("Enter a number: ")
  if user_input.lower() == "done":
    break

  validate_input = checking_input(user_input)
  if validate_input is not None:
    total_sum += validate_input
    count += 1
avg = 0
avg = total_sum / count

print(f"Total sum of {count} numbers is: {total_sum} and average is: {avg}")
