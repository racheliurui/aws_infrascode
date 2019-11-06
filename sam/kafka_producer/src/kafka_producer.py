from kafka import KafkaProducer
import os
import avro.schema
from avro.io import DatumWriter

bootstrap_servers1=os.environ['KafkaEndpoint']

# Path to user.avsc avro schema
schema_path="user.avsc"
schema = avro.schema.parse(open(schema_path).read())

def producer():
   producer = KafkaProducer(bootstrap_servers=bootstrap_servers1)
   #producer.send('sample', b'Hello, World!')
   #producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
   producer.send('sample', generateAvro())
   producer.flush()


def generateAvro():
    writer = avro.io.DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write({"name": "123", "favorite_color": "111", "favorite_number": random.randint(0,10)}, encoder)
    raw_bytes = bytes_writer.getvalue()
    return raw_bytes
