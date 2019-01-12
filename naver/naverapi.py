import os
import sys
import re
import json
import urllib.request
client_id = "hWxIo5cW8YWSioyROCD2"
client_secret = "PKyLJVkqjN"
encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    resdata = json.loads(response.read())
    print(resdata['display'])
    for item in resdata['items']:
        print('-----------------')
        print(item['title'])
        print(item['link'])
        print(item['postdate'])
        print('-----------------')
    print(resdata['start'])
    print(resdata['total'])

else:
    print("Error Code:" + rescode)