'''Create a dictionary where student names are keys
 and their marks are values. Write a function that
 finds the student with the highest marks.'''
student = {'ghani':56,'khizer':78,'Sufyan':75}
marks = 0
name = ''
for x,y in student.items():
    if marks < y:
        marks = y
        name = x
print(f"{name} has hishest marks: {marks}")
