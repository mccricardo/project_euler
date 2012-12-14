from sieve_of_atkin import SieveOfAtkin

soa = SieveOfAtkin(800000)
primes = set(soa.getPrimes())

def truncableRight(val):
	s = str(val)
	for i in range(len(s), 0, -1):
		if int(s[:i]) not in primes:
			return False
	return True

def truncableLeft(val):
	s = str(val)
	for i in range(len(s)):
		if int(s[i:]) not in primes:
			return False
	return True

result = 0
for i in (i for i in primes if i > 7):	
	if truncableRight(i) and truncableLeft(i):
		result += i

print result