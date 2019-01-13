import json
import urllib.request

client_id = "hWxIo5cW8YWSioyROCD2"
client_secret = "PKyLJVkqjN"

def getResultApi(key):
    encText = urllib.parse.quote(key)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        return json.loads(response.read())
    else:
        print("Error Code:" + rescode)