"""Create a dictionary of students and their marks.
 Write a function that removes all students whose marks
  are below the average marks of the class."""


if __name__ == "__main__":
    student_mark_sheet = {'Ghani': 85, 'Khizer': 175, 'Sufyan': 189}
    print(student_mark_sheet)
    CLASS_AVERAGE = 0.0
    updated_list = []
    TOTAL_MARKS = 0
    STUDENT_MARK_SHEET_LENGTH = len(student_mark_sheet)

    for name, marks in student_mark_sheet.items():
        TOTAL_MARKS += marks
        CLASS_AVERAGE = TOTAL_MARKS/STUDENT_MARK_SHEET_LENGTH
    print(f"average of the class is {CLASS_AVERAGE}")

    for name, marks in student_mark_sheet.items():
        if marks < CLASS_AVERAGE:
            updated_list.append(name)
    UPDATED_DICT_LENGTH = len(updated_list)
    for index in range(0, UPDATED_DICT_LENGTH):
        del student_mark_sheet[updated_list[index]]
    print(student_mark_sheet)
