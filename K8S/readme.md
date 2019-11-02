# Setup kops env

## Setup IAM cops user and group

> https://github.com/kubernetes/kops/blob/master/docs/aws.md

```shell
aws iam create-group --group-name kops
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess --group-name kops
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonRoute53FullAccess --group-name kops
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --group-name kops
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/IAMFullAccess --group-name kops
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonVPCFullAccess --group-name kops
aws iam create-user --user-name kops
aws iam add-user-to-group --user-name kops --group-name kops
aws iam create-access-key --user-name kops
```


## Setup s3 bucket for cluster status store

```bash
aws s3api create-bucket --bucket prefix-example-com-state-store --create-bucket-configuration LocationConstraint=ap-southeast-2
aws s3api put-bucket-encryption --bucket prefix-example-com-state-store --server-side-encryption-configuration '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]}'
```


## Local controller

* setup profile represent kops User
* export env variable

```shell
# Hello world
kops create cluster --name=kubernetes-cluster.${dns} \
--state=s3://${S3Bucket} --zones=${zones} \
--node-count=2
```
