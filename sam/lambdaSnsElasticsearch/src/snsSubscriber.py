import os
import io
import random


snsArn=os.environ['snsArn']


def lambdaSnsElasticsearch(event, context):
    message = event['Records'][0]['Sns']['Message']
    print("From SNS: " + message)
