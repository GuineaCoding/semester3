import boto3

# Set the name of the key pair
key_pair_name = 'keyToTheProjectAWS'

# Combine key pair name with 'week3Lab' for a tag name
tag_name = key_pair_name + 'week3Lab'

# Set the ID of the security group
security_group_id = 'sg-04570d40a75c4df74'

# Commands to set up the server when it starts
user_data_script = """#!/bin/bash
yum update -y
yum install httpd -y
systemctl enable httpd
systemctl start httpd
"""

# Initializing the boto3 EC2 resource
ec2 = boto3.resource('ec2')

# Creating a new EC2 server
new_instances = ec2.create_instances(
    ImageId='ami-0277155c3f0ab2930',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.nano',
    KeyName=key_pair_name,
    SecurityGroupIds=[security_group_id],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': tag_name
                }
            ]
        }
    ],
    UserData=user_data_script
)

# Printing the ID of the new server
print(new_instances[0].id)

