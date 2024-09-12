'''Create a list of dictionaries where each dictionary
represents a student’s information. Write a function
that searches for a student by name and returns their
information if found.'''
std = [{'Name':'Ghani','RollNumber':"1",'marks':270},{'Name':'Khizer','RollNumber':"2",'marks':320},{'Name':'Sufyan','RollNumber':"3",'marks':180}]
print(std)
found = True
name = input("Enter the name to find: ")
for i in std:
    for x,y in i.items():
        if x == 'Name' and y == name.capitalize():
            print("ID\t",i['RollNumber'],'\n',"Name\t",i['Name'],'\n',"Marks\t",i['marks'])
            found = True
            exit()
        else:
            found = False
if not found:
    print("Student Not Found")