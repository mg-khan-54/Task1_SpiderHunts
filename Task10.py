'''Create a list of tuples where each tuple
contains a student's name, subject, and marks.
Convert this list into a nested dictionary where
each student has a dictionary of subjects and marks.'''

stud = [('ghani',),("php","Python","Java"),(56,67,78)]
dict = {}
name = list(stud[0])
sub = list(stud[1])
marks = list(stud[2])
dict['Name']=name[0]

for x in range(0,len(sub)):
    dict[sub[x]]=marks[x]
print(dict)








