'''You have 3 dictionaries, each representing different
subjects and their corresponding marks for students.
Write a program to merge these dictionaries into one
where each student has their total marks from all subjects.'''

std1 = [{"Name":"Ghani"},{"python":34},{"PHP":23},{"Java":28}]
std2 = [{"Name":"Khizer"},{"python":76},{"PHP":34},{"Java":65}]
std3 = [{"Name":"Sufyan"},{"python":78},{"PHP":38},{"Java":73}]
name = ''
dict = {}
def student(std):
    total = 0
    for x in std:
        for a,b in x.items():
            if a == "Name":
                name = b
            else:
                total += b
        dict[name] = total

student(std1)
student(std2)
student(std3)
print(dict)





# merged = {**dict1, **dict2, **dict3}
# print(merged)
