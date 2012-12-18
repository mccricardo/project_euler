"""
Note: ++ represents concatenation of strings.

A number of the form  (9* x 1) ++ (9* x 2) and (9** x 1) ++ (9** x 2) 
will never yield a 9 digit number.

But a number of the form (9*** x 1) ++ (9*** x 2).

A number resulting from a number with zeros will never be pandigital, so 9123 is the 
smallest possible.

No need to consider n > 2: it will yield numbers with length > 9.

"""

def is9Pandigital(val):	
	if len(val) != 9:
		return False
	else:
		for i in xrange(1,10):
			if str(i) not in val:
				return False
	return True

for n in range(9999, 9123, -1):
  p = str(n*1) + str(n*2)
  if is9Pandigital(p): 
    print p
    break