"""Class with Highest Average: Create a dictionary
where the keys are class names, and the values are
lists of student marks. Write a function that
determines which class has the highest average marks."""

if __name__ == "__main__":
    class_grades = {"python":[34,45,56,67,78],"PHP\t":[76,56,80,70,43],"Java":[34,45,78,7,98]}
    HIGHEST_AVERAGE = 0.0
    WINNER_CLASS = ""
    for class_name,marks in class_grades.items():
        TOTAL_MARKS = 0
        for each in marks:
            TOTAL_MARKS += each
            if TOTAL_MARKS/len(marks)> HIGHEST_AVERAGE:
                WINNER_CLASS = class_name
                HIGHEST_AVERAGE = TOTAL_MARKS/len(marks)
        print(f"{class_name}\t\tclass average is {HIGHEST_AVERAGE}")
    print(f"\n{WINNER_CLASS}\t\thighest class average marks! {HIGHEST_AVERAGE}")
