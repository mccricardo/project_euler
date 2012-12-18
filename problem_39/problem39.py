"""
Pythagorean Theorem says. a^2 + b^2 = c^2.

The perimiter is: a + b + c = p. So c = p - a - b

Making the substitution we get:  a^2 + b^2 = (p - a - b)^2. If we simplyfy we get:
	b = p * (p - 2 * a) / 2 * (p - a)

Because b has to be an integer, we have that p * (p - 2 * a) % 2 * (p - a) == 0.

There we have a way to check for a right triangle.

An optimization comes from a Pythagorean Theorem corollary that states that 
a + b > c. So, we only need to evaluate values until p / 4.


Another optimization comes from the fact that no matter which integral values 
we choose for a, b and c such that a^2 + b^2 = c^2 the perimeter will be even.
So, we only need to consider even perimeters.
"""

myMax = 0
myLimit = 1000
 
for p in range(myLimit / 2, myLimit, 2):
  count = 0;
  
  for a in range(2, p/4 +1):
    if  p*(p - 2*a) % (2*(p-a)) == 0: 
    	count += 1

    if count > myMax: 
    	myMax, pMax = count, p
 
print pMax