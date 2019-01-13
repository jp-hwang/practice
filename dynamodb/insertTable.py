import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Movies')

title = "Avengers"
year = 2018

response = table.put_item(
   Item={
        'year': year,
        'title': title,
        'info': {
            'plot':"What's up man1",
            'rating': decimal.Decimal(0)
        }
    }
)

print("PutItem succeeded:")