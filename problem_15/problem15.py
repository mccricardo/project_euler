"""
Grid n x m: every path will have n * m moves without backtracking.
Total moves = n + m

Calculate number of possible moves (with only 2 possible moves per move): 
	Combination formula

		 	  n!
C(n,r) = --------------
		 r! * (n - r)!

"""
from math import factorial

def num_paths(width, height):
	n = width + height
	r = width # or height

	return factorial(n) / (factorial(r) * factorial(n - r))

print num_paths(20, 20)
