# Generate triangle numbers, starting on T286
# For each of them, check if it's also pentagonal and hexagonal

from math import sqrt

# Using some simplifications and the quadratic form we can get:
#	n = (1 + sqrt(1 + 24 * Pn)) / 6 
def number_is_pentagonal(number):
	n = (1 + sqrt(1 + 24 * number)) / 6 	
	# Check if result is integer, and if so, we have a pentagonal number
	return n.is_integer()


# Using some simplifications and the quadratic form we can get:
#	n = (1 + sqrt(1 + 8 * Hn)) / 4 
def number_is_hexagonal(number):
	n = (1 + sqrt(1 + 8 * number)) / 4 
	# Check if result is integer, and if so, we have an hexagonal number
	return n.is_integer()

def get_triangle_number(index):
	return index * (index + 1) / 2

index = 286
while not (number_is_pentagonal(get_triangle_number(index)) and 
			number_is_hexagonal(get_triangle_number(index))):
	index +=1

print "Triangle number:", get_triangle_number(index)