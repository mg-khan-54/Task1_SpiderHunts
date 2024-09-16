"""Create a dictionary where student names are keys
 and their marks are values. Write a function that
 finds the student with the highest marks."""

if __name__ == "__main__":
    student_Dictionary = {'ghani': 56, 'khizer': 78, 'Sufyan': 75}
    STUDENT_MARKS = 0
    STUDENT_NAME = ''

    for _name, _marks in student_Dictionary.items():
        if STUDENT_MARKS < _marks:
            STUDENT_MARKS = _marks
            STUDENT_NAME = _name
    print(f"{STUDENT_NAME} has highest marks: {STUDENT_MARKS}")
