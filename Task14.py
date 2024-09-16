"""Write a program that takes a list of student marks
 and counts how many times each mark appears using a dictionary.
"""


if __name__ == "__main__":
    student_data = {}
    marks_list = []
    final_result = {}
    COUNTER_NUMBER = 0
    INDEX_NUMBER = 0
    input_name = input("Enter your name: ")

    for x in range(0, 10):
        input_marks = int(input('Enter marks: '))
        # creates marks list form user input
        marks_list.append(input_marks)
        # creates dictionary with name as key and marks list as value
    student_data[input_name] = marks_list
    print(student_data)

    for name, mark_list in student_data.items():

        for mark in mark_list:
            value = mark
            mark_list_length= len(mark_list)
            for index_ in range(mark_list_length):
                if value == mark_list[index_]:
                    COUNTER_NUMBER += 1
                final_result[mark] = COUNTER_NUMBER
                INDEX_NUMBER += 1
            COUNTER_NUMBER = 0
    print(final_result)
