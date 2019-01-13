import boto3
dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='sg_keyword',
    # key  
    #   1.Partition key  하나의 속성으로 구성되는 단순 기본 키
    #   2.Partition key Sort key  첫 번째 속성은 파티션 키이고, 두 번째 속성은 정렬 키

    KeySchema=[
        {
            'AttributeName': 'keyword',
            'KeyType': 'HASH'  #Partition key 
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'keyword',
            'AttributeType': 'S'
        }

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)