from sieve_of_atkin import SieveOfAtkin

soa = SieveOfAtkin(1000000)
primes = set(soa.getPrimes())
s = 0

def rotate(n):
	return int(str(n)[-1] + str(n)[:-1])

def isCircularPrime(n):
	v = rotate(n)	
	while n != v:		
		if v not in primes:
			return False
		v = rotate(v)

	return True


for i in primes:		
	if isCircularPrime(i):		
		s +=1		

print s
