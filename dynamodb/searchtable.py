import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Movies')

print("Movies from 2000")

response = table.query(
    # ProjectionExpression="#yr, title",
    # ExpressionAttributeNames={ "#yr": "year" },
    KeyConditionExpression=Key('year').eq(2000)
)

for i in response['Items']:
    print(i['year'], ":", i['title'])