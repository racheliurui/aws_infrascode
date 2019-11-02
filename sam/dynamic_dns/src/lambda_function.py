import json
import lambdaLib

def lambda_ec2_dns_handler(event, context):
    #print(event)
    lambdaLib.updateDNSEvent_lambda_handler(event, context)
    print('DEBUG: Lambda Function Successfully Executed')



def lambda_rds_dns_handler(event, context):
    #print(event)
    lambdaLib.updateDNSScheduler_lambda_handler(event, context)
    print('DEBUG: Lambda Function Successfully Executed')
