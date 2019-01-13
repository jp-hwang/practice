import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('sg_keyword')

keyword = "어벤져스"

response = table.put_item(
   Item={
        'keyword': keyword
    }
)

print("PutItem succeeded:")