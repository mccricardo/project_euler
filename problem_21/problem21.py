def get_divisors(number):
	return [x for x in range(1, number/2 +1) if number % x == 0]


amicable_sum = 0
for i in range (1, 10000):
	s1 = sum(get_divisors(i))
	s2 = sum(get_divisors(s1))

	if i == s2 and i != s1:
		amicable_sum += i

print amicable_sum
