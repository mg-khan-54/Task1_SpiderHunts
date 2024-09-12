'''Write a program to store information about 5 students
 (name, roll number, and marks) using a list of dictionaries.
  Each dictionary should represent one student.'''

class Student():
    def entry(self):
        dict = {}
        name = input(f'Enter student name: ')
        roll_number = input(f'Enter roll number: ')
        marks = input('Enter marks: ')
        dict['name']=name
        dict['roll Number']=roll_number
        dict['marks']= marks
        return dict
    def print_data(self,dict):
        print(dict["name"],dict["roll Number"],dict["marks"])

def main():
    std = Student()
    std2 = Student()
    std3 = Student()
    std4 = Student()
    std5 = Student()
    std_p = std.entry()
    std2_p=std2.entry()
    std3_p=std3.entry()
    std4_p=std4.entry()
    std5_p= std5.entry()
    std.print_data(std_p)
    std.print_data(std2_p)
    std.print_data(std3_p)
    std.print_data(std4_p)
    std.print_data(std5_p)
main()
