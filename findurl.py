#This program reads a user submitted url, parses that website
#and retrieves desired url within that website 


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter Count: ')
position = input('Enter Position: ')
print('Retrieving :', url)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for i in range(int(count)):
    url = tags[int(position)].get('href', None)
    print('Retrieving :', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
