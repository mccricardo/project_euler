memory = {1 : 1}

def find_sequence(start, end):
	longest_sequence = 0
	number = 0
	for i in range(start, end+1):
		aux = i
		seq = 1
		while(aux != 1):						
			if aux % 2 == 0:
				aux /= 2
			else:
				aux = aux * 3 + 1
		
			seq += 1

		if seq > longest_sequence:
			print "Longest so far: ", seq,i
			longest_sequence = seq
			number = i

	return number



def get_sequence_size(start):
	if start in memory:
		return memory[start]

	if start % 2 == 0:
		memory[start] = 1 + get_sequence_size(int(start / 2))
	else:
		memory[start] = 1 + get_sequence_size(int(start * 3 + 1))

	return memory[start]

def find_sequence_memoizing(value):	
	largest_so_far = 1
	highest = 0
	for i in range(1, value):
		temp = get_sequence_size(i)				
		if temp > largest_so_far:
			highest = i
			largest_so_far = temp
	return highest

print find_sequence_memoizing(1000000)

