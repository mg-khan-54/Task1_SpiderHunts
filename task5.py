'''Create a list of dictionaries where each
 dictionary contains a student’s name and
 their marks. Sort the list by marks in descending order.'''

students = [{"ghani":56},{"sufyan":45},{"khizer":78},{"shahbaz":34}]
temp = students.copy()
mark = 0
name = ""
newStudent = []
index = 0
for x in range(len(temp)):
    for x in students:
        for a,b in x.items():
            # print(a,"and", b)
            if mark < b:
                mark = b
                val = x
    newStudent.append(val)
    mark = 0
    students.remove(val)
students = temp
print(newStudent)
print(students)
# print(mark)