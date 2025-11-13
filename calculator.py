import math
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

def logarithm(a, b):
    return math.log(b, a)

def exponent(a, b):
    return a**b

