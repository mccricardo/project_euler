# Generate triangle numbers, starting on T286
# For each of them, check if it's also pentagonal and hexagonal

# Using some simplifications and the quadratic form we can get:
#	n = (1 + sqrt(1 + 24 * Pn)) / 6 
proc number_is_pentagonal {number} {
	set n [expr {(1 + sqrt(1 + 24 * $number)) / 6}]
	# Check if result is integer, and if so, we have a pentagonal number
	return [expr {$n == floor($n)}]	
}

# Using some simplifications and the quadratic form we can get:
#	n = (1 + sqrt(1 + 4 * Hn)) / 4 
proc number_is_hexagonal {number} {
	set n [expr {(1 + sqrt(1 + 8 * $number)) / 4}]
	# Check if result is integer, and if so, we have a pentagonal number
	return [expr {$n == floor($n)}]	
}

proc get_triangle_number {index} {
	return [expr {$index * ($index + 1) / 2}]
}

set index 286
while {!([number_is_pentagonal [get_triangle_number $index]] &&\
		[number_is_hexagonal [get_triangle_number $index]])
		} {
			incr index
		}
puts "Triangle number: [get_triangle_number $index]"