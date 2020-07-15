#This programs prompts for a URL, reads the JSON data from that URL and
#parses and extracts the comment counts from the JSON data,
#compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
file = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(file), 'characters')

sum = 0
data = json.loads(file)
print('Count: ', len(data['comments']))

for item in data['comments'] :
    sum = sum + int(item['count'])
print('Sum: ', sum)
