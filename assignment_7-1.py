# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Error: the file",fname,"does not exist")
    exit()
for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)
