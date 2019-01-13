import boto3
import json
from insertKeywordLink import putKeywordLink
from naverSearchApi import getResultApi
from scanKeyword import getKeyword

scanResult = getKeyword()

for scandata in scanResult:
        keyword = scandata['keyword']
        apiResult = getResultApi(keyword)    
        for apidata in apiResult.get('items'):
                putKeywordLink(keyword, apidata)
