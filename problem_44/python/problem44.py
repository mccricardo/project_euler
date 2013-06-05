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
from sys import maxint

# Check if word is triangle, using the above formula for that.
def number_is_pentagonal(number):
	n = (1 + sqrt(1 + 24 * number)) / 6 	
	# Check if result is integer, and if so, we have a pentagonal number
	return n.is_integer()

# The general aproach will be to generate pentagonal numbers and check the
# difference and sum between the current one and the previouns one's, until 
# we find the first pair that matches the problem's criteria.
#
# That's enough to get the minimal difference, because, as we can see the
# difference between a pentagonal and the following one grows quadratically:
# 	Pn = n(3n - 1) / 2 = (3 * n**2 - n ) / 2
#
# What this means is that the difference between the current pentagonal number 
# and it's predecessors will always be smaller than the difference between the
# current pentagonal number and any of it's successors.
pentagonal_numbers = []
n = 0
while True:
	n += 1
	p = n * (3 * n - 1) / 2
	for j in pentagonal_numbers:
		if number_is_pentagonal(abs(p - j)) and number_is_pentagonal(p + j):
			print "The minimized diference is", abs(p - j)
			exit(0)
	pentagonal_numbers.insert(0, p)

