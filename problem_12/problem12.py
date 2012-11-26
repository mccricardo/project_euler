from math import sqrt
from sieve_of_atkin import SieveOfAtkin

def NumberOfDivisors(number):
    nod = 0
    s = int(sqrt(number))

    for i in range(1, s):
 		if number % i == 0:
 			nod += 2

    if s * s == number:
    	nod -= 1

    return nod

def PrimeFactorisationNoD(number, prime_list): 
    nod = 1
    remain = number
 	
    for i in range(len(prime_list)):
    	# In case there is a remainder this is a prime factor as well
        # The exponent of that factor is 1
        if prime_list[i] * prime_list[i] > number:
        	return nod * 2

        exponent = 1
        while remain % prime_list[i] == 0:
        	exponent += 1
        	remain /= prime_list[i]
        
        nod *= exponent

        # If there is no remainder, return the count
        if remain == 1:
        	return nod

    return nod
   
number = 0
i = 1
soa = SieveOfAtkin(75000)
prime_list = soa.getPrimes()

""" 
while NumberOfDivisors(number) < 500:		
	number += i
	i +=1
"""
while PrimeFactorisationNoD(number, prime_list) < 500:		
	number += i
	i +=1

print number
