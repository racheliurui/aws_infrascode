https://github.com/awslabs/kinesis-kafka-connector


mkdir -p /usr/local/share/kafka/plugins
cd /usr/local/share/kafka/plugins
wget https://github.com/racheliurui/aws_infrascode/blob/master/kafka-firehose/amazon-kinesis-kafka-connector-0.0.9-SNAPSHOT.jar

cd /opt/kafka_2.12-2.3.0
bin/connect-standalone.sh /installer/worker.properties /installer/kinesis-kafka-firehose-connecter.properties
