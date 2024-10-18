# Dice Rolling - Wap runs, it will randomly choose a number 1 and 6. Then program will print what that number is. It should then ask if you'd like to roll again.

import random

def roll_dice():
  """This function generate random between 1 and 6"""
  while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice1: {dice1}")
    print(f"Dice2: {dice2}")
    user_input = input("Roll the dice again? (Y/N) ").lower()
    if user_input == "n":
      break
    elif user_input != "y":
      print("Please enter Y/N")
      quit()

roll_dice()