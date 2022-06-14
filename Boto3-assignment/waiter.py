import boto3

def lambda_handler(event, context):
    ec2=boto3.resource("ec2")
    # print(ec2)
    instances=ec2.instances.filter(
            Filters=[
                {
                    "Name":"instance-state-name",
                    "Values":["stopped"]
                }
                ]
            )
    for instance in instances:
        instance.start()
        instance.wait_until_running()
        print("Running")