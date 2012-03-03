# Eggs.py
# Calculates number of egg boxes and remainder
# Author:     J Palmer
# Created on: 2012-02-17
# Version:    1.1

while True:
	try:
		input_eggs = int(raw_input("How many eggs are in your basket? "))
		if(input_eggs >= 0):
			break
		else:
			print 'This is not a valid positive integer! Please try again!'
	except ValueError:
		print "This was not a valid number! Please try again!"

eggs = int(input_eggs)
boxes = eggs / 6
remainder = eggs % 6


b_noun = 'box' #default = singular
if boxes > 1:
		b_noun= 'boxes' # change box to boxes when number of boxes is plural


r_noun = 'egg' #default = singular
if remainder > 1:
		r_noun = 'eggs' # change egg to eggs when number of remaining eggs is plural


if eggs < 0:
	print 'Congratulations, you have a negative number of eggs! You have successfully subverted the laws of physics and created ANTI-EGGS!' # this line is no longer necessary since it throws an exception when the user enters a negative number at the start, but it's funny so i'm leaving it in anyway :cool:
elif eggs == 0:
	print 'You have no eggs! You do not need a box or anything! You seem to be in the wrong place!'
else:
	if boxes == 0:
		boxes_text = 'cannot fill any boxes'
	else:
		boxes_text = 'can fill %(b)i %(bn)s' % {'b' : boxes , 'bn' : b_noun} # form the "can fill xxx boxe(s)" string for printing in a minute
	if remainder == 0:
		remainder_text = 'no eggs'
	else:
		remainder_text = "%(r)i %(t)s"  % {'r' : remainder , 't' : r_noun} # form the "yyy egg(s)" string for printing in a minute
	print 'You %(boxes_text)s and you will have %(remainder_text)s left over.' % {'boxes_text' : boxes_text , 'remainder_text' : remainder_text,}

