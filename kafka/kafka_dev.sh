
#JDK
#https://docs.aws.amazon.com/corretto/latest/corretto-8-ug/downloads-list.html
yum install java-1.8.0



mkdir -p /installer
cd /installer
wget http://apache.mirror.amaze.com.au/zookeeper/zookeeper-3.5.6/apache-zookeeper-3.5.6.tar.gz
gzip -d apache-zookeeper-3.5.6.tar.gz
tar -xvf apache-zookeeper-3.5.6.tar
mv /installer/apache-zookeeper-3.5.6 /opt/apache-zookeeper-3.5.6

cp /opt/apache-zookeeper-3.5.6/conf/zoo_sample.cfg /opt/apache-zookeeper-3.5.6/conf/zoo.cfg

cat >/opt/apache-zookeeper-3.5.6/conf/zoo.cfg <<EOL
tickTime=2000
dataDir=/var/zookeeper
clientPort=2181
EOL

cd /opt/apache-zookeeper-3.5.6
bin/zkServer.sh start /opt/apache-zookeeper-3.5.6/conf/zoo.cfg

# this will install kafka on EC2 and running in single instance mode for testing purpose
#https://kafka.apache.org/

mkdir -p /installer
cd /installer
wget http://apache.mirror.amaze.com.au/kafka/2.3.0/kafka_2.12-2.3.0.tgz
tar -xzf kafka_2.12-2.3.0.tgz
mv /installer/kafka_2.12-2.3.0 /opt/kafka_2.12-2.3.0
