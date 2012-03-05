# game.py
# Guessing a random number game thing whatup
# Author:     J Palmer
# Created on: 2012-03-05
# Version:    1.2 FIXED A VERY IMPORTANT ERROR IN THE NUMBER OF GUESSES THING!!!!!! also grammar and adding out of range check

import random

def Guess():
	done = 0
	guesses = []
	g_count = 0
	print "I'm thinking of a number between 1 and 100."
	while done == 0:
		if g_count == 0:
			str_guess = " guess."
		else:
			str_guess = " guesses."
		
		while True:
			try:
				x = int(raw_input("Guess the number I'm thinking of: "))
				break
			except ValueError:
				print 'This is not a valid integer! Try again.'

		if x in guesses:
			print "You've already guessed this number, try one that you haven't guessed"

		elif ((x < 0) or (x > 100)):
			print 'Your guess was not between 1 and 100! Try again.'
		
		elif x == n:
			g_count+=1
			print "Congratulations! You got the number I was thinking of. (It was " + repr(x) + ".) It took you " + repr(g_count) + str_guess
			done = 1
		
		else:
			guesses.append(x)
			g_count += 1
			print "You're on " + repr(g_count) + str_guess
			if x < n:
				print "Try higher next time."
			else:
				print "Try lower next time."


def main():
	global n
	n = 0
	while n in [0,25,50,100]:
		n = random.randint(1,100)
	print n
	Guess()


if __name__ == "__main__":
	main()

