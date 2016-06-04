#Parsing websites using URLlib and Regular Expressions

import urllib.request
import urllib.parse
import re

url='http://forums.teamtwice.com/'

values = {'type': 'all',
          'q': 'tzuyu'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(str(respData))

#using a regular expression to parse whatever is between paragraph tags
#.*? basically means anything
paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

#Printing all results
for eachP in paragraphs:
    print(eachP)
