function is_palindrome(str_number) {
	// JS strings are immutable.
	// To reverse it: 
	//   - transform it in an array
	//   - reverse the array 
	//   - join it again
	if (str_number === str_number.split('').reverse().join('')) {
		return true;
	}

	return false;
}

function largest_palindrome(start, end) {
	// Just to be sure start can be the maximum
	var max = start - 1;

	// Two cicles because we need all possible combinations
	for (var i = start; i < end; i++) {
		for (var j = start; j < i; j++) {
			value = i * j;
			if (is_palindrome(value.toString()) &&  value > max) {
				max = value
			}
		}
	}

	return max;
}

console.log(largest_palindrome(100, 1000));