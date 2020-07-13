import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
xfile = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(xfile), 'characters')

sum = 0
data = ET.fromstring(xfile)
dlist = data.findall('comments/comment')
print('Count: ', len(dlist))
for item in dlist :
    sum = sum + int(item.find('count').text)
print('Sum: ', sum)
