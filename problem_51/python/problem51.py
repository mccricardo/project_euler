from itertools import combinations
from math import sqrt
import sys

def is_prime(number):
	for n in xrange(2, int(sqrt(number)) + 1):
		if number % n == 0:
			return False

	return True

def get_combinations(size):
	return combinations([x for x in xrange(size)], size -1)

def num_replace(s_number, positions, digit):
	res = ""
	for i in xrange(len(s_number)):
		if i in  positions:
			res += str(digit)
		else:
			res += s_number[i]

	return res


start = 100001
while True:
	start += 2

	if is_prime(start):
		str_start = str(start)	

		for i in xrange(2, len(str_start)):
			primes = [start]
			combs = get_combinations(i)

			for c in combs:			
				for j in xrange(1, 10):			
					num = num_replace(str_start, c, j)
				
					if is_prime(int(num)):
						primes.append(int(num))
					
					print primes

					if len(primes) > 7:
						print min(primes)
						sys.exit()




