import json
import boto3
import os

route53client = boto3.client('route53')
HostedZoneIdVar=os.environ['HostedZoneIdVar']


def upsert_typeA_DNSRecord(source, target):
	print ('upsert record with ' + source + ' = ' +  target)
	try:
		response = route53client.change_resource_record_sets(
        HostedZoneId=HostedZoneIdVar,
		ChangeBatch= {
						'Comment': 'add %s -> %s' % (source, target),
						'Changes': [
							{
							 'Action': 'UPSERT',
							 'ResourceRecordSet': {
								 'Name': source,
								 'Type': 'A',
								 'TTL': 300,
								 'ResourceRecords': [{'Value': target}]
							}
						}]
		})
	except Exception as e:
		print(e)


def upsert_cname_record(sourceRecord, targetCName):
	print ('upsert record with ' + sourceRecord + ' = ' +  targetCName)
	try:
		response = route53client.change_resource_record_sets(
		HostedZoneId=HostedZoneIdVar,
		ChangeBatch= {
						'Comment': 'add %s -> %s' % (sourceRecord, targetCName),
						'Changes': [
							{
							 'Action': 'UPSERT',
							 'ResourceRecordSet': {
								 'Name': sourceRecord,
								 'Type': 'CNAME',
								 'TTL': 300,
								 'ResourceRecords': [{'Value': targetCName}]
							}
						}]
		})
	except Exception as e:
		print(e)
