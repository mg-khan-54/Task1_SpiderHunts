"""Create a list of dictionaries where each dictionary
represents a student’s information. Write a function
that searches for a student by name and returns their
information if found."""

if __name__ == "__main__":
    students_List = [{'Name':'Ghani','RollNumber':"1",'marks':270},
                     {'Name':'Khizer','RollNumber':"2",'marks':320},
                     {'Name':'Sufyan','RollNumber':"3",'marks':180}]
    FOUND_NAME = True
    INPUT_NAME = input("Enter the name to find: ")

    for item in students_List:
        for key,value in item.items():
            if key == 'Name' and value == INPUT_NAME.capitalize():
                print("ID\t\t",item['RollNumber'],'\nName\t',item['Name'],
                      '\nMarks\t',item['marks'])
                FOUND_NAME = True
                exit()
            else:
                FOUND_NAME = False

    if not FOUND_NAME:
        print("Student Not Found")
