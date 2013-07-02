#!/usr/bin/python

sum = 2
prev_1 = 1
prev_2 = 2

while prev_2 < 4000000:
	curr = prev_1 + prev_2
	if curr % 2 == 0:
		sum += curr

	prev_1 = prev_2
	prev_2 = curr

print sum