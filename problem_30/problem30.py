"""
lambda: creates an anonymous. In our case to calculate the power of the number 
		and check if it is equal to the number.

filter: takes a boolean function (our lambda creation) and an itterable	and 
		constructs a list from from those elements of iterable for which the
		function returns true.

sum: adds them up.

How to get the upper bound 354294.

The biggest number 4-digit number that can be written as the sum of fifth 
powers of it's digits is 236196. So it is possible to get a 4-digit number
that can be written as the sum of fifth powers of their digits.

Let's do the same for next possible sizes:
	- 5-digit: 295245 -> possible
	- 6-digit: 354294 -> possible
	- 7-digit: 413343 -> impossible

So it is impossible to get a 7-digit number that can be written as the sum of 
fifth powers of their digits.
"""

print sum(filter(lambda i: i == sum([int(c)**5 for c in str(i)]), range(2,354294)))