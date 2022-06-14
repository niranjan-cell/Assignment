#!/bin/bash
sudo yum update -y
python --version
pip install boto3
sudo yum update -y
sudo yum install https://repo.ius.io/ius-release-el$(rpm -E '%{rhel}').rpm
sudo yum install -y python3
whereis pip
pip install boto3
$PATH
sudo nano /etc/sudoers
pip3 install boto3

#aws s3 ls s3://bucket_name
[ec2-user@niranjan ~]$ aws s3 ls s3://testingwithec2permission
2022-04-30 10:06:43     135585 DAA Assessment.pdf
2022-04-30 11:01:33         27 getfile.txt
2022-04-30 10:11:20       1462 rasberry.pem
2022-04-30 11:11:38         19 text.txt
