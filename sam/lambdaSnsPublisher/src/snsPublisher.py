import os
import io
import json
import boto3
import coffeeTransaction
import random

snsArn=os.environ['snsArn']
minOrdersPerMin=int(os.environ['minOrdersPerMin'])
maxOrdersPerMin=int(os.environ['maxOrdersPerMin'])

client = boto3.client('sns')


# publish order information in bulk
def lambdaSnsPublisher(event, context):
    numOfOrders=random.randint(10,60)
    for x in range(numOfOrders):
      message = coffeeTransaction.getDummyCoffeeOrder()
      response = client.publish(
        TargetArn=snsArn,
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
      )
      print("Published SNS: " + json.dumps(message))
    print("Published: "+str(numOfOrders) + "  messages !!!")
