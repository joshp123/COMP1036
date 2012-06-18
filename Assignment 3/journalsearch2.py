import csv, string

def main():
    while True:
        fin = raw_input("Where is your data located: ")
        data = open(fin, "rbU")
        if data == 0:
            print "This file does not exist! Please enter a correct one."
        else:
            break
    # file acquired, begin reading in

    authors = []
    journals = []
    papers = []
    reader = csv.reader(data, delimiter="\t")
    index = 0
    for line in reader:
        # first line has titles so ignore
        (author, year, title, journal) = line
        tempauthors = []
        authors.append([author.split(';'),index])
        journals.append([journal,index])
        tempauthors.append(author.split(';'))
        ptitle = ''
        comma_yn = ''
        for x in xrange(0,len(tempauthors[0])-1):
            if x > 0:
                comma_yn = ', '

            ptitle = ptitle + comma_yn + tempauthors[0][x]
           # print ptitle
        if len(tempauthors[0]) == 1:
            ampersand = ''
        else:
            ampersand = " & "
        ptitle = ptitle + ampersand + tempauthors[0][-1] + ". (" + year + "). " + title + ". " + journal + "." # concentate title, add to array of titles
        #print 'Diagnorstic: inputting ptitle' + ptitle
        del tempauthors
        papers.append(ptitle)
        ptitle = ''

    
    # file read in, ask user to do stuff:
    while True:
        question = raw_input("Search on author (A = ***) or journal/conference (J = ***), where *** is any string [Q = quit]:")
        if question[0] == "A":
            search_type = 1
            print "Searching by author  " + question
            break
        elif question[0] == "J":
            search_type = 2
            print "Searching by Journal " + question
            break
        elif question[0] == "Q":
            print "Quitting."
            return
        else:
            print "I didn't understand your input; please try again!"

    # field sorted, now extract query

    question = question[4:]
    # authorsearch
    if search_type == 1:
        if question in authors == False:
            print "I couldn't find the author you were searching for."
            return
        for x in xrange(0,len(authors)):
            for y in xrange(0,len(authors[x][0])):
                if authors[x][0][y] == question:
                    print "Paper found:\n" + papers[x]
        return
    else:
        if question in journals == False:
            print "I couldn't find the journal you were searching for."
            return

        for x in xrange(0,len(journals)):
            for y in xrange(0,len(journals[x])):
                if journals[x][y] == question:
                    print "Paper found:\n" + papers[x]
        return


if __name__ == "__main__":
    main()
