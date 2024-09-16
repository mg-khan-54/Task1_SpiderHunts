"""user input function gets the data from user
and returns a dictionary of student data."""
class Student:
    """this is a student class."""
    def user_input(self):
        """user input function gets the data from user
and returns a dictionary of student data."""
        student_dict = {}
        student_name = input('Enter student name: ')
        roll_number = input('Enter roll number: ')
        marks = input('Enter marks: ')
        student_dict['name'] = student_name
        student_dict['roll Number'] = roll_number
        student_dict['marks'] = marks
        return student_dict


    def print_data(self, dictionary_student):
        """This function takes Student dictionary as argument
and prints the data with formating"""
        print(dictionary_student["name"],"\t", dictionary_student["roll Number"],
              "\t",dictionary_student["marks"])

def main():
    '''this is main function'''
    student_1, student_2, student_3 = Student(), Student(), Student()
    student_4, student_5 = Student(), Student()
    object_list = [student_1, student_2, student_3, student_4, student_5]
    return_list = []
    for instance in object_list:
        return_list.append(instance.user_input())
    print(Student.user_input.__doc__)
    index = 0
    for instance in object_list:
        instance.print_data(return_list[index])
        index += 1
    print(Student.print_data.__doc__)



if __name__ == "__main__":
    main()
