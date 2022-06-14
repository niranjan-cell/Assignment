import boto3
def deleting_res_ec2(region,terminate):
    AWS_REGION='us-east-1'
    ec2_resources=boto3.resource('ec2',region_name=AWS_REGION)

    INSTANT_STATE='running'
    instances = ec2_resources.instances.filter(
        Filters=[
            {
                'Name':'instance-state-name',
                'Values':[
                    INSTANT_STATE
                ]
            }
        ]
    )
    for instance in instances:
        print(instance.id)
    if terminate:
        for instance in instances:
            instance.terminate()
            print(f"terminating {instance.id }." )
            instance.wait_until_terminated()
            print(f"The ec2 instance with instance ID {instance.id} is terminated.")


region='us-east-1'
terminate=False
deleting_res_ec2(region,terminate)