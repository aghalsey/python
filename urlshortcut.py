#!/usr/bin/python
#
#
import urllib.request, urllib.parse, urllib.error

webpage = urllib.request.urlopen('https://www.york.ac.uk/teaching/cws/wws/webpage1.html')

for line in webpage:
	print(line.decode().strip())
