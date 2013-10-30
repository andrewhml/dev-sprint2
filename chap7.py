# Enter your answrs for chapter 7 here
# Name: Andrew Lee

import math

def countdown(n):
	while n > 0:
		print n
		n = n-1
	print 'Blastoff!'

#countdown(10)

def sequence(n):
	while n != 1:
		print n,
		if n%2 == 0:
			n = n/2
		else:
			n = n*3+1

#sequence(3)

def square_estimate(a):
	x = a/2
	while True:
		print x
		y = (x + a/x) / 2
		if abs(y-x) < epsilon:	#think python says epsilon is a term but it is not recognized
			break
		x = y
	print x

#square_estimate(25)


# Ex. 7.5

def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result

def estimate_pi():

	estimate = 0
	k = 0
	constant = 2 * math.sqrt(2) / 9081
	while True:
		num = factorial(4*k) * (1103 + 26390*k)
		den = factorial(k)**4 * 396**(4*k)
		temp = constant * num / den
		estimate += temp
		print k
		
		if abs(temp) < 1e-15:
			break
		k += 1
	
	return 1 / estimate

print estimate_pi()
# How many iterations does it take to converge?
# Takes 3 iterations to converge