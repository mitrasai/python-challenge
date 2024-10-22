def isUnique(intArray):
  for i in range(0, len(intArray)):
    for j in range(i + 1, len(intArray)):
      if intArray[i] == intArray[j]:
        return False
  return True


intArray = [1, 2, 3, 4, 5, 6]
result = isUnique(intArray)
print(result)
