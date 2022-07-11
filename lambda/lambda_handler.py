# Here we will define our main action

import json
import boto3

def handler(event, context):
    print("✅ Hello, world AWS!")
    return { 'statuscode': 200, 'body': 'success!'}