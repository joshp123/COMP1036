# journal_search.py
# Searches a database of journals and allows searching within them
# Author:     J Palmer
# Created on: 2012-03-18
# Version:    1.0.0 [initial barebones non-funtional version]

import os, fileinput, csv, string

def build_dataset(filename):
    Journals = []
    Authors = []
    Title = []
    dataset = []
    with open(filename, 'rbU') as fd:
        reader = csv.reader(fd, delimiter="\t")
        for line in reader:
            (author, year, title, journal) = line
            dataset.append({'author': author.split(';'),
                            'year': year,
                            'title': title,
                            'journal': journal})
    # print dataset
    # TODO: error handling
    
    return tuple(dataset)


def file_search(data):
	searchstr = raw_input("Search on author (A = ***) or journal/conference (J = ***), where *** is any string [Q = quit]: ")
	args = string.split(searchstr)

	if args [0] == A:
		# search authors
		field = author

	elif args [0] == J:
		field = journal
		# search journals
	elif args [0] == Q:
		print "Program Exiting"
		return
	else:
		print "Please enter a valid command!"
	
	

	return


def file_get_check():
	valid = 0
	while valid == 0:
		filename = raw_input("Please specify the file containing your data: ")
		if(os.path.exists(filename)):
			valid = 1
		else:
			print "This doesn't appear to be a valid file. Please try again."
	return filename

def main():
	filename = file_get_check()
	data = build_dataset(filename)


if __name__ == "__main__":
	main()
