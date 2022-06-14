import boto3
s3=boto3.resource("s3")
s3.Bucket("testingwithec2permission").download_file("getfile.txt","downgetfile.txt")