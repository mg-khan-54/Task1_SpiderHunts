'''Class with Highest Average: Create a dictionary
where the keys are class names, and the values are
lists of student marks. Write a function that
determines which class has the highest average marks.'''

class_ = {"CLass python":[34,45,56,67,78],"CLass PHP":[76,56,80,70,43],"CLass Java":[34,45,78,7,98]}
highest_av = 0.0
winner = ""
for x,y in class_.items():
    total = 0
    for a in y:
        total += a
        if total/len(y)> highest_av:
            winner = x
            highest_av = total/len(y)
    print(f"{x} and class average is {highest_av}")
print(f"\n{winner} has the highest average marks! {highest_av}")