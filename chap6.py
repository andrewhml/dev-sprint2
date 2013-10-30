# Enter your answrs for chapter 6 here
# Name:Andrew Lee

import math

# Ex. 6.3

def area (radius):
	temp = math.pi * pow(int(radius), 2)
	return temp

def distance(x1, y1, x2, y2):
   	dx = x2-x1
   	dy = y2-y1
   	dsquared = pow(dx, 2) + pow(dy, 2)
   	d = math.sqrt(dsquared)
   	return d

def circle_area(xc, yc, xp, yp):
	radius = distance(xc, yc, xp, yp)
	result = area(radius)
	print result
	return result


#circle_area(1, 2, 4, 6)


def is_divisible(x, y):
	if x % y == 0:
		return True
	else:
		return False

def is_divisible(x, y):
	return x % y == 0

#is_divisible(6, 4)

def is_between(x, y, z):
	if x <= y and y <= z:
		return True
	else:
		return False

def factorial(n):
	if not isinstance(n, int):
		print 'Factorial is only defined for integers.'
		return None
	elif n < 0:
		print 'Factorial is not defined for negative integers.'
		return None
	elif n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result



# Ex. 6.6

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1: -1]

# Wrong answer still need help understanding where this goes wrong.
#def is_palindrome(word):
#	n = len(word)
#	if middle(word) == '':
#		return None
#	elif word[0] == word[n-1]:
#		word = middle(word)
#		is_palindrome(word)
#		result = True
#		return result
#	else:
#		result = False
#		return result

def is_palindrome(word):
	if len(word) <= 1:
		return True
	if first(word) != last(word):
		return False
	return is_palindrome(middle(word))

#print is_palindrome('moooooooiooom')
#print is_palindrome('noon')
#print is_palindrome('racecar')


# Ex 6.7
def is_power(a,b):
	if a%b == 0:
		if a/b == 1:
			return True
		else:
			c = a/b
		return is_power(c, b)
	else:
		return False


#print is_power(27, 3)

# Ex 6.8
def gcd(a,b):
	if a > b:
		if a%b == 0:
			return b
		if a%b != 0:
			return gcd(b,a%b)
	if b > a:
		if b%a == 0:
			return a
		if b%a != 0:
			return gcd(a,b%a)

print gcd(1071, 462)
print gcd(234, 3009)
print gcd(200, 1000)
