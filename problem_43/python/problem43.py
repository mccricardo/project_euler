# Generate pandigital numbers, using permutations.
# Check the property.
from itertools import permutations

def tuple_to_number(tuple_number):
	number = 0
	number_size = len(tuple_number) - 1		
	for j in tuple_number:
		number += j * pow(10, number_size) 
		number_size -= 1

	return number

# Check the problem property
def check_property(tuple_number):
	if (tuple_to_number(tuple_number[1:4]) % 2 == 0 and 
			tuple_to_number(tuple_number[2:5]) % 3 == 0 and
			tuple_to_number(tuple_number[3:6]) % 5 == 0 and
			tuple_to_number(tuple_number[4:7]) % 7 == 0 and
			tuple_to_number(tuple_number[5:8]) % 11 == 0 and
			tuple_to_number(tuple_number[6:9]) % 13 == 0 and
			tuple_to_number(tuple_number[7:10]) % 17 == 0):
		return True
	
	return False

possible_digits = [9,8,7,6,5,4,3,2,1,0]
number_sum = 0
# No need to check if number is pandigital; only permutations are generated.
for i in permutations(possible_digits):		
	if check_property(i):
		number_sum += tuple_to_number(i)

print "Sum of all 0 to 9 pandigital numbers with this property:", number_sum
			