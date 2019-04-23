"""
Author: Andrea Murphy and Mohamed Ali Metwally
Date: April 16, 2019
DESC: Gets items from the "dynamoDB" Database
"""

import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = dynamodb.Table('users')

response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)
