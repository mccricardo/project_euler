# Start with prime 3.
# 
# If none of the primes in prime_list divide n, then it's also prime and 
# add it to the list.
#
# If not, let's put the problem formula with another aspect:
#	prime = odd_number - 2 * pow(i, 2)
#
# This means that we can check if any of the primes can be constructed in terms
# of the odd number. If not, we found our number.

# If number is not divisable by any prime, it's also prime
proc check_prime {number primes_list} {
	foreach prime $primes_list {
		if {![expr {$number % $prime}]} {
			return 1
		}
	}
	return 0
}

# Check if we can get any of the primes user the current number
proc check_number {number primes_list} {
	foreach prime $primes_list {		
		for {set i 1} {$i < $number} {incr i} {
			if {$prime == [expr {$number - 2 * pow($i, 2)}]} {
				return 0
			}
		}
	}	
	return 1
}

set number 3
set primes_list {}
while 1 {
	if {![check_prime $number $primes_list]} {
		lappend primes_list $number
	} else {
		if {[check_number $number $primes_list]} {
			break
		}
	}
	incr number 2
}

puts "The number is: $number"
