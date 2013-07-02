#!/usr/bin/python

def is_palindrome(number):
	start = 0
	end = len(number) -1
	
	while start < end:		
		if number[start] != number[end]:
			return 0

		start +=1
		end -= 1

	return 1

max = 0
for i in xrange(100, 1000):
	for j in xrange(100, i):
		value = i * j
		if is_palindrome(str(value)) and value > max:
			max = value

print max


