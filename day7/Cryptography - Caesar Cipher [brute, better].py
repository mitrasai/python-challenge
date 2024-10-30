
alphabets = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

def encrypt(p_message, p_shift_number):
  """This function shifts each letter of the message forwards in the alphabet 
  by the numbersToBeShifted and returns encrypted message."""
  result = ""
  for char in p_message:
    if char in alphabets:
      # current position
      position = alphabets.index(char)
      # new position by moving forward
      new_position = position + p_shift_number
      # handling index out of bounds
      while new_position > 25:
        new_position = new_position - 26

      result += alphabets[new_position]
    else:
      result += char
  return f"The encoded message is {result}"

def decrypt(p_message, shift_number):
    """This function shifts each letter of the message backwards in the alphabet 
    by the numbersToBeShifted and returns decrypted message."""
    
    result = ""
    for char in p_message:
        if char in alphabets:
          position = alphabets.index(char)
          new_position = position - shift_number

          while new_position < 0:
            new_position = new_position + 26

          result += alphabets[new_position]
        else:
          result += char

    return f"The decoded message is {result}"

end_task = False
while not end_task:
  user_choice = input("Type 'E' to encrypt, type 'D' to decrypt:\n").upper()
  if user_choice not in ["E", "D"]:
    print("Please choose 'E' or 'D'!!")
    break

  message = input("Enter your message:\n").upper()
  numbersToBeShifted = int(input("Enter shift number:\n"))

  if user_choice == "E":
    encrypted_message = encrypt(message, numbersToBeShifted)
    print(encrypted_message)
  elif user_choice == "D":
    decrypted_message = decrypt(message, numbersToBeShifted)
    print(decrypted_message)

  restart = input("Type 'Y' to continue, type 'N' to stop\n").upper()
  if restart == "N":
    end_task = True
    print("Thank You!")
  elif restart == "Y":
    continue
  else:
    print("Choose 'Y' or 'N'!!")
    break