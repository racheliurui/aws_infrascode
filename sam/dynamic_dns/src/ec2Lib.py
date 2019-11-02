import json
import boto3
import route53Lib


# get list of instances filtered by tag
def filterInstanceByTag(ec2client, tag):
    return ec2client.describe_instances(
       Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name': 'tag:Name', 'Values': [tag]}])

# get all running instances
def filterInstancesByStatus(ec2client,status):
    return ec2client.describe_instances(
       Filters=[{'Name': 'instance-state-name', 'Values': [status]}])

def filterInstanceById(ec2client,instanceID):
    return ec2client.describe_instances(
       Filters=[{'Name': 'instance-id', 'Values': [instanceID]}])

# reservation=ec2client.describe_instances()['Reservations'][0]
def getIpAddressFromReservation(reservation):
      instance=reservation['Instances'][0]
      if 'PublicIpAddress' in instance and len(instance['PublicIpAddress'])>0:
         return instance['PublicIpAddress']
      else:
         return instance['PrivateIpAddress']
      return None

def getTagValueFromReservation(reservation,tagName):
      tags=reservation['Instances'][0]['Tags']
      return [x for x in tags if x['Key']==tagName][0]['Value']


# If the instance has public ip address, then return ; otherwise, return private IP address of the instance
def getIPAddressByTag(ec2client, tag):
    instances=ec2client.describe_instances(
       Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name': 'tag:Name', 'Values': [tag]}])
    return getIpAddressFromDescribedReservation(instances['Reservations'][0])

# update all running instances; using tagvalue where tagName=tagName as the DNS name
def updateDNSRecordForReservationsUsingSpecificTagValue(reservations,tagName):
    for reservation in reservations['Reservations']:
      instance=reservation['Instances'][0]
      ipAddress=getIpAddressFromReservation(reservation)
      dnsName=getTagValueFromReservation(reservation,tagName)
      route53Lib.upsert_typeA_DNSRecord(dnsName,ipAddress)


# update all running instances; using tagvalue where tagName=tagName as the DNS name
def updateAllRunningInstanceDNS(ec2client,tagName):
    reservations=filterInstancesByStatus(ec2client,'running')['Reservations']
    updateDNSRecordForReservationsUsingSpecificTagValue(reservations,tagName)

def updateAllRunningInstanceDNSForRegions(regionList,tagName):
    for region in regionList:
        ec2client=boto3.client('ec2', region_name=region)
        updateAllRunningInstanceDNS(ec2client,tagName)


def updateDNSByInstanceId(ec2client,instanceID,tagName):
    reservations=filterInstanceById(ec2client,instanceID)
    updateDNSRecordForReservationsUsingSpecificTagValue(reservations,tagName)


# trigger by SNS message
def update_RunningEC2_DNS_ByEventSNSAndTag(event, tagName):
    if('Records' in event):
       message=event['Records'][0]['Sns']['Message']
       messageJson=json.loads(message)
       instanceId=messageJson['detail']['instance-id']
       region=messageJson['region']
       ec2client=boto3.client('ec2', region_name=region)
       updateDNSByInstanceId(ec2client,instanceId,tagName)

# Trigger by EC2 Start Event
def update_RunningEC2_DNS_ByEventAndTag(event, tagName):
       instanceId=event['detail']['instance-id']
       region=event['region']
       ec2client=boto3.client('ec2', region_name=region)
       updateDNSByInstanceId(ec2client,instanceId,tagName)
