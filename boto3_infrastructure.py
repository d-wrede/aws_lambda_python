import boto3


def create_vpc():
    # Define the CIDR block for the VPC
    cidr_block = "10.0.0.0/16"

    # Create a VPC
    response = ec2.create_vpc(CidrBlock=cidr_block)

    # Get the VPC ID from the response
    vpc_id = response["Vpc"]["VpcId"]

    # Tag the VPC
    tag_name = "Name"
    tag_value = "MyVPC"
    ec2.create_tags(Resources=[vpc_id], Tags=[{"Key": tag_name, "Value": tag_value}])

    print(f"VPC created with ID: {vpc_id}")
    return vpc_id


def create_internet_gateway(vpc_id):
    # Create an Internet Gateway
    response = ec2.create_internet_gateway()

    # Get the Internet Gateway ID from the response
    igw_id = response["InternetGateway"]["InternetGatewayId"]

    # Tag the Internet Gateway
    tag_name = "Name"
    tag_value = "MyIGW"
    ec2.create_tags(Resources=[igw_id], Tags=[{"Key": tag_name, "Value": tag_value}])

    # Attach the Internet Gateway to the VPC
    ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)

    print(f"Internet Gateway with ID {igw_id} attached to VPC with ID {vpc_id}")
    return igw_id


def create_security_group(vpc_id):
    # Create a security group in the VPC
    response = ec2.create_security_group(
        GroupName="SSHSecurityGroup",
        Description="Security group to allow SSH access from anywhere",
        VpcId=vpc_id,
    )

    # Get the security group ID from the response
    security_group_id = response["GroupId"]

    # Tag the security group
    tag_name = "Name"
    tag_value = "SSHSecurityGroup"
    ec2.create_tags(
        Resources=[security_group_id], Tags=[{"Key": tag_name, "Value": tag_value}]
    )

    # Add an inbound rule to allow SSH traffic (port 22) from any IP address
    ip_protocol = "tcp"
    from_port = 22
    to_port = 22
    cidr_ip = "0.0.0.0/0"

    ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpProtocol=ip_protocol,
        FromPort=from_port,
        ToPort=to_port,
        CidrIp=cidr_ip,
    )

    print(
        f"Security group with ID {security_group_id} created and configured for SSH access from anywhere."
    )
    return security_group_id


def create_private_subnet(vpc_id):
    # Create a subnet with a specific CIDR block in the VPC
    cidr_block_subnet = "10.0.1.0/24"
    response = ec2.create_subnet(VpcId=vpc_id, CidrBlock=cidr_block_subnet)

    # Get the subnet ID from the response
    subnet_id = response["Subnet"]["SubnetId"]

    # Tag the subnet
    tag_name = "Name"
    tag_value = "PrivateSubnet"
    ec2.create_tags(Resources=[subnet_id], Tags=[{"Key": tag_name, "Value": tag_value}])

    print(f"Private subnet with ID {subnet_id} created in VPC with ID {vpc_id}")
    return subnet_id


def create_ec2_instance(subnet_id, security_group_id):
    ami_id = "ami-0df24e148fdb9f1d8"

    # Specify the instance type
    instance_type = "t3.micro"

    # Launch the EC2 instance within the private subnet
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        SubnetId=subnet_id,
        SecurityGroupIds=[security_group_id],
    )

    # Get the instance ID from the response
    instance_id = response["Instances"][0]["InstanceId"]

    # Tag the instance
    tag_name = "Name"
    tag_value = "PrivateInstance"
    ec2.create_tags(Resources=[instance_id], Tags=[{"Key": tag_name, "Value": tag_value}])

    print(
        f"EC2 instance with ID {instance_id} created in the private subnet with ID {subnet_id}"
    )
    return instance_id

def main():
    # Create an EC2 client
    ec2 = boto3.client("ec2", region_name="us-west-2")

    # Create a VPC
    vpc_id = create_vpc()

    # Create an Internet Gateway
    igw_id = create_internet_gateway(vpc_id)

    # Create a security group
    security_group_id = create_security_group(vpc_id)

    # Create a private subnet
    subnet_id = create_private_subnet(vpc_id)

    # Create an EC2 instance
    instance_id = create_ec2_instance(subnet_id, security_group_id)



if __name__ == "__main__":
    main()