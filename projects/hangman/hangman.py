import random
import ascii_art
from replit import clear
from hangman_words import word_list

# Generate a secret word
# word_list = ["PLAYER", "THANOS", "NARUTO", "LUFFY", "GOKU"]

secret_word = random.choice(word_list)
# print(secret_word)
length_word = len(secret_word)

# Generate/show blanks and board to the player
blanks = []
for _ in range(length_word):
  blanks.append("_")

attempts = 6
guessed_letters = []
end_game = False
print("Welcome to Hangman!")

while not end_game:
  # Ask player to guess a letter
  guess = input("Guess a letter: ").upper()
  clear()
  # Check if letter is already guessed or not
  if guess in guessed_letters:
    print("You have already guessed this letter")
    continue
  else:
    guessed_letters.append(guess)

  # Is the guessed letter in the word or not
  for position in range(length_word):
    # if the letter is in the secrect word, loop through         each position in secret word and update blanks list with     the matched leter in its position in secret word
    letter = secret_word[position]
    if guess == letter:
      blanks[position] = letter

  if guess not in secret_word:
    attempts = attempts - 1
  if attempts == 0:
    end_game = True
    print(f"Correct word is: {secret_word}")
    print("You lose!")

  print(" ".join(blanks))
  print(ascii_art.hangman_stage[attempts])

  if "_" not in blanks:
    end_game = True
    print("You win!")

  if end_game:
    ask = input("Do you want to play again?(Y/N): ").upper()
    if ask == "Y":
      secret_word = random.choice(word_list).upper()
      length_word = len(secret_word)

      blanks.clear()
      for _ in range(length_word):
        blanks.append("_")
      attempts = 6  # reset attempts
      guessed_letters.clear()
      end_game = False
      print("Welcome to Hangman!")
    else:
      print("Thank you! See you next time!")
