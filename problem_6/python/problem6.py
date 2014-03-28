#!/usr/bin/env python

print (sum([p for p in xrange(1,101)]))**2 - \
	sum(map(lambda x: x**2, [p for p in xrange(1,101)]))