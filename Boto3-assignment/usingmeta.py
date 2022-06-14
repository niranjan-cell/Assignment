import boto3

def list_ec2_all_region(event, context):
    intances_all=boto3.resource("ec2")
    ec2_region=[region["RegionName"] for region in intances_all.meta.client.describe_regions()['Regions']]
    INSTANCE_STATE="running"
    ans=[]
    for region in ec2_region:
        # intances=resources
        ec2=boto3.resource("ec2",region)
        # instances=ec2.instances.all()
        instances=ec2.instances.filter(
            Filters=[
                {
                    "Name":"instance-state-name",
                    "Values":[INSTANCE_STATE]
                }
                ]
            )
        for instance in instances:
            ans.append(f" the instance id ={instance.id} is in {region}.")
    return ans
    