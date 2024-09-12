'''Create a dictionary of students and their marks.
 Write a function that takes a student’s name and
  updates their marks if they exist in the dictionary;
  otherwise, it adds the student with the new marks.'''

Students = {'ghani': 56, 'khizer': 78, 'sufyan': 34, 'shahbaz': 98}
name = input('Enter student name: ')
print(Students)

for x,y in Students.items():
    if x == name:
        print(f"15 Marks Awarded to {x}")
        Students[x] = y+15
print(Students)