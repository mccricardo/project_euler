# Only need to check this values.
# Why, for example:
#   - if number is divisible by 20 it's divisible by 2, 4, 5, 10
#   - if a number is divisible by 18 it's divisible by 2, 3, 6, 9, 18
#   - and so on
divide_by = [11, 13, 14, 16, 17, 18, 19, 20]

def find_multiple(step):	
	start = step

	while True:
		start += step
		if any(start % num for num in divide_by):
			continue
		else:
			return start


if __name__ == '__main__':
	# Because 2520 is the smallest number divisible by all number from 1..10
	# we can use this number as a start and step.
	print find_multiple(2520)