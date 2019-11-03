#########################
#   install zookeeper
#
#########################
mkdir -p /installer
cd /installer
wget http://apache.mirror.digitalpacific.com.au/zookeeper/zookeeper-3.5.6/apache-zookeeper-3.5.6-bin.tar.gz
gzip -d apache-zookeeper-3.5.6-bin.tar.gz
tar -xvf apache-zookeeper-3.5.6-bin.tar
mv /installer/apache-zookeeper-3.5.6-bin /opt/apache-zookeeper-3.5.6-bin


cat >/opt/apache-zookeeper-3.5.6-bin/conf/zoo.cfg <<EOL
tickTime=2000
dataDir=/var/zookeeper
clientPort=2181
EOL

cd /opt/apache-zookeeper-3.5.6-bin
bin/zkServer.sh start /opt/apache-zookeeper-3.5.6-bin/conf/zoo.cfg
