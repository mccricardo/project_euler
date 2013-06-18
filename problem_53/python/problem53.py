# Just using Python's factorial funciotn from the math lib and 
# the combinatorial formula.

from math import factorial

def combinations_n_r(n, r):
	return factorial(n) / (factorial(r) * factorial(n - r))

limit = 1000000
count = 0
# Just go through the possible values, and count the one's > limit
for n, r in [(n,r) for n in xrange(23, 101) for r in xrange(1, n + 1)]:
	if combinations_n_r(n, r) > limit:
		count += 1

print "Number of combinations:", count