# Random sum thing but catches non-ints and repeats 10 times (incase you really hate calculators or something idk)
# does the sum of 2 random numbers
# Josh Palmer 26/2/2k12 etc

import random
global c,w
c = 0
w = 0

def AskRand():
	global c,w
	numbers = tuple([random.randint(1,100) for x in xrange(2)])
	while True:
		try:
			n_in = int(raw_input("Solution to %d + %d = " % numbers))
			break
		except ValueError:
			print 'This is not a valid integer! Try again.'
	if	n_in == sum(numbers):
		print "You are right!"
		c +=1
	else:
		print "You're wrong :( The correct answer was: " + repr(sum(numbers))
		w +=1

for i in xrange(10):
	print'Question number: ' + str(i+1)
	AskRand()

print 'You got ' + repr(c) + ' sums right, and ' + repr(w) + ' sums wrong.'



