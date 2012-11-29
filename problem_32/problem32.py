"""
Brute Force aproach.

'Trick' is to limit the bounderies.

For multiplicand * multiplier = product the biggest possible number for 'product' has 5 
digists, because it is impossible to generate a number with more than 5 digits with the 
remaining 4 digits. So product < 100000.
"""

products = set()

def is9Pandigital(a, b):
	numbers = str(a) + str(b) + str(a*b)
	if len(numbers) != 9:
		return False
	else:
		for i in xrange(1,10):
			if str(i) not in numbers:
				return False
	return True

for i in xrange(0, 100000):
    for j in xrange(i, 100000):    	
    	if len(str(i) + str(j) + str(i * j)) > 9:
    		break
    	if is9Pandigital(i, j):
    		products.add(i * j)

print sum(products)