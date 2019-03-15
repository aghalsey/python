import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
total = int(input('Enter count: '))
position = int(input('Enter position: '))
count = 0

while (count < total):
    # Retrieve all of the a tags, re-assign all variables for each iteration
    tags = soup('a')
    url = tags[position-1].get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(url)
    count = count + 1

#print(url)


#for tag in tags:

    # Look at the parts of a tag
    #print('TAG:', tag)
    #print(tag.get('href', None))
    #print('Contents:' + tag.contents[0])
    #print('Attrs:', tag.attrs)