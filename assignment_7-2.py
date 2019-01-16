# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Error: file does not exist")
    exit()
count = 0
spamtot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    spampos = line.find(":")
    spamstr = line[spampos+1:]
    spamfloat = float(spamstr)
    spamtot = spamtot + spamfloat
print("Average spam confidence:", spamtot)
