"""
Author: Andrea Murphy and Mohamed Ali Metwally
Date: April 16, 2019
DESC: Delete an items from the "dynamoDB" Database
"""

import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = dynamodb.Table('users')


table.delete_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
