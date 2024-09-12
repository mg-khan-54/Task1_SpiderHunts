'''Create a dictionary where student names are keys
and marks are values. Write a function that returns
the names of the top 3 students based on their marks.'''

std = {'Ghani': 85, 'Khizer': 175, 'Sufyan': 189 , 'Shahbaz': 78 , 'Danial': 115, 'giku': 145}
temp = std
highest = 0
highest_mark = {}

for x in range(len(std)):
    if len(highest_mark) == 3:
        continue
    for x,y in temp.items():
        if y > highest:
            name = x
            highest = y
    highest_mark[name] = highest
    highest = 0

    del temp[x]
print(highest_mark)

