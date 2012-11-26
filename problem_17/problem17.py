number = {
    1:'one',2:'two',3:'three',4:'four',5:'five',
    6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
    11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
    16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',
    30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
    80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}

# strig.replace(' ', '')

def get_words(value):
	number_word = ''	
	unity = 0
	dozen = 0
	hundred = 0
	thousand = 0

	n = value
	unity = value % 10
	value /= 10

	if value != 0:
		dozen = value % 10
		value /= 10

	if value != 0:
		hundred = value % 10
		value /= 10

	if value != 0:
		thousand = 1000

		
	if thousand != 0:
		number_word += 'onethousand'
	
	elif n < 20:
		number_word += number[n]
	else:
		if hundred != 0:
			number_word += number[hundred] + 'hundred'
			if dozen != 0 or unity != 0:
				number_word += 'and' 	
			
		if dozen > 1:
			number_word += number[dozen*10]
		
		if dozen == 1 and unity == 0:
			number_word += 'ten'
		elif unity != 0:
			if dozen == 1:
				number_word +=  number[10 + unity]
			else:
				number_word += number[unity]

	return number_word


string = ''
for i in range(1, 1001):
	string += get_words(i)



print len(string)