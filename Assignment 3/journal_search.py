# journal_search.py
# Searches a database of journals and allows searching within them
# Author:     J Palmer
# Created on: 2012-05-04
# Version:    1.3 [omg it works] // added error checking: ignores header line, and exits on incorrect data; error actually work now


# TODO: check erros mofo

import os, fileinput, csv, string, sys

def build_dataset(filename):
	dataset = []
	with open(filename, 'rbU') as fd:  ## BLANK FILE ALTERZ
		reader = csv.reader(fd, delimiter="\t")
		header_skipped = 0
		for line in reader:
			(author, year, title, journal) = line
			if header_skipped == 0: # don't add fist line of file, header
				header_skipped = 1
				continue

			dataset.append({'author': author.split(';'),
							'year': year,
							'title': title,
							'journal': journal})
			
			if (journal == '') or (year == '') or (author == '') or (title == ''): # if any values blank, error
				print "Incorrectly formatted data found. The erroneous line is: \n" + repr(line) + "\nProgram Exiting."
				sys.exit()

	return tuple(dataset)


def search_prompt():
	valid = 0
	while valid == 0:
		searchstr = raw_input("Search on author (A = ***) or journal/conference (J = ***), where *** is any string [Q = quit]:\n")
		args = string.split(searchstr)
		if args [0] == "A":
			# search authors
			field = "author"
			valid = 1
		elif args [0] == "J":
			field = "journal"
			# search journals
			valid = 1
		elif args [0] == "Q":
			print "Program Exiting"
			sys.exit()
		else:
			print "Please enter a valid command!"

	# field sorted, now extract query

	query = searchstr[4:len(searchstr)]

	return field, query

def find_in_dataset(dataset, search, fields=['author', 'journal']):
	retval = []
	for record in dataset:
		if search in record['journal'] or \
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

def sanitize(result):

	# loop over everything
	fullstring = [] # make a list of all sanitized results ready for output, so that main can loop and print em all
	
	for x in xrange(0,len(result)):
		results = result[x] # map results[x] to another variable so i don't have to type results[x]['author'][0] a billion times

		# count authors

		a_count = len(results['author'])
		if a_count == 1:
			authors = results['author'][0] + "."
		else:
			authors1 = ''
			for x in xrange(0,a_count-1):
				authors1 = authors1 + results['author'][x] + ", "
			authors = authors1 + "& " + results['author'][a_count-1] + "." ##  might need to change this for 2 authors idk

		# stick together the other crap

		fullstring.append(authors + " (" + results['year'] + "). " + results['title'] + ". " + results['journal'] + ".")

	return fullstring



def main():
	filename = file_get_check()
	data = build_dataset(filename)
	while True:
		field, query = search_prompt()
		results = find_in_dataset(data, query, field)
		if len(results) == 0:
			print "\nNo matching papers found\n"
		else:
			output = sanitize(results)
			print '\n'
			for x in xrange(0,len(output)):
				print output[x]
			print "\n"
	return



if __name__ == "__main__":
	main()
