print("Welcome to Love Calculator")
name1 = input("Enter his name: ").lower()
name2 = input("Enter her name: ").lower()

combination = name1 + name2

trueCount = combination.count('t') + combination.count('r') + combination.count(
    'u') + combination.count('e')

loveCount = combination.count('l') + combination.count('o') + combination.count(
    'v') + combination.count('e')

loveScore = int(str(trueCount) + str(loveCount))

if loveScore < 10 or loveScore > 85:
  print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore > 40 and loveScore < 70:
  print(f"Your score is {loveScore}, you are alright together.")
else:
  print(f"Your score is {loveScore}.")
