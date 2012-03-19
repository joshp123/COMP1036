# journal_search.py
# Searches a database of journals and allows searching within them
# Author:     J Palmer
# Created on: 2012-03-18
# Version:    1.0

import os, fileinput

def ParseFile(filename):
	filein = open(filename,"r")
	i = 0
	lines = []
	for line in fileinput.input(files=filename):
		lines.append(line)
	for i in xrange(0,len(lines)):
		# operate on lines here
	return



def FileGetCheck():
	valid = 0
	while valid == 0:
		filename = raw_input("Please specify the file containing your data: ")
		if(os.path.exists(filename)):
			valid = 1
		else:
			print "This doesn't appear to be a valid file. Please try again."
	return filename

def main():
	filename = FileGetCheck()
	ParseFile(filename)


if __name__ == "__main__":
	main()
