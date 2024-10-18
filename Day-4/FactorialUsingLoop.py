def factorial(p_num):
    # TODO
    if p_num < 0:
        return "Factorial does not exist for negative numbers"

    if p_num <= 1:
        return f"The factorial of {p_num} is {int(1)}"

    fact = 1
    original_num = p_num
    while p_num > 1:
        fact = fact * p_num
        p_num = p_num - 1
    return f"The factorial of {original_num} is {fact}"


print(factorial(4))
print(factorial(-1))
print(factorial(0))
