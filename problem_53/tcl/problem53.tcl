# Calculate factorial
proc factorial {n} {
	set result 1
	for {set i $n} {$i > 0} {incr i -1} {
		set result [expr {$result * $i}]
	}
	return $result
}

# Combinatorial formula
proc combinations_n_r {n r} {
	return [expr {[factorial $n] / ([factorial $r] * [factorial [expr {$n - $r}]])}]
}

set limit 1000000
set count 0
for {set n 23} {$n < 101} {incr n} {
	for {set r 1} {$r <= $n} {incr r} {
		if {[combinations_n_r $n $r] > $limit} {
			incr count
		}
	}
}

puts "Number of combinations: $count"

