import math

def next_number(number):
    return number + 1

def previous_number(number):
    return number - 1

def odd_number(number):
    if number % 2 == 0:
        return False
    return True

def prime_number(number):
    if (number % 2 == 0 and number != 2) or (number in [0,1]):
        return False
    else:
        for i in range(3, number, 2):
            if number % i == 0:
                return False
    return True

def square_number(number):
    return math.sqrt(number)

def binary_number(number):
    return bin(number)[2:]

def oct_number(number):
    return oct(number)[2:]
