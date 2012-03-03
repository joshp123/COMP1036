# game.py
# Guessing a random number game thing whatup
# Josh Palmer 26/2/2k12 etc

import random

def Guess():
	done = 0
	guesses = []
	g_count = 0
	while done == 0:
		while True:
			try:
				x = int(raw_input("Guess the number I'm thinking of: "))
				break
			except ValueError:
				print 'This is not a valid integer! Try again.'

		if x in guesses:
			print "You've already guessed this number, try one that you haven't guessed"
		elif x == n:
			print "Congratulations! You got the number I was thinking of. (It was " + repr(x) + ".) It took you " + repr(g_count) + " guesses."
			done = 1
		else:
			guesses.append(x)
			g_count += 1
			print "You're on " + repr(g_count) + " guesses."
			if x < n:
				print "Try higher next time."
			else:
				print "Try lower next time."


def main():
	global n
	n = 0
	while n in [0,25,50,100]:
		n = random.randint(1,100)
	Guess()


if __name__ == "__main__":
	main()

