from math import pow
from operator import add

def sum_digits(b, p):
	value = pow(b, p)
	s = 0
	while value > 0:
		s += int(int(value) % int(10))
		value = int(int(value) / int(10))
		
	return s

print sum_digits(2, 1000)
