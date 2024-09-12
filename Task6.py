'''Create a dictionary with student names as keys
and their marks as values. Write a function to calculate
 and return the average marks of all students.'''


def students(std):
    total = 0
    for x,y in std.items():
        total += y
    print(total/len(std))

def main():
    std = {"ghani": 56, "sufyan": 45, "khizer": 78, "shahbaz": 34}
    students(std)
main()
