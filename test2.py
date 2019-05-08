import csv


def storefileintolist(filename):
    f = open(filename)
    csv_f=csv.reader(f)
    attendee_list=[]
    for row in csv_f:
        attendee_list.append(row[2])
    return attendee_list

def writecsvfromlist(listname):
	w = open('output.csv','w')
	csv_w=csv.writer(w)
	for i in range(len(listname)):
		csv_w.writerow([listname[i]])

#https://stackoverflow.com/questions/15129567/csv-writer-writing-each-character-of-word-in-separate-column-cell
	

list1 = storefileintolist('attendees1.csv')
list2 = storefileintolist('attendees2.csv')

testlist=[None]*len(list1)
# Create list of size equal to list1
for i in range(len(list1)):
	testlist[i]=list1[i]+' _ '+list2[i+1]	

print(testlist)
print('writing output file')
writecsvfromlist(testlist)

