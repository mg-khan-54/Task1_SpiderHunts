'''Create a dictionary of students with their marks.
 Write a function that calculates and returns the
  difference between the highest and lowest marks in the class.'''

std = {'Ghani': 85, 'Khizer': 32, 'Sufyan': 189}
print(std)
def calculate(std):
    highest = 0
    lowest = 0
    for x,y in std.items():
        if y > highest:
            highest = y
            lowest = highest
    print(highest," is the highest mark")
    for x,y in std.items():
        if y < lowest:
            lowest = y
    print(lowest," is the lowest mark")
    difference = highest - lowest
    return difference


print(f"Difference is {calculate(std)}")