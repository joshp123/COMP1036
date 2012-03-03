# itt lets do a leastsquares fit lolz
# 
#
# yosposbitch

import math, csv, os

def GetInput(x):
	input = csv.reader(open(x,'r'), delimeter=',')
	i = 0
	for row in input:
		print row
		setattr(r,i,row)
		i += 1
	for i in xrange(1,3):
		print r.i


def main():
	while True:
		try:
			x = raw_input("Full filename: ")
			if os.path.exists(x):
				GetInput(x)
				break
			else:
				print 'This is not a valid file, try again'
	return

if __name__ == "__main__":
	main()
