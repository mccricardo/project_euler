# Works, simple and fast.
# For bigger problems, we could have a problem. 
# Implement a proper exponentiation algorithm.

set number 0
for {set i 1} {$i <= 1000} {incr i} {
	set number [expr {$number + $i**$i }]
}

# Because in Tcl everything is a string, we can just use numer :)
puts [string range $number [expr [string length $number] -10] [string length $number]]