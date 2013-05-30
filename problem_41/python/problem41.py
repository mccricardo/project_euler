# General aproach:
#
# Generate pandigital numbers in buckets:
#	 - start with numbers with biggest possible size (9) and down from there
#
# Starting from the biggest in each bucket check if it's prime
#
# Stop as soon as the first one is found

import itertools
from math import sqrt

def tupleToNumber(tuple_number):
	number = 0
	number_size = len(tuple_number) - 1		
	for j in tuple_number:
		number += j * pow(10, number_size) 
		number_size -= 1

	return number

# Naive (brute-force) implementation for prime checking.
# Because the biggest possible number is 987654321, and it's sqrt approximately 31426
# this aproach is not problematic.
# For more efficient solutions, you can check the link below for guidance:
#	- http://en.wikipedia.org/wiki/Primality_test
def isPrime(number):
	for i in xrange(2, int(sqrt(number))):
		if number % i == 0:
			return False
	return True

digits = 0
possible_digits = [9,8,7,6,5,4,3,2,1]
while digits < len(possible_digits):
	# No need to check if number is pandigital, because only permutations are generated.
	# Also, numbers are already sorted.
	for i in itertools.permutations(possible_digits[digits:]):		
		if isPrime(tupleToNumber(i)):
			print tupleToNumber(i), "is the biggest possible prime."
			exit(0)
	digits += 1
