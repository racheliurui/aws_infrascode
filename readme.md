# Infra-as-Code

## Current Status


![infra-status](https://api.travis-ci.org/racheliurui/aws_cloudformation.svg?branch=master)



## Travis Environment Variable

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- region
- s3bucket


## IAM Travis User Access  

* AWS managed ReadOnlyAccess
* Customed policy
  * Travis User should be attached with policy as blow and replace the "YOURBUCKET" using value of s3bucket
  * TravisUserPolicy
    >https://github.com/hashicorp/terraform/issues/2834

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:*"
            ],
            "Resource": "*"
        },
		{
            "Effect": "Allow",
            "Action": [
                        "s3:GetBucketLocation",
                        "s3:ListAllMyBuckets"
                      ],
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::YOURBUCKET",
                "arn:aws:s3:::YOURBUCKET/*"
            ]
        },
		    {
            "Effect": "Allow",
            "Action": "ec2:ReplaceNetworkAcl*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ec2:CreateNetworkAcl*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ec2:DeleteNetworkAcl*",
            "Resource": "*"
        }
    ]
}
```
