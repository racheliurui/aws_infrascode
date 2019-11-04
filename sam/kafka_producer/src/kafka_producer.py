from kafka import KafkaProducer
import os

bootstrap_servers1=os.environ['KafkaEndpoint']

def producer():
   producer = KafkaProducer(bootstrap_servers=bootstrap_servers1)
   producer.send('sample', b'Hello, World!')
   producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
   producer.flush()
