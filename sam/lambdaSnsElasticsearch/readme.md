
# Feature

* subscribe to SNS topic
* get message payload
* persist to elastisearch


# Step 1: Download Script


```shell
cd ~/github
git clone git@github.com:racheliurui/aws_infrascode.git
```



# Step 2: Set up Variable on mac/linux

```shell
cd ~/github/aws_infrascode/sam/lambdaSnsElasticsearch
cp sample.sh vault.sh
```

* Edit the variables in vault.sh

## Setup Topic subscription permission

https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html

## Deploy lambda to certain region

```shell
cd ~/github/aws_infrascode/sam/lambdaSnsElasticsearch

. ./vault.sh
sam build --template ${app}.yml --profile $profile --region $region

sam package --s3-bucket $regionBucketName --output-template packaged.yml  --profile $profile --region $region
sam deploy --template-file packaged.yml --stack-name sam-${app} --parameter-overrides \
snsArn=$snsArn \
esregion=$esregion \
eshost=$eshost \
--capabilities CAPABILITY_NAMED_IAM --profile $profile --region $region

```
