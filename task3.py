'''Take two lists, one containing names and
 the other containing marks. Convert them
 into a dictionary where names are keys and
  marks are values.'''

if __name__ == "__main__":
    student_names = ['ghani','khizer','sufyan','shahbaz']
    STUDENT_MARKS = [56, 78, 34, 98]
    STUDENT_DATA = {}
    LENGTH = len(student_names)
    for num in range(0,LENGTH):
        STUDENT_MARKS[student_names[num]] = STUDENT_MARKS[num]
    print(STUDENT_MARKS)
