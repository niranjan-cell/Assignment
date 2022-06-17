# Connect s3 with ec2
Creating IAM role for ec2.
Attach the IAM role with ec2 go to action and add to ec2.

> setting up the boto3 in ec2
```shell
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
```
> to list the object of s3
```
#aws s3 ls s3://bucket_name
[ec2-user@niranjan ~]$ aws s3 ls s3://testingwithec2permission
2022-04-30 10:06:43     135585 DAA Assessment.pdf
2022-04-30 11:01:33         27 getfile.txt
2022-04-30 10:11:20       1462 rasberry.pem
2022-04-30 11:11:38         19 text.txt

```
putobject history
```bash
[ec2-user@niranjan ~]$ ls
getobject.py  putobject.py  text2.txt  text.txt
[ec2-user@niranjan ~]$ cat putobject.py
import boto3
s3 = boto3.resource('s3')
#s3.meta.client.upload_file("object_name","Bucket_name","file_name")
s3.meta.client.upload_file("text2.txt","testingwithec2permission","text.txt")
[ec2-user@niranjan ~]$ python3 putobject.py
```
![before](https://github.com/niranjan-cell/Assignment/blob/6a09231cce91a896bac6439f2e2e23685d5eed26/Screenshot%20(97).png)
>putobject.py
``` python
import boto3
s3 = boto3.resource('s3')
#s3.meta.client.upload_file("object_name","Bucket_name","file_name")
s3.meta.client.upload_file("text2.txt","testingwithec2permission","text.txt")
```
![after put](https://github.com/niranjan-cell/Assignment/blob/6a09231cce91a896bac6439f2e2e23685d5eed26/Screenshot%20(98).png)
getobject history
```
[ec2-user@niranjan ~]$ ls
getobject.py  putobject.py  text2.txt  text.txt
[ec2-user@niranjan ~]$ cat getobject.py
import boto3
s3=boto3.resource("s3")
#s3.Bucket("BucketName").download_file("object_name","file_name")
s3.Bucket("testingwithec2permission").download_file("getfile.txt","downgetfile.txt")
[ec2-user@niranjan ~]$ python3 getobject.py
[ec2-user@niranjan ~]$ ls
downgetfile.txt  getobject.py  putobject.py  text2.txt  text.txt
[ec2-user@niranjan ~]$
```
> getobject.py
```python
import boto3
s3=boto3.resource("s3")
#s3.Bucket("BucketName").download_file("object_name","file_name")
s3.Bucket("testingwithec2permission").download_file("getfile.txt","downgetfile.txt")
```
![after get](https://github.com/niranjan-cell/Assignment/blob/6a09231cce91a896bac6439f2e2e23685d5eed26/Screenshot%20(99).png)
