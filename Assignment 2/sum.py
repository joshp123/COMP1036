# sum.py
# Asks user to add up 2 random numbers
# Author:     J Palmer
# Created on: 2012-03-05
# Version:    1.2 (protected against non-integer input)

import random
numbers = tuple([random.randint(1,100) for x in xrange(2)])
while True:
		try:
			n_in = int(raw_input("Solution to %d + %d = " % numbers))
			break
		except ValueError:
			print 'This is not a valid integer! Try again.'
print "You are right!" if n_in == sum(numbers) else "you're wrong :( The correct answer was " + repr(sum(numbers)) + "."