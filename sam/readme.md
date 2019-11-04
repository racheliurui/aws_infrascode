# Step 1: Download Script


```shell
cd ~/github
git clone git@github.com:racheliurui/aws_infrascode.git
```



# Step 2: Set up common Variable on mac/linux

```shell
cd ~/github/aws_infrascode/sam
cp sample.sh vault.sh
```

* Edit the variables in vault.sh.


```shell
region='ap-southeast-2'
regionBucketName=${s3bucket}.${region}
aws configure set region $region --profile $profile
aws s3 mb s3://$regionBucketName  --region $region --profile $profile
```
