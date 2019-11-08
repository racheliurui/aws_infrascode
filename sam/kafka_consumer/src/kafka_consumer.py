from kafka import KafkaConsumer
import os
import io
import avro.schema
from avro.io import DatumReader

bootstrap_servers1=os.environ['KafkaEndpoint']

# Path to user.avsc avro schema
schema_path="user.avsc"
schema = avro.schema.Parse(open(schema_path, "r").read())


def consume():
   # To consume messages
   consumer = KafkaConsumer('sample',
                 group_id='my_group',
                 bootstrap_servers=[bootstrap_servers1])
   for msg in consumer:
     bytes_reader = io.BytesIO(msg.value)
     decoder = avro.io.BinaryDecoder(bytes_reader)
     reader = avro.io.DatumReader(schema)
     user1 = reader.read(decoder)
     print(user1)
