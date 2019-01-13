import boto3

def putKeywordLink(keyword, data):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('sg_keywordlink')   
    
    table.put_item(
        Item={
            'keyword': keyword,
            'link': data['link'],
            'title' : data['title'],        
        'postdate' : data['postdate']
        }
    )

