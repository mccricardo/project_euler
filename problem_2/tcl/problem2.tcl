#!/usr/bin/tclsh

set sum 2
set prev_1 1
set prev_2 2

while {$prev_2 < 4000000} {
	set curr [expr $prev_1 + $prev_2]
	if {[expr {$curr % 2}] == 0} {
		set sum [expr {$sum + $curr}]
	}
	set prev_1 $prev_2
	set prev_2 $curr
}

puts $sum