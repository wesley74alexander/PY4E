name = input("Enter file:")
handle = open(name)
dct = dict()
addresses = list()
for line in handle:
    line = line.rstrip()
    if not line.startswith("From ") : continue
    words = line.split()
    addresses.append(words[1])
for address in addresses:
    dct[address] = dct.get(address, 0) + 1
maxcount = None
maxaddress = None
for address,count in dct.items():
    if  maxcount is None or maxcount < count:
        maxcount = count
        maxaddress = address
print(maxaddress, maxcount)
