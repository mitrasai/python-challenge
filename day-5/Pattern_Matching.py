def print_pattern(n):
  for i in range(0, n):
    for j in range(0, i + 1):
      print("*", end=" ")
    print("")

  for i in range(n, 0, -1):
    for j in range(0, i - 1):
      print("*", end=" ")
    print("")


n = 5
print_pattern(n)
