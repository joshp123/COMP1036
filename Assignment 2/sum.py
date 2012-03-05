# Random sum thingy
# does the sum of 2 random numbers
# Josh Palmer 26/2/2k12 etc

import random
numbers = tuple([random.randint(1,100) for x in xrange(2)])
print "You are right!" if int(raw_input("Solution to %d + %d = " % numbers)) == sum(numbers) else "you're wrong :( the correct answer was" + sum(numbers)