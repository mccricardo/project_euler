# Start with prime 3.
# 
# If none of the primes in prime_list divide n, then it's also prime and 
# add it to the list.
#
# If not, let's put the problem formula with another aspect:
#	prime = odd_number - 2 * pow(i, 2)
#
# This means that we can check if any of the primes can be constructed in terms
# of the odd number. If not, we found our number.

number = 3
primes_list = set()
while True :
   if all(number % p for p in primes_list) :
      primes_list.add(number)
   else :
      if not any((number-2*pow(i,2)) in primes_list for i in xrange(1, number)):
         break
   number += 2

print "The number is:", number

