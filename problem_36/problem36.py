def isPalindrome(s):
	return True if str(s) == str(s)[::-1] else False 

def decToBin(val):
	return bin(val)[2:]

result = 0

print sum((i for i in range(1000000) if isPalindrome(i) and isPalindrome(decToBin(i))))


