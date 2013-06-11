# The n'th member of an arithmetic sequence can be found using:
#	an = a1 + (n - 1 ) * d
# where a1 is the firs number, n the index and d the diference between them.
# 
# Because we know d, and that we only have 3 members in the sequence:
#	- generate combinations of size 4
#	- for each of them, generate possible permutations
#	- get smallest prime, and from that get the other members of the sequence
#	- if they are both primes and also present in the permutations, 
#		we found the solution

from itertools import combinations_with_replacement, permutations
from math import sqrt

# Transform a tuple into a number
def tuple_to_number(tuple_number):
	number = 0
	number_size = len(tuple_number) - 1		
	for j in tuple_number:
		number += j * pow(10, number_size) 
		number_size -= 1

	return number

# Brute-force check check.
# Because numbers are small, not critical.
def is_prime(number):
	for i in xrange(2, int(sqrt(number))):
		if number % i == 0:
			return False
	return True

# Check combinations
def check_combination(comb):	
	# Transform tuples into numbers
	possible_perms = [tuple_to_number(p) for p in permutations(comb)]		
	for perm in possible_perms:	
		# If the number is prime, get the two other possible one's		
		if is_prime(perm) and perm > 1497:			
			a2 = perm + 3330
			a3 = perm + 2*3330
			# If they are prime and are also in the possible permutations, end
			if is_prime(a2) and is_prime(a3) and a2 in possible_perms and a3 in possible_perms:
				print str(perm) + str(a2) + str(a3)
				return True

# Generate all possible combinations of numbers with size 4
for comb in combinations_with_replacement([0,1,2,3,4,5,6,7,8,9], 4):		
	if check_combination(comb):
		break
