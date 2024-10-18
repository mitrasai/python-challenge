  import random

  play_again = True

  while play_again:
    user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    pre_choice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(pre_choice)

    print(f"You chose {user_choice}, computer chose {computer_choice}.")

    if user_choice == computer_choice:
      print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
      if computer_choice == "scissors":
        print("Rock smashes scissors! You win.")
      else:
        print("Paper covers rock! You lose.")
    elif user_choice == "paper":
      if computer_choice == "rock":
        print("Paper covers rock! You win.")
      else:
        print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
      if computer_choice == "paper":
        print("Scissor cuts paper! You win.")
      else:
        print("Rock smashes scissor! You lose.")
    else:
      print("Invaid choice! please choose rock, paper, scissors.")

    response = input("\nPlay again (Y/N)? ").lower()

    if response == "n":
      play_again = False
    elif response != "y":
      print("Invalid choice, please choose (Y/N)")
      play_again = False
      quit()