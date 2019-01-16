import re
file = input('Enter File: ')
fh = open(file)
values = list()
for line in fh:
    line = line.rstrip()
    strings = re.findall('[0-9]+' , line)
    if len(strings) < 1 : continue
    for string in strings:
        values.append(float(string))
print('Sum:', sum(values))
