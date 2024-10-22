def maxProduct(intArray):
  arrLength = len(intArray)
  prodMaxi = 0
  maxiPair = ""
  for i in range(0, arrLength):
    for j in range(i + 1, arrLength):
      if intArray[i] * intArray[j] > prodMaxi:
        prodMaxi = intArray[i] * intArray[j]
        maxiPair = "(" + str(intArray[i]) + "," + str(intArray[j]) + ")"
  return maxiPair


intArray = [10, 20, 30, 40, 50]
result = maxProduct(intArray)
print(result)
