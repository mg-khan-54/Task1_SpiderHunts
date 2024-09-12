'''Create a dictionary of students and their marks.
 Write a function that adds a grade (A, B, C, etc.)
 to each student based on their marks and returns an
  updated dictionary.'''
std = {"Ghani":[34,45,56,67,78],"Khizer":[76,56,80,70,43],"Sufyan":[34,45,78,7,98]}

def student(Dict):
    total = 0
    for x,y in Dict.items():
        for a in y:
            total += a
            average = total/len(y)
        if average > 90:
            y.append('A')
        elif 90> average > 80:
            y.append("B")
        elif 80> average > 70:
            y.append("C")
        elif 70> average > 60:
            y.append('D')
        elif 60> average > 50:
            y.append('F')
    return Dict
def Print(updated):
    for x,y in updated.items():
        print(f"name = {x}\ngrade = {y}")

def main():
    std = {"Ghani": [34, 45, 56, 67, 78], "Khizer": [76, 56, 80, 70, 43], "Sufyan": [34, 45, 78, 7, 98]}
    Updated = student(std)
    Print(Updated)
main()
