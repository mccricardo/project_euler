# Simplest way to do it: brute force aproach
# Start concatenating the number until we all the desired digit

def get_digit(digit):
	s = ''
	number = 1

	while len(s) < digit:
		s += str(number)
		number +=1

	return int(s[digit-1])
				

value = 1
digits = [1, 10, 100, 1000, 10000, 100000, 1000000]
for i in digits:
	value *= get_digit(i)

print "First aproach"
print value

# Still simple (brute force), but more efficient
# Instead of calculating the string every time we want a digit, calcute only fot the biggest one

def get_string(digit):
	s = ''
	number = 1

	while len(s) < digit:
		s += str(number)
		number +=1

	return s

value = 1
digits = [1, 10, 100, 1000, 10000, 100000, 1000000]
digits.sort()
number = get_string(digits[len(digits) - 1])
for i in digits:
	value *= int(number[i-1])

print "Second aproach"
print value
