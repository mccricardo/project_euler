with open('names.txt', 'r') as f:
	names = sorted(f.read().replace('"', '').split(','), key=str)

letters = dict([(chr(65+i), i+1) for i in range(91-65)])

def get_word_score(word):
	score = 0
	for l in word:
		score += letters[l]

	return score

total_score = 0
for i in range(len(names)):

	word_score = get_word_score(names[i])
	total_score += (word_score * (i+1)) 

print total_score






