import json
import kafka_consumer

def lambda_kafka_consumer(event, context):
    #print(event)
    kafka_consumer.consume()
    print('DEBUG: Lambda Function Successfully Executed')
