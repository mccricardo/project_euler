#! /usr/bin/env python
""" Project Euler, problem 8. """

# Global vars
FILE = '../number.txt'
NUMBER = None
NUM_ADJACENT_DIGITS = 5

def string_to_product(my_string):
    """ Convert string to product of it's digits. """
    res = 1
    for i in my_string:
        res *= int(i)

    return res

def get_number():
    """ Read number from file. """
    try:
        with open(FILE) as number_file:
            return number_file.readlines()[0]
    except IOError:
        print 'Error opening {0} file'.format(FILE)

NUMBER = get_number()

# Let's check if NUMBER has at least NUM_ADJACENT_DIGITS
if len(NUMBER) < NUM_ADJACENT_DIGITS:
    # If that's the case, we just need the product
    print string_to_product(NUMBER)
else:
    # We have at least NUM_ADJACENT_DIGITS, let's do some initial setup
    current_index = 0
    current_product = string_to_product(
        NUMBER[current_index:current_index + NUM_ADJACENT_DIGITS])

    max_product = string_to_product(
        NUMBER[current_index:current_index + NUM_ADJACENT_DIGITS])

    # Let's iterate over the digits,
    # until we have no more NUM_ADJACENT_DIGITS chunks left
    while current_index + 1 + NUM_ADJACENT_DIGITS < len(NUMBER):
        current_index += 1

        if NUMBER[current_index - 1] == '0':
            # If the first digit of the previous sequence was 0
            # we need to re-calculate
            current_product = string_to_product(
                NUMBER[current_index:current_index + NUM_ADJACENT_DIGITS])
        else:
            # If it wasn't, we just need to divide by it and nultiply bythe next
            current_product = (current_product /
                int(NUMBER[current_index - 1]) *
                int(NUMBER[current_index + NUM_ADJACENT_DIGITS - 1]))

        if current_product > max_product:
            max_product = current_product

    print max_product


