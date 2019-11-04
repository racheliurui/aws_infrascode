
# Feature

make sure you have kafka server sits in same VPC with the lambda

- publish message to kafka every 1 min


# Step 1: Download Script


```shell
cd ~/github
git clone git@github.com:racheliurui/aws_infrascode.git
```



# Step 2: Set up Variable on mac/linux

```shell
cd ~/github/aws_infrascode/sam/kafka_producer
cp sample.sh vault.sh
```

* Edit the variables in vault.sh.


## Deploy kafka_producer to certain region

```shell
cd ~/github/aws_infrascode/sam/kafka_producer


sam build --template kafka_producer.yml --profile $profile --region $region
sam package --s3-bucket $regionBucketName --output-template packaged.yml  --profile $profile --region $region
sam deploy --template-file packaged.yml --stack-name sam-kafkaproduer --parameter-overrides KafkaEndpoint=$KafkaEndpoint VPCsubnet1=$VPCsubnet1 VPCsecuritygroup=$VPCsecuritygroup --capabilities CAPABILITY_NAMED_IAM --profile $profile --region $region
```
