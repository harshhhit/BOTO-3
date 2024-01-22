import boto3
from botocore.exceptions import ClientError

def terminate_ec2_instance(instance_id):
    ec2 = boto3.client("ec2")

    try:
        ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} terminated successfully.")

    except ClientError as e:
        print(f"Error terminating EC2 instance {instance_id}: {e}")

instance_id_to_terminate = 'i-00f22ca72a5cd2a4e'


terminate_ec2_instance(instance_id_to_terminate)
