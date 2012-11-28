"""
Set: Unordered collections of unique elements.

Generate all possible numbers and get length of the set.
"""
from math import pow

print len(set(pow(i, j) for i in range(2, 101) for j in range(2,101)))

