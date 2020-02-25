import os
import io
import random
import boto3
import json




def lambdaSnsDataCheck(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])

    print("From SNS: " + json.dumps(message))


    return  'ok'
