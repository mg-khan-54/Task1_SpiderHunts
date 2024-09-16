"""Create a dictionary of students with their marks.
 Write a function that calculates and returns the
  difference between the highest and lowest marks in the class."""

def calculate(student_dictionary):
    """This function takes a dictionary as argument, calculates and returns the
difference between the highest and lowest marks in the class"""
    highest_score = 0
    lowest_score = 0
    for student_name, marks in student_dictionary.items():
        if marks > highest_score:
            highest_score = marks
            lowest_score = highest_score
    print(highest_score, " is the highest mark")
    for name, marks in student_dictionary.items():
        if marks < lowest_score:
            lowest_score = marks
    print(lowest_score, " is the lowest mark")
    difference = highest_score - lowest_score
    return difference


def main():
    """This is main function"""
    student_marks = {'Ghani': 85, 'Khizer': 32, 'Sufyan': 189}
    print(student_marks)
    print(f"Difference is {calculate(student_marks)}")


if __name__ == "__main__":
    main()
