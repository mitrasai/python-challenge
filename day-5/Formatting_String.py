names = ["John", "Edy", "Jane", "Kane"]
scores = [90, 95, 80, 75]

print("{0:<10} {1:<5}".format("Name", "Score"))
for index in range(0, len(names)):
  name = names[index]
  score = scores[index]
  print("{0:<10} {1:<5}".format(name, score))
