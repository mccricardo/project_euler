// Only need to check this values.
// Why, for example:
//   - if number is divisible by 20 it's divisible by 2, 4, 5, 10
//   - if a number is divisible by 18 it's divisible by 2, 3, 6, 9, 18
//   - and so on
var divide_by = [11, 13, 14, 16, 17, 18, 19, 20]

function find_multiple(step) {
	var not_found = true;
	var start = step;
	
	while (not_found) {		
		start += step;
		for (var i in divide_by) {
			if (start % divide_by[i] != 0) {				
				not_found = true;
				break;
			}
			not_found = false;
		}		
	}

	return start;
}

console.log(find_multiple(2520));