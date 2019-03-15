#parsexml.py

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import re


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = data.decode()

#print(tree)
counts = re.findall('<count>([0-9]+)</count>',tree)

sum = 0
for count in counts:
	sum = sum + int(count)
    
print("Length: " + str(len(counts)))
print("Sum: " + str(sum))