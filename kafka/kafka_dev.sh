sudo su
#########################
#   install JDK
#########################
#https://docs.aws.amazon.com/corretto/latest/corretto-8-ug/amazon-linux-install.html
amazon-linux-extras enable corretto8
yum install -y java-1.8.0-amazon-corretto
yum install -y java-1.8.0-amazon-corretto-devel
#alternatives --config javac
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64

# this will install kafka on EC2 and running in single instance mode for testing purpose
#https://kafka.apache.org/
#########################
#   install kafka
#########################
mkdir -p /installer
cd /installer
wget http://apache.mirror.amaze.com.au/kafka/2.3.0/kafka_2.12-2.3.0.tgz
tar -xzf kafka_2.12-2.3.0.tgz
mv /installer/kafka_2.12-2.3.0 /opt/kafka_2.12-2.3.0
cd /opt/kafka_2.12-2.3.0
bin/zookeeper-server-start.sh config/zookeeper.properties &
bin/kafka-server-start.sh config/server.properties &


cat >/etc/systemd/system/zookeeper.service <<EOL
[Unit]
Description=zookeeper - dev
After=syslog.target network.target remote-fs.target nss-lookup.target
[Service]
Restart=always
RestartSec=300
Type=simple
PIDFile=/usr/local/zookeeper/logs/kafka.pid
WorkingDirectory=/opt/kafka_2.12-2.3.0/bin
#ExecStartPre=
ExecStart=/opt/zookeeper-server-start.sh /opt/kafka_2.12-2.3.0/config/zookeeper.properties
ExecReload=/opt/zookeeper-server-start.sh /opt/kafka_2.12-2.3.0/config/zookeeper.properties
ExecStop=zookeeper-server-stop.sh
PrivateTmp=true
[Install]
WantedBy=multi-user.target
EOL

systemctl enable zookeeper.service
systemctl start zookeeper.service

cat >/etc/systemd/system/kafka.service <<EOL
[Unit]
Description=kafka - dev
After=syslog.target network.target remote-fs.target nss-lookup.target
[Service]
Restart=always
RestartSec=300
Type=simple
PIDFile=/usr/local/kafka/logs/kafka.pid
WorkingDirectory=/opt/kafka_2.12-2.3.0/bin
#ExecStartPre=
ExecStart=/opt/kafka_2.12-2.3.0/bin/kafka-server-start.sh /opt/kafka_2.12-2.3.0/config/server.properties
ExecReload=/opt/kafka_2.12-2.3.0/bin/kafka-server-start.sh /opt/kafka_2.12-2.3.0/config/server.properties
ExecStop=/opt/kafka_2.12-2.3.0/bin/kafka-server-stop.sh
PrivateTmp=true
[Install]
WantedBy=multi-user.target
EOL

systemctl enable kafka.service
systemctl start kafka.service

#########################
#   Create Topics
#########################
#bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
#bin/kafka-topics.sh --zookeeper localhost:2181 --list
#bin/kafka-console-producer.sh  --broker-list localhost:9092  --topic test
#bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sample --from-beginning

# TODO
# Make Kafka Zookeeper autostart
