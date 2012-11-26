with open('numbers.txt', 'r') as f:
	data = [int(n) for  n in f.readlines()]

S = sum(data)
 
print repr(S)[:10]