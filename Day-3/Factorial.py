def factorial(num):
  if num <= 1:
    return 1
  return num * factorial(num - 1)


num = int(input("Enter a number: "))
output = factorial(num)
print(f"The factorial of {num} is: {output}")
