import json
import boto3
import os
import route53Lib


def getAllRDSInstances(rds_client):
    return rds_client.describe_db_instances()

# rds_client.describe_db_instances()[0]['Endpoint']['Address']
def getTagValueForRDS(rds_client,rds_arn, tagName):
    response=rds_client.list_tags_for_resource(ResourceName=rds_arn)
    taglist=response['TagList']
    return [x for x in taglist if x['Key']==tagName][0]['Value']


def updateDNSForRds(tagName):
    session = boto3.session.Session()
    rds_client=boto3.client('rds', region_name=session.region_name)
    dbs = getAllRDSInstances(rds_client)
    for db in dbs['DBInstances']:
      DNSName=getTagValueForRDS(rds_client,db['DBInstanceArn'], tagName)
      route53Lib.upsert_cname_record(DNSName,db['Endpoint']['Address'])
