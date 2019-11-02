import json
import boto3
import ec2Lib
import rdsLib
import os

TagName=os.environ['TagName']

def updateDNSEvent_lambda_handler(event, context):
    if('detail' in event):
       ec2Lib.update_RunningEC2_DNS_ByEventAndTag(event,TagName)



def updateDNSScheduler_lambda_handler(event, context):
    rdsLib.updateDNSForRds(TagName)
    #rdsLib.updateRDSForRegions(regionList,TagName)
