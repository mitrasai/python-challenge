# we can solve this problem using, sorting, hashing
def permutation(intArray1, intArray2):
  if len(intArray1) != len(intArray2):
    return False

  sum1 = 0
  sum2 = 0
  prod1 = 1
  prod2 = 1

  for i in range(0, len(intArray1)):
    sum1 = sum1 + intArray1[i]
    sum2 = sum2 + intArray2[i]
    prod1 = prod1 * intArray1[i]
    prod2 = prod2 * intArray2[i]

  if sum1 == sum2 and prod1 == prod2:
    return True
  return False


intArray1 = [1, 2, 3, 4, 5]
intArray2 = [5, 1, 2, 3, 4]
result = permutation(intArray1, intArray2)
print(result)
