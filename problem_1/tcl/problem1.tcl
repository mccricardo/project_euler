proc multiples {limit} {
	set result 0
	for {set i 1} {$i < $limit} {incr i} {
		if {[expr {$i % 3}] == 0 || [expr {$i % 5}] == 0} {
			set result [expr {$result + $i}]
		}
	}
	return $result
}

puts [multiples 1000]