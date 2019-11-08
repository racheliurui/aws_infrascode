
# Feature

make sure you have kafka server sits in same VPC with the lambda

- consume kafka message and write to log


# Step 1: Download Script


```shell
cd ~/github
git clone git@github.com:racheliurui/aws_infrascode.git
```



# Step 2: Set up Variable on mac/linux

```shell
cd ~/github/aws_infrascode/sam/kafka_consumer
cp sample.sh vault.sh
```

* Edit the variables in vault.sh.


## Deploy kafka_producer to certain region

```shell
cd ~/github/aws_infrascode/sam/kafka_consumer


sam build --template kafka_consumer.yml --profile $profile --region $region
sam package --s3-bucket $regionBucketName --output-template packaged.yml  --profile $profile --region $region
sam deploy --template-file packaged.yml --stack-name sam-kafkaconsumer --parameter-overrides KafkaEndpoint=$KafkaEndpoint VPCsubnet1=$VPCsubnet1 VPCsecuritygroup=$VPCsecuritygroup --capabilities CAPABILITY_NAMED_IAM --profile $profile --region $region
```
