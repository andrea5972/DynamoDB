"""
Author: Andrea Murphy and Mohamed Ali Metwally
Date: April 16, 2019
DESC: Updates items within the tables of the Database
"""

import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = dynamodb.Table('users')


table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)
