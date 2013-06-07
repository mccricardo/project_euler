# Works, simple and fast.
# For bigger problems, we could have a problem. 
# Implement a proper exponentiation algorithm.

number = 0
for i in xrange(1, 1001):
	number += i**i

print number
str_number = str(number)
print str_number[len(str_number) - 10:]