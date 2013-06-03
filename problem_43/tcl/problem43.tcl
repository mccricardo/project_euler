# Generate pandigital numbers, using permutations.
# Check the property.

# Like foreach but call 'body' for every permutation of the elements
# in the list 'items', setting the variable 'var' to the permutation.
#   
# Cortesy of Salvatore Sanfilippo (http://wiki.tcl.tk/11262).
proc foreach_permutation {var items body} {
    set l [llength $items]
    if {$l < 2} {
       uplevel [list set $var [lrange $items 0 0]]
       uplevel $body
    } else {
       for {set j 0} {$j < $l} {incr j} {
           foreach_permutation subcomb [lreplace $items $j $j] {
               uplevel [list set $var [concat [lrange $items $j $j] $subcomb]]
               uplevel $body
           }
       }
    }
}

proc tuple_to_number tuple {
	set number 0
	set number_size [expr [llength $tuple] -1]	
	foreach n $tuple {
		set number [expr $number + [expr $n * pow(10, $number_size)]]
		incr number_size -1		
	}
	return [expr int($number)]
}

proc check_property tuple {	
	if {![expr [expr [tuple_to_number [lrange $tuple 1 3]] % 2]] &&\
		![expr [expr [tuple_to_number [lrange $tuple 2 4]] % 3]] &&\
		![expr [expr [tuple_to_number [lrange $tuple 3 5]] % 5]] &&\
		![expr [expr [tuple_to_number [lrange $tuple 4 6]] % 7]] &&\
		![expr [expr [tuple_to_number [lrange $tuple 5 7]] % 11]] &&\
		![expr [expr [tuple_to_number [lrange $tuple 6 8]] % 13]] &&\
		![expr [expr [tuple_to_number [lrange $tuple 7 9]] % 17]]\
		} {
		return 1
	} 
	return 0
}

set final_value 0
foreach_permutation p {9 8 7 6 5 4 3 2 1 0} {
	if {[check_property $p]} {
		incr final_value [tuple_to_number $p]
	}
}

puts "Sum of all 0 to 9 pandigital numbers with this property: $final_value"

