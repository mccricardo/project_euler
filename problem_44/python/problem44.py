# From the problem: Pn = n(3n - 1) / 2
# Using a little math we get to:
#	3n**2 - n - 2Pn = 0
#
# To find if a number is Pentagonal we can solve that equation 
# using the quadratic form: 
#
# n = (-b +/- sqrt(b**2 - 4*a*c)) / 2*a
# where a = 3(coefficient of 3n**2), b = -1(coefficient of n), and c = -2*tn.
#
# Making the appropriate substitutions, we get:
#	n = (-(-1) +/- sqrt((-1)**2 - 4 * 3 * (-2) * Pn)) / 2 * 3
#
# Simplifying:
#	n = (1 +/- sqrt(1 + 24 * Pn)) / 6
#
# Because we don't want a negative number, we can rule out the "-" before the 
# sqrt, and so we get:
#	n = (1 + sqrt(1 + 24 * Pn)) / 6 

from math import sqrt

# Check if word is triangle, using the above formula for that.
def number_is_pentagonal(number):
	n = (1 + sqrt(1 + 24 * number)) / 6 	
	# Check if result is integer, and if so, we have a pentagonal number
	return n.is_integer()

