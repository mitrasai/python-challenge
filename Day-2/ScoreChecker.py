# wap to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade: A (>=0.9), B (>=0.8), C (>=0.7), D (>=0.6), F(<0.6)

print("Welcome to Score Checker, please enter a score between 0.0 and 1.0")
try:
  score = float(input("Enter a score: "))
except:
  print("Bad Score.")
  quit()
else:
  if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
      print("A")
    elif score >= 0.8:
      print("B")
    elif score >= 0.7:
      print("C")
    elif score >= 0.6:
      print("D")
    else:
      print("F")
  else:
    print("Bad Score.")
