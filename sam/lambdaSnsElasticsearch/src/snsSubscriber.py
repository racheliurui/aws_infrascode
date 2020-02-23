import os
import io
import random
import boto3
import json
import requests
from requests_aws4auth import AWS4Auth

snsArn=os.environ['snsArn']
esregion = os.environ['esregion']
eshost = 'https://'+os.environ['eshost']# the Amazon ES domain, including https://

service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, esregion, service, session_token=credentials.token)

# index must be lower case
index = 'coffee'
type = 'sampleType'
url = eshost + '/' + index + '/' + type + '/'

headers = { "Content-Type": "application/json" }



def lambdaSnsElasticsearch(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])

    print("From SNS: " + json.dumps(message))
    id = message['orderId']
    timestamp = message['timestamp']

    # Create the JSON document
    document = { "id": id, "timestamp": timestamp, "message": message }
    # Index the document
    r = requests.put(url + id, auth=awsauth, json=document, headers=headers)
    print("ELK Response SNS: " + r.text)

    return  r.text
