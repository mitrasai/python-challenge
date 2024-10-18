def add_even_numbers(start, end):
  even_sum = 0
  for num in range(start, end + 1):
    if num % 2 == 0:
      even_sum += num
  return even_sum


sum_even = add_even_numbers(1, 100)
print(sum_even)
