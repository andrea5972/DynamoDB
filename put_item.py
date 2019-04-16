"""
Author: Andrea Murphy and Mohamed Ali Metwally
Date: April 16, 2019
DESC: Puts items into tables in the "dynamodb" Database
"""

import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = dynamodb.Table('users')

table.put_item(
               Item={
               'username': 'janedoe',
               'first_name': 'Jane',
               'last_name': 'Doe',
               'age': 25,
               'account_type': 'standard_user',
               }
            )
