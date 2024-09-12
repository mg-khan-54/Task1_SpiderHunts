'''Take two lists, one containing names and
 the other containing marks. Convert them
 into a dictionary where names are keys and
  marks are values.'''
nemes = ['ghani','khizer','sufyan','shahbaz']
marks = [56,78,34,98]
Data = {}
for x in range(0,len(nemes)):
    Data[nemes[x]] = marks[x]
print(Data)