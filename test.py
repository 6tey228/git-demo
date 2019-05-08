import csv

def storefileintolist(filename):
    f = open(filename)
    csv_f=csv.reader(f)
    attendee_list=[]
    for row in csv_f:
        attendee_list.append(row[2])

    return attendee_list

list1 = storefileintolist('attendees1.csv')
list2 = storefileintolist('attendees2.csv')

set1=set(list1)
set2=set(list2)

difference=set2.difference(set1)
print(difference)



    
    


