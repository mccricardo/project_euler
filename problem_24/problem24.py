from itertools import permutations

a = list(permutations([0,1,2,3,4,5,6,7,8,9], 10))[999999]

print ''.join((str(b) for b in a))