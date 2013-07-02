#!/usr/bin/python
from math import sqrt

limit = 600851475143
primes = set()

for i in xrange(2, int(sqrt(limit)) + 1):
	# If "i" divides "limit" and none of primes divide "i", so this is a prime 
	# for the "limit" factorization.
	if limit % i == 0 and all(i % p for p in primes):
		primes.add(i)

print max(primes)
