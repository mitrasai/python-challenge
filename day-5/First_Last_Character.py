# First and Last Characters
# Implement a function which takes the string type list as a parameter and returns the count of the number of strings where the string length is 2 or more and the first and the last characters are same.

# Example
# list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
# count_words(list1)

# Output
# 3

list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']


def count_words(list1):
  count = 0
  for item in list1:
    val = item
    first_character = val[0]
    last_character = val[len(val) - 1]

    if first_character == last_character:
      count += 1

  return count


result = count_words(list1)
print(result)
