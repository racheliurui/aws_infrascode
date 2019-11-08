accountId='1234567'
profile='profilename'


KafkaEndpoint='kafkaserver:9092'
VPCsubnet1='subnetid'
VPCsecuritygroup='securitygroupid'
region='ap-southeast-2'
# recommend to use the DNS Domain Name to make it unique
s3bucket='dns.sam'
regionBucketName=${s3bucket}.${region}
