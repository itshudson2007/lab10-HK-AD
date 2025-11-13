import math

def logarithm(x, y):
    if x <= 0 or x == 1 or y <= 0:
        raise ValueError("Invalid input for logarithm: Base must be positive and not 1, and the number must be positive.")
    return math.log(x, y)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by zero")
    return a / b

