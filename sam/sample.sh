accountId='12345567'
profile='abc'
region='ap-southeast-2'
# recommend to use the DNS Domain Name to make it unique
s3bucket='dns.sam'

aws_access_key_id='AAAAAAAAAAAAAA'
aws_secret_access_key='BBBBBBBBBBBBBBBBBBBBBBBBBBBBB'

aws configure set aws_access_key_id $aws_access_key_id --profile $profile
aws configure set aws_secret_access_key $aws_secret_access_key --profile $profile
