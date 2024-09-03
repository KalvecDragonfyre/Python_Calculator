import math


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def square_root(x):
    return math.sqrt(x)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def percent(x):
    return x / 100

def exponent(x, y):
    return x ** y