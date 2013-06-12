# Simple aproach:
#	- start with zero numbers that have 4 prime factors.
#	- for each number, get number of prime factors
#	- if 4, increment current number of 4 prime factors
#	- if not, set to 0
#	- stop when we have 4

# We don't need the actual factorization, only the number of factors
def distinct_prime_factors(number):
	distinct_prime_factors = 0
	for p in primes_list:		
		if number % p == 0:
			distinct_prime_factors += 1
	return distinct_prime_factors

number_of_distinc_primes = 0
number = 2
primes_list = set()
while number_of_distinc_primes != 4 :
	# If it's prime, no need to try it
	if all(number % p for p in primes_list):
		primes_list.add(number)
		number_of_distinc_primes = 0
	else:		
		# If number of distinct primes is 4, count it
		if distinct_prime_factors(number) == 4:				
			number_of_distinc_primes += 1
		# If not, reset to 0
		else:
			number_of_distinc_primes = 0		
	number += 1	

print "The first number is:", number - 4
