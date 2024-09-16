"""Create a list of dictionaries where each
 dictionary contains a student’s name and
 their marks. Sort the list by marks in descending order."""

if __name__ == "__main__":
    students_list = [{"Ghani": 56}, {"Sufyan": 45}, {"Khizer": 78}, {"Shahbaz": 34}]
    Temporary_List = students_list.copy()
    TEMP_MARK = 0
    TEMP_NAME = ""
    newStudent = []
    for num in range(len(Temporary_List)):
        for list_item in students_list:
            for name, marks in list_item.items():
                # print(a,"and", b)
                if TEMP_MARK < marks:
                    TEMP_MARK = marks
                    index_value = list_item
        newStudent.append(index_value)
        TEMP_MARK = 0
        students_list.remove(index_value)
    students = Temporary_List
    print(newStudent)
