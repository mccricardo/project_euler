# From the problem: tn = 1/2 n(n+1).
# With a bit of mathemetics we get to:
#	n**2 - n - 2*tn = 0
#
# To solve that equation, we can use the quadratic Formula:
# 
#	n = (-b +/- sqrt(b**2 - 4*a*c)) / 2*a
# 
# where a = 1(coefficient of n**2), b = -1(coefficient of n**2), and c = -2*tn.
# Making the appropriate substitutions, we get:
#	n = (-1 +/- sqrt(1**2 - 4 * 1 * -2*tn)) / 2*1
#
# Simplifying:
#	n = (-1 +/- sqrt(1 + 8*tn)) / 2
#
# Because we don't want a negative number, we can rule out the "-" before the 
# sqrt, and so we get:
#	n = (-1 + sqrt(1 + 8*tn)) / 2
#
# Given all of these, if we transform a word into it's value, 
# we can find out if it is a triangle word.

# Array to transform each letter on it's corresponding value
array set LETTER_TO_NUMBER {A 1 B 2 C 3 D 4 \
							E 5	F 6 G 7 H 8 \
							I 9 J 10 K 11 L 12 \
							M 13 N 14 O 15 P 16 \
							Q 17 R 18 S 19 T 20 \
							U 21 V 22 W 23 X 24 \
							Y 25 Z 26 \
							}

# To transform word into number, go through each letter and add it's value
proc word_to_number {word} {
	global LETTER_TO_NUMBER
	set value 0
	for {set i 0} {$i < [string length $word]} {incr i} {
		incr value $LETTER_TO_NUMBER([string index $word $i])
	}
	return $value
}

# Check if word is triangle, using the above formula for that.
proc word_is_triangle {number_of_word} {
	set n [expr {(-1 + sqrt(1 + 8*$number_of_word)) / 2 }]
	
	# Check if result is integer, and if so, we have a triangle word :-)
	return [expr {$n == floor($n)}]	
}

# true words, split on the ','
set fp [open "../words.txt" r]
set file_data [split [read $fp] ","]  
close $fp

set number_of_triangle_words 0
foreach i $file_data {	
	# Trim the '"'
	set number_of_word [word_to_number [string trim $i "\""]]	
	# Check if it's triangle, and if so count it
	if  {[word_is_triangle $number_of_word]} {
		incr number_of_triangle_words
	}	
}

puts "Number of triangle words: $number_of_triangle_words"