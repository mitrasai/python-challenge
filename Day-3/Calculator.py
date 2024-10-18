def add(num1, num2):
    """This function adds two numbers"""
    return num1 + num2

def substract(num1, num2):
    """This function substracts numbers"""
    return num1 - num2

def multiply(num1, num2):
    """This function multiplies two numbers"""
    return num1 * num2

def divide(num1, num2):
    """This function divides numbers"""
    return int(num1 / num2)

def calculate(num1, num2, op):
    """This function takes two numbers and performs calculations"""
    if op == '+':
        return add(num1, num2)
    elif op == '-':
        return substract(num1, num2)
    elif op == '*':
        return multiply(num1, num2)
    elif op == '/':
        return divide(num1, num2)

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
op = input("Pick operation from this list (+,-,*,/) ")

result = calculate(num1, num2, op)
print(f"{num1} {op} {num2} = {result}")