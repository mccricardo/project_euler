i = 1
fib = 1
n1 = 0
n2 = 1

while len(str(fib)) < 1000:
	fib = n1 + n2
	n1 = n2
	n2 = fib
	i += 1

print i