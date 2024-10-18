def add_odd_numbers():
  odd_sum = 0
  for num in range(1, 101, 2):
    odd_sum = odd_sum + num
  return odd_sum


sum_odd = add_odd_numbers()
print(sum_odd)
