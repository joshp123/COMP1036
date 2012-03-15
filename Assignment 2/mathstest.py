# mathstest.py
# Random sum thing but catches non-ints and repeats 10 times and keeps score
# Author:     J Palmer
# Created on: 2012-03-05
# Version:    1.2 made it slightly more elegant - instead of using global variables and incrementing them, the askrand() function returns a value and it works with that 


import random

def AskRand(): # Returns 1 if answered correctly, 0 if answered incorrectly
	numbers = tuple([random.randint(1,100) for x in xrange(2)])
	while True:
		try:
			n_in = int(raw_input("Solution to %d + %d = " % numbers))
			break
		except ValueError:
			print 'This is not a valid integer! Try again.'
	if	n_in == sum(numbers):
		print "You are right!"
		return 1
	else:
		print "You're wrong :( The correct answer was: " + repr(sum(numbers))
		return 0

questions_asked = 0
correct = 0
wrong = 0
for i in xrange(10):
	print'Question number: ' + str(i+1)
	correct += AskRand()
	questions_asked +=1
	wrong = questions_asked - correct

print 'You got ' + repr(correct) + ' sums right, and ' + repr(wrong) + ' sums wrong.'



