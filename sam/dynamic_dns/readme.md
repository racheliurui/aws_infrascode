
# Feature

![archi](https://raw.githubusercontent.com/racheliurui/aws_cloudformation/master/sam/dynamic_dns/images/Diagram.PNG)

- Dynamically update DNS record value using EC2 and RDS tag name.

# Step 1: Download Script


```shell
cd ~/github
git clone git@github.com:racheliurui/aws_cloudformation.git
```



# Step 2: Set up Variable

```powershell
cd ~/github/aws_cloudformation/sam/dynamic_dns
Copy-Item -Path "./sample.ps1" -Destination "./vault.ps1"
```

* Edit the variables in vault.ps1.


## Deploy Dynamic DNS to certain region

```powershell
cd ~/github/aws_cloudformation/sam/dynamic_dns
$region='ap-southeast-2'
$regionBucketName=$s3bucket+"."+$region
aws configure set region $region --profile $profile
aws s3 mb s3://$regionBucketName  --region $region --profile $profile


sam build --template dynamic_dns.yml --profile $profile --region $region
sam package --s3-bucket $regionBucketName --output-template packaged.yml  --profile $profile --region $region
sam deploy --template-file packaged.yml --stack-name lambdadynamicdns --parameter-overrides HostedZoneIdVar=$HostedZoneIdVar TagName=$TagName --capabilities CAPABILITY_NAMED_IAM --profile $profile --region $region
```
