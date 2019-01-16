#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_119213.html (Sum ends with 93)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

import re
final = list()
tags = soup('span')
for tag in tags:
    stag = str(tag)
    strings = re.findall('[0-9]+',stag)
    for string in strings:
        final.append(float(string))
print(sum(final))
