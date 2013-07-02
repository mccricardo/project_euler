#!/usr/bin/tclsh

set limit 600851475143
set primes {}

for {set i 2}  {$i < sqrt($limit)} {incr i} {
	set is_prime 1
	# If "i" divides "limit" and none of primes divide "i", so this is a prime 
	# for the "limit" factorization.
	if {[expr {$limit % $i}] == 0} {
		foreach prime $primes {
			if {[expr {$i % $prime}] == 0} {
				set is_prime 0
				break
			}
		}

		if {$is_prime} {
			lappend primes $i
		}
	}
}

# No need to check for maximum: the last inserted value is the maximum
puts [lindex $primes [expr [llength $primes] - 1]]