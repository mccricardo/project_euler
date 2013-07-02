#!/usr/bin/tclsh

proc is_palindrome {number} {
	set start 0
	set end [expr [string length $number] - 1]

	while {$start < $end} {
		if {[string index $number $start] != [string index $number $end]} {
			return 0
		}
		incr start
		incr end -1
	}
	return 1
}

set max 0
for {set i 100} {$i < 1000} {incr i} {
	for {set j 100} {$j < $i} {incr j} {
		set value [expr {$i * $j}]		
		if {[is_palindrome $value] && $value > $max} {
			set max $value
		}
	}
}

puts $max