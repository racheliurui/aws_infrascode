
# Feature

- Auto stop all ec2 being used

# Step 1: Download Script


```shell
cd ~/github
git clone git@github.com:racheliurui/aws_infrascode.git
```



# Step 2: Set up Variable

```shell
cd ~/github/aws_infrascode/sam/auto_stop
cp sample.sh vault.sh
```

* Edit the variables in vault.ps1.


## Deploy Dynamic DNS to certain region

```bash
cd ~/github/aws_infrascode/sam/auto_stop

sam build --template auto_stop.yml --profile $profile --region $region
sam package --s3-bucket $regionBucketName --output-template packaged.yml  --profile $profile --region $region
sam deploy --template-file packaged.yml --stack-name sam-autostop --capabilities CAPABILITY_NAMED_IAM --profile $profile --region $region
```
