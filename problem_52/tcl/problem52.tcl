# General aproach:
#	- from a base number, get it's multiples (2x...6x)
#	- make them a string
# 	- sort them
#	- see if they match :)

set start 2
set num_count 0
while {$num_count < 5} {
	# Tansform string into list and sort it
	set sorted_start [lsort -integer [split $start {}]]
	for {set i 2} {$i < 7} {incr i} {		
		# Get multiple and sort it		
		set sorted_multiple [lsort -integer [split [expr {$start * $i}] {}]]
		# Check if they're not the same
		if {$sorted_start != $sorted_multiple} {
			set num_count 0
			break
		# If  they are, count it
		} else {
			incr num_count
		}
	}
	incr start	
}

puts [incr start -1]