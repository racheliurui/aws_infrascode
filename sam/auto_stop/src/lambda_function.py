import json
import boto3

def lambda_auto_stop(event, context):
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]).stop()
    print('DEBUG: Lambda Function Successfully Executed to stop all running instances')
