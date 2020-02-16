accountId='1234567'
profile='aaa'
aws_access_key_id='bbbbb'
aws_secret_access_key='ccccccc'
aws configure set aws_access_key_id $aws_access_key_id --profile $profile
aws configure set aws_secret_access_key $aws_secret_access_key --profile $profile

export region='ap-southeast-2'
# recommend to use the DNS Domain Name to make it unique
export s3bucket=$profile
export regionBucketName=${s3bucket}.sam.${region}


export snsArn='arn:aws:sns:ap-southeast-2:12345656:testTopic'
export app='lambdaSnsElasticsearch'
