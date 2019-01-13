import boto3
import json

def getKeyword():
    scanList =[]
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('sg_keyword')

    pe = "#key"
    # Expression Attribute Names for Projection Expression only. 
    ean = { "#key": "keyword"}

    response = table.scan(  
        ProjectionExpression=pe,
        ExpressionAttributeNames=ean
        )

    for i in response['Items']:
        scanList.append(i)

    while 'LastEvaluatedKey' in response:
        response = table.scan(
            ProjectionExpression=pe,        
            ExpressionAttributeNames= ean,
            ExclusiveStartKey=response['LastEvaluatedKey']
            )

        for i in response['Items']:
            scanList.append(i)
    return scanList

