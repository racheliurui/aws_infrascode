import json
import kafka_producer

def lambda_kafka_producer(event, context):
    #print(event)
    kafka_producer.producer()
    print('DEBUG: Lambda Function Successfully Executed')
