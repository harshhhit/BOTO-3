import boto3
from botocore.exceptions import ClientError

def create_ec2_instance():
    ec2 = boto3.client("ec2")

    try:
        response = ec2.run_instances(
            ImageId="ami-07b36ea9852e986ad",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="keypair1"
        )

        instance_id = response['Instances'][0]['InstanceId']
        print(f"Instance {instance_id} created successfully.")

    except ClientError as e:
        print(f"Error creating EC2 instance: {e}")

# Run the function to create an EC2 instance
create_ec2_instance()












