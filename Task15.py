"""Create a dictionary where student names are keys
and marks are values. Write a function that returns
the names of the top 3 students based on their marks."""
if __name__ == "__main__":

    student_marks_sheet = {'Ghani': 85, 'Khizer': 175, 'Sufyan': 189,
                           'Shahbaz': 78, 'Danial': 115, 'giku': 145}
    temp_mark_sheet = student_marks_sheet
    HIGHEST_TEMP = 0
    highest_mark = {}
    NAME_TEMP = ''
    STUDENTS_MARK_SHEET_LENGTH =len(student_marks_sheet)
    for index in range(STUDENTS_MARK_SHEET_LENGTH):
        if len(highest_mark) == 3:
            continue
        for item_name, item_marks in temp_mark_sheet.items():
            if item_marks > HIGHEST_TEMP:
                NAME_TEMP = item_name
                HIGHEST_TEMP = item_marks
        highest_mark[NAME_TEMP] = HIGHEST_TEMP
        HIGHEST_TEMP = 0
        del temp_mark_sheet[NAME_TEMP]

    print(highest_mark)
