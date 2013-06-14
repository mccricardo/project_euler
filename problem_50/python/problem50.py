from sieve_of_atkin import SieveOfAtkin
from itertools import combinations

# The intended value has to be in the primes list, meaning < limit.
# The biggest possible sequence will involve the smallest primes that add up
# to limit.
def get_max_sequence():
	seq = 0
	s = 0
	while(s < limit):
		s += primes_list[seq]
		seq +=1
	return seq	

limit = 1000000
# Generate list of primes.
soa = SieveOfAtkin(limit)
primes = set(soa.getPrimes())
# Because result is given as a set, turn into a list and sort it.
primes_list = list(primes)
primes_list.sort()
# We know that the sequence will have a maximum:
#	- only consider sequences of that size or smaller
for l in xrange(get_max_sequence(), 1, -1):				
	i = 0
	value = sum(primes_list[i:i+l])
	# Because the value has to be in primes_list, no need to check values bigger
	# than the limit.
	while value < limit:
		if value in primes:
			print l, value		
			exit(0)
		i +=1
		value = sum(primes_list[i:i+l])
