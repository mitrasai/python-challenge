import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

number_of_letters = int(input("How many letters do you want in your password? "))
number_of_numbers = int(input("How many numbers do you want in your password? "))
number_of_symbols = int(input("How many symbols do you want in your password? "))

# use choice() function from random module to select random characters from letters, numbers or symbols

password = ""

for letter in range(1, number_of_letters+1):
  password += random.choice(letters)
for num in range(1, number_of_numbers+1):
  password += random.choice(nums)
for symbol in range(1, number_of_symbols+1):
  password += random.choice(symbols)

# print(f"Your password is: {password}")

# generating comples password
password_list = list(password)
# print(password_list)
random.shuffle(password_list)
# print(password_list)

# key = "".join(password_list)
# print(key)

final_password = ""
for item in password_list:
  final_password += item

print(f"Your password is: {final_password}")