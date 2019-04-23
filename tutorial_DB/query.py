"""
Author: Andrea Murphy and Mohamed Ali Metwally
Date: April 23, 2019
DESC: Batch Writer
"""

import boto3
from boto3.dynamodb.conditions import Key, Attr

# Get the service resource.
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = dynamodb.Table('users')


response = table.query(
                       KeyConditionExpression=Key('username').eq('johndoe')
                       )
items = response['Items']
print(items)

# Scan the table based on attributes of the items
#response = table.scan(
#                     FilterExpression=Attr('age').lt(27)
#                    )
#items = response['Items']
#print(items)

response = table.scan(
                      FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
                      )
items = response['Items']
print(items)
