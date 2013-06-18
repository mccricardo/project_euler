# General aproach:
#	- from a base number, get it's multiples (2x...6x)
#	- make them a string
# 	- sort them
#	- see if they match :)

start = 2
num_count = 0
# While we don't have all 5 possible multiples, keep on going
while num_count != 5:
	start_str = sorted(str(start))
	# Generate multiples
	for numbers in [start*i for i in range(2,7)]:		
		# Check if the sorted multiple matches the base number
		if start_str != sorted(str(numbers)):
			num_count = 0
			break
		# If it does, count it
		else:			
			num_count += 1
	start += 1

print start - 1