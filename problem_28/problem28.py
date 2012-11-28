"""
Let's consider tours in the spiral.

For each tour in the spiral, we add 4 numbers: 3, 5, 7 , 9.

For the first tour, the difference between values to add is 2.

For the following tours, the increment is:
	the difference between numbers in the previous tour + 2.

As an example, on the second tour: 2 + 2 = 4, so the for next numbers are:
	13, 17, 21, 25.

We stop when we reach the biggest possible number.

"""

max_value = 1001 * 1001
nsum = 1
value_to_add = 1
increment = 2
numbers_in_tour = 0

while value_to_add < max_value:
	if numbers_in_tour == 4:
		numbers_in_tour, increment = 0, increment + 2

	value_to_add += increment
	nsum += value_to_add	
	numbers_in_tour += 1

print nsum
