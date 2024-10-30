def removeDuplicate(nums):
  if len(nums) == 0:
    return 0
  i = 0
  for j in range(1, len(nums)):
    if nums[j] != nums[i]:
      i = i + 1
      nums[i] = nums[j]
  return i + 1


nums = [1, 1, 2]
result = removeDuplicate(nums)
print(results)