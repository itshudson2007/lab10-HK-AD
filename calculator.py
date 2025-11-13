import math

def logarithm(x, y):
    if x <= 0 or x == 1 or y <= 0:
        raise ValueError("Invalid input for logarithm: Base must be positive and not 1, and the number must be positive.")
    return math.log(y, x)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by zero")
    return b / a

def exp(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)
