#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name
#that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
#Last name in sequence: Anayah
#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Chintu.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: A

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

position = int(input('Enter position: '))
count = int(input('Enter count: '))
print(url)

n = 0
import re
tags = soup('a')
while count > 0 :
    for tag in tags:
        n = n + 1
        if not n == position: continue
        else:
            strtag = str(tag)
            strings = re.findall('"(.+?)"',strtag)
            print(strings[0])
            html = urlopen(strings[0], context=ctx).read()
            soup = BeautifulSoup(html, "html.parser")
            tags = soup('a')
            n = 0
            count = count - 1
            break
print('Done')
