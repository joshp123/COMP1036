# journal_search.py
# Searches a database of journals and allows searching within them
# Author:     J Palmer
# Created on: 2012-03-18
# Version:    1.0.0 [initial barebones non-funtional version]

import os, fileinput, csv, string

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
    # print dataset
    # TODO: error handling
    
    return tuple(dataset)


def search_prompt():
	searchstr = raw_input("Search on author (A = ***) or journal/conference (J = ***), where *** is any string [Q = quit]: ")
	args = string.split(searchstr)

	if args [0] == "A":
		# search authors
		field = "author"

	elif args [0] == "J":
		field = "journal"
		# search journals
	elif args [0] == "Q":
		print "Program Exiting"
		return
	else:
		print "Please enter a valid command!"
	# field sorted, now extract query

	query = searchstr[4:len(searchstr)]

	return field, query

def find_in_dataset(dataset, search, fields=['author', 'title']):
    retval = []
    for record in dataset:
        if search in record['title'] or \
            _subsearch(search, record['author']):
       			retval.append(record)
    return tuple(retval)
 
 
def _subsearch(needle, haystack):
    for field in haystack:
        if needle in field:
            return True
    return False


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
	field, query = search_prompt()
	results = find_in_dataset(data, query, field)
	print results



if __name__ == "__main__":
	main()
