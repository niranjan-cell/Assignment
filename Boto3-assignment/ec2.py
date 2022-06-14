import boto3
client = boto3.client('ec2')

resp = client.run_instances(ImageId='ami-0e1d30f2c40c4c701',
                            InstanceType='t2.micro',
                            MinCount=1,
                            MaxCount=1)
                            
                            
                            
for instance in resp['Instances']:
    print(instance['InstanceId'])
"""
wget https://www.python.org/ftp/python/3.7.11/Python-3.7.11.tgz
for installing the linux
"""
