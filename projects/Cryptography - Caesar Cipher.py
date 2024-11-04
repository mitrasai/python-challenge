"""
Cryptography with Python - Encryption & Decryption

Encrypt = Hello
Decrypt = MJQQT
"""

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

def refactor_position(p_position, p_cipher_type):
  if p_cipher_type == "E":
    while p_position > 25:
      p_position = p_position - 26
  else:
    while p_position < 0:
      p_position = p_position + 26
  return p_position

def caesar_cipher(p_initial_message, p_shift_number, p_cipher_type):
  result = ""
  if p_cipher_type == "D":
    p_shift_number *= -1
  
  for char in p_initial_message:
    if char in alphabets:
      # current position
      position = alphabets.index(char)
      # new position
      new_position = position + p_shift_number
      new_position = refactor_position(new_position, p_cipher_type)
      result += alphabets[new_position]
    else:
      result += char
  print(f"Here is the {'decode' if p_cipher_type == 'D' else 'encode'}d, result: {result}")

end_program = False
while not end_program:
  user_choice = input("Type 'E' to encrypt, type 'D' to decrypt:\n").upper()
  message = input("Enter you message:\n").upper()
  numbersToBeShifted = int(input("Enter the shift number:\n"))
  caesar_cipher(message, numbersToBeShifted, user_choice)

  restart = input("Type 'Y' to continue, type 'N' to stop\n").upper()
  if restart == "N":
    end_task = True
    print("Thank you!")
    break
  elif restart == "Y":
    continue
  else:
    print("Please choose 'Y' or 'N'!!")
    break