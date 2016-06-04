import urllib.request
#import urllib or urllib2 for python 2(Don't need .request or .parse)
import urllib.parse

#Gets the entire source code of the specified sites
x = urllib.request.urlopen('https://www.google.com')

###############################
#Getting and Posting requests on a website

url='http://forums.teamtwice.com/'
#Our search request
values = {'type': 'all',
          'q': 'tzuyu'}
#Encodes the values as a url
data = urllib.parse.urlencode(values)
#Type of encoding
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
#In python2, this is a string value, but not in python 3
respData = resp.read()
print(str(respData))

#This raises the exception of HTTP Error 403: Forbidden
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e))
    
#The solution is
try:
    url = 'https://www.google.com/search?q=test'
    #Everytime you access a website, you sent a header which is data about you
    #By changing this, we can get access to websites
    headers = {}
    #This is the type of browser you are using, defaulted to your Python version
    #Change to a different user-agent
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    #Changing the default header for request
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))
