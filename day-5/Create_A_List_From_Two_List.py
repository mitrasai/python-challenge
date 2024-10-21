# Create a List from Two Lists
# Given two lists create a third list by picking an odd-index element from the first list and even-index elements from the second.

# list_one = [4, 12, 16, 21, 24, 28, 32]
# list_two = [5, 10, 15, 20, 25, 30, 35]

# Output
# [12, 21, 28, 5, 15, 25, 35]

list_one = [4, 12, 16, 21, 24, 28, 32]
list_two = [5, 10, 15, 20, 25, 30, 35]
list_three = []

for i in range(0, len(list_one)):
  if i % 2 != 0:
    list_three.append(list_one[i])

for i in range(0, len(list_two)):
  if i % 2 == 0:
    list_three.append(list_two[i])

print(list_three)
