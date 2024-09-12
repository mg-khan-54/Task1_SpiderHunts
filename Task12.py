'''Create a dictionary of students and their marks.
 Write a function that removes all students whose marks
  are below the average marks of the class.'''

std = {'Ghani': 85, 'Khizer': 175, 'Sufyan': 189}
print(std)
average = 0.0
li = []
total = 0
for x,y in std.items():
    total += y
    average = total/len(std)
print(f"average of the class is {average}")

for x,y in std.items():
    if y < average:
        li.append(x)
for x in range(0,len(li)):
    del std[li[x]]
print(std)
