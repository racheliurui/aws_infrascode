
# Feature

* every minute will simulate to publish N number of transaction messages to topic 'snsArn'
* number of transactions per min will be random number N, minOrdersPerMin<=N<=maxOrdersPerMin
* Each transaction will have random values for,
   * cup of coffees , products, second within the min, channels


# Step 1: Download Script


```shell
cd ~/github
git clone git@github.com:racheliurui/aws_infrascode.git
```



# Step 2: Set up Variable on mac/linux

```shell
cd ~/github/aws_infrascode/sam/lambdaSnsPublisher
cp sample.sh vault.sh
```

* Edit the variables in vault.sh

## Setup Topic publish permission

By default, the SNS topic should have permission to allow lambda in same account to publish message to it.
https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html

## Deploy lambda to certain region

```shell
cd ~/github/aws_infrascode/sam/lambdaSnsPublisher

. ./vault.sh
sam build --template ${app}.yml --profile $profile --region $region

sam package --s3-bucket $regionBucketName --output-template-file packaged.yml  --profile $profile --region $region
sam deploy --template-file packaged.yml --stack-name sam-${app} --parameter-overrides \
snsArn=$snsArn \
minOrdersPerMin="10" \
maxOrdersPerMin="60" \
--capabilities CAPABILITY_NAMED_IAM --profile $profile --region $region
```
