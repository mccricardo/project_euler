"""
Brute Force aproach.

'Trick' is to limit the bounderies.

Factorians: http://en.wikipedia.org/wiki/Factorion

"""

def fact(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n * fact(n-1)

def fact_sum(n):
	v = 0

	while n != 0:			
		v += fact(n % 10)
		n /= 10

	return v

v = 0
for i in range(3, 100000):		
	if fact_sum(i) == i:
		print i
		v +=1
		
print v