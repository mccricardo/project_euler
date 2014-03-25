function largest_prime_factor(number) {
	var primes = new Array();

	for (var i=2; i<Math.sqrt(number); i++) {
		var is_prime = 1;
		// Check if  i divides number.		
		if (number % i == 0) {
			// Chek if any of the primes we have already divide it.
			for (var p in primes) {				
				if (i % primes[p] == 0) {
					is_prime = 0;
					break;
				}
			}

			// If i divides number an none of the primes we have already divide
			// it, we have a new prime for our factorization.
			if (is_prime) {
				primes.push(i);
			}			
		}	
	}

	return primes[primes.length - 1]
}

console.log(largest_prime_factor(600851475143));