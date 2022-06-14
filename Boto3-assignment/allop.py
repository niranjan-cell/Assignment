import boto3
ec2=boto3.resource("ec2","us-east-1")
"""
instances=ec2.meta.run_instances(
        ImageId='ami-08895422b5f3aa64a',
        MinCount=1,
        MaxCount=2,
        InstanceType='t2.micro',
        KeyName='radha'
        )
"""
## for creating instances
instanceid=[]
imageId=['ami-0022f774911c1d690','ami-08895422b5f3aa64a']
for iD  in imageId:
    instance=ec2.create_instances(
        ImageId=iD,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='radha'
        )
    for inst in instance:
        inst.wait_until_running()
        print(f"{inst.id} is running")
        instanceid.append(inst.id)
ec2=boto3.resource("ec2","us-east-1")

##for stopping instances
for instId in instanceid:
#    ec2=boto3.resource("ec2","us-east-1")
    inst=ec2.instances.filter(InstanceIds=[instId])
    #.stop()
    for ins in inst:
        ins.stop()
        ins.wait_until_stopped()
    print(f"{instId} is stopped")
#for runnug back
for instId in instanceid:
    inst=ec2.instances.filter(InstanceIds=[instId])
    for ins in inst:
        ins.start()
        ins.wait_until_running()
    print(f"{instId} is started")
#fo terminating
for instId in instanceid:
    inst=ec2.instances.filter(InstanceIds=[instId]).terminate()
#    inst.wait_until_terminated()
    print(f"{instId} is terminated")

