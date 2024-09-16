"""Create a dictionary of students and their marks.
Write a function that adds a grade (A, B, C, etc.)
to each student based on their marks and returns an
updated dictionary."""

def student(student_dict):
    """This function take students marks dictionary as argument
and returns updated dictionary with each student marks
average and grades according to their average score"""
    average_marks = 0.0
    total_marks = 0
    for item_name, marks_list in student_dict.items():
        for each_mark in marks_list:
            total_marks += each_mark
            average_marks = total_marks / len(marks_list)

        if average_marks > 90:
            marks_list.append(f'average is {average_marks}')
            marks_list.append('Grade is A')

        elif 90 > average_marks > 80:
            marks_list.append(f'average is {average_marks}')
            marks_list.append("Grade is B")

        elif 80 > average_marks > 70:
            marks_list.append(f'average is {average_marks}')
            marks_list.append("Grade is C")

        elif 70 > average_marks > 60:
            marks_list.append(f'average is {average_marks}')
            marks_list.append('Grade is D')

        elif 60 > average_marks > 50:
            marks_list.append(f'average is {average_marks}')
            marks_list.append('Grade is F')
    return student_dict


def print_result(updated_dictionary):
    """This function takes dictionary as argument and prints data."""
    for item_name, item_result in updated_dictionary.items():
        print(f"name = {item_name}\t\tgrade = {item_result}")

if __name__ == "__main__":

    student_dictionary = {"Ghani": [34, 45, 56, 67, 78],
                          "Khizer": [76, 56, 80, 70, 43],
                          "Sufyan": [34, 45, 78, 7, 98]}
    def main():
        """This is main function"""
        updated = student(student_dictionary)
        print_result(updated)
    main()
