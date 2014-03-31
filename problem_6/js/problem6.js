// Create a list with numbers up to 100
function integegerGenerator(limit) {
	var array = [];
	for (var i = 1; i <= limit; i++) {
		array.push(i);
	}

	return array;
}

function difference (limit) {
	sum_of_squares = 0;
	square_of_sum = 0;

	// Itereate over the list onlye once and do calculations along the way
	var num_array = integegerGenerator(100);
	for (var i in num_array) {
		sum_of_squares += Math.pow(num_array[i], 2);
		square_of_sum += num_array[i];
	}

	// At the end, we need to square the sum
	square_of_sum = Math.pow(square_of_sum, 2);	
	
	return square_of_sum - sum_of_squares;
}

console.log(difference(100));
