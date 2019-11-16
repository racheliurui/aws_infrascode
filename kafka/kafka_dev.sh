#########################
#   install JDK
#########################
#https://docs.aws.amazon.com/corretto/latest/corretto-8-ug/amazon-linux-install.html
amazon-linux-extras enable corretto8
yum install -y java-1.8.0-amazon-corretto
yum install -y java-1.8.0-amazon-corretto-devel
#alternatives --config javac
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64/jre

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


# todo make zookpeer and kafka autostart
