from sieve_of_atkin import SieveOfAtkin
from math import sqrt, pow

soa = SieveOfAtkin(1000)
primes = soa.getPrimes()
nmax = 0

# Taken from here: http://blog.dreamshire.com/2009/03/26/94/
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(sqrt(n))
  f = 5
  while f <= r:
      if n%f == 0: return False
      if n%(f+2) == 0: return False
      f +=6
  return True


# b has to be prime, so that when n = 0 the result is prime
for a,b in [(a,b) for a in range(-1000, 1000) for b in primes]:
    n = 1
    while is_prime(pow(n,2) + a*n + b): 
        n += 1

    if n > nmax:
        nmax, product = n, a * b

print product