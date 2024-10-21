# Implement a function which takes two lists as parameter and return concatenation of these lists item wise.

# Example
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# concatenate(list1, list2)
# Output
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]


def concatenate(list1, list2):
  combined_list = []
  for item1 in list1:
    for item2 in list2:
      combined_list.append(item1 + item2)
  print(combined_list)


concatenate(list1, list2)
