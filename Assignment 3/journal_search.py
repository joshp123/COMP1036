# journal_search.py
# Searches a database of journals and allows searching within them
# Author:     J Palmer
# Created on: 2012-03-18
# Version:    1.0.0 [initial barebones non-funtional version]

import os, fileinput, csv

def build_dataset(filename):
    dataset = []
    with open(filename, 'rbU') as fd:
        reader = csv.reader(fd, delimiter="\t")
        for line in reader:
            (author, year, title, journal) = line
            dataset.append({'author': author.split(';'),
                            'year': year,
                            'title': title,
                            'journal': journal})

    # TODO: error handling
    
    return tuple(dataset)



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
	data = build_dataset(filename)
# 

if __name__ == "__main__":
	main()
