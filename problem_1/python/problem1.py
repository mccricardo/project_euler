result = 0
limit = 1000
for i in xrange(1, limit):
	if i % 3 == 0 or i % 5 == 0:
		result += i

print result