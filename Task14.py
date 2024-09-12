'''Write a program that takes a list of student marks
 and counts how many times each mark appears using a dictionary.
'''
std = {}
marks = []
result = {}
counter = 0
ab = 0
name = input("Enter your name: ")

for x in range(0,10):
    mar = int(input('Enter marks: '))
    marks.append(mar)
std[name]= marks
print(std)
for x,y in std.items():
    for a in y:
        num = a
        for c in range(len(y)):
            if num == y[c]:
                counter += 1
            result[a] = counter
            ab += 1
        counter = 0
print(result)