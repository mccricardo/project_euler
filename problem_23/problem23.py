s = 0
abundant_numbers = set()
# 4179871

def get_divisors(number):
	return [x for x in range(1, number/2 +1) if number % x == 0]

for i in range(1,  28123):
	if sum(get_divisors(i)) > i: 
		abn.add(i)
	if not any((i-a in abundant_numbers) for a in abundant_numbers):
		s += i

print s
