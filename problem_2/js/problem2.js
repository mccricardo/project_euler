function fib(limit) {
	sum = 2;
	prev_1 = 1;
	prev_2 = 2

	while (prev_2 < limit) {
		curr = prev_1 + prev_2;
		if (curr % 2 == 0) {
			sum += curr;
		}
		prev_1 = prev_2;
		prev_2 = curr;
	}

	return sum;
}

console.log(fib(4000000))