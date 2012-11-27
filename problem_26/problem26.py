"""
 - Fermat's little theorem: 1/d has a cicle of n digits if 10^n - 1 mod n = 0

 - If d is prime, than it can have a up to d - 1 repeating decimal digits

 - So, find the last prime p, under 1000, that has p - 1 digits
"""

from sieve_of_atkin import SieveOfAtkin

soa = SieveOfAtkin(1000)
primes = soa.getPrimes()

primes.sort() # just to be sure
primes.reverse()

for prime in primes:
	cycle = 1
	while (pow(10, cycle) - 1 ) % prime != 0:				
		cycle += 1

	if prime - cycle == 1:
		break

print prime

	