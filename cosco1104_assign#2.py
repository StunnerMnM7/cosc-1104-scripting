import boto3
import time



# AWS resources, default constants and dependency initialization
region = "us-east-1"
ec2_client = boto3.client("ec2", region_name=region)
autoscaling_client = boto3.client("autoscaling", region_name=region)

# Security group config
sec_grp_name = "assign2-sg"
http_port = 80  
ssh_port = 22 
#HTTPS = 443
#RDS_PORT = 5432


# Instance Details
instance_type = "t2.micro"
key_name = "vockey"
user_data_script = """
#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
echo '<h1>Welcome to the Web Server</h1>' | sudo tee /var/www/html/index.html
"""

# Auto Scaling Group Configuration
launch_template_name = "assign2-web-launch-template"
asg_name = "assign2-web-asg"
asg_desired_cap = 2
asg_max_cap = 4
asg_min_cap = 1
asg_policy_name = "assign2_asg_policy"
target_cpu_utilization = 50


def create_security_group():
    response = ec2_client.create_security_group(
        GroupName= sec_grp_name,
        Description= "Custom Security Group for Web Server",
        VpcId =ec2_client.describe_vpcs()["Vpcs"][0]["VpcId"], #Here 0 means it'ss use default VPC 
    )
    sg_id = response["GroupId"]
    print(f"Created security group: {sec_grp_name}, ID: {sg_id}")
    
    ec2_client.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": http_port,
                "ToPort": http_port,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
            },
            {
                "IpProtocol": "tcp",
                "FromPort": ssh_port,
                "ToPort": ssh_port,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
            },
        ],
    )
    print("Configured security group rules.")
    return sg_id


def launch_instance(security_group_id):
    response = ec2_client.run_instances(
        ImageId="ami-0c02fb55956c7d316", # Amazon Linux AMI id for US-east-1
        InstanceType =instance_type,
        KeyName= key_name,
        MinCount=1,
        MaxCount =1,
        SecurityGroupIds=[security_group_id],
        UserData=user_data_script,
    )
    instance_id = response["Instances"][0]["InstanceId"]
    print(f"Launched EC2 instance: {instance_id}")
    return instance_id


def create_custom_ami(instance_id):
    response = ec2_client.create_image(
        InstanceId= instance_id,
        Name ="assign2-web-image",
        Description="Custom image for web server",
    )
    ami_id = response["ImageId"]
    print(f"Created custom AMI: {ami_id}")
    
    waiter = ec2_client.get_waiter("image_available")
    waiter.wait(ImageIds=[ami_id])
    print(f"AMI {ami_id} is now available.")
    return ami_id


def create_launch_template(ami_id, security_group_id):
    response = ec2_client.create_launch_template(
        LaunchTemplateName=launch_template_name,
        LaunchTemplateData={
            "ImageId": ami_id,
            "InstanceType": instance_type,
            "KeyName": key_name,
            "SecurityGroupIds": [security_group_id],
            "UserData": user_data_script.encode("utf-8").decode("latin1"),
        },
    )
    print(f"Created launch template: {launch_template_name}")
    return response["LaunchTemplate"]["LaunchTemplateId"]


def create_auto_scaling_group(launch_template_id):
    response = autoscaling_client.create_auto_scaling_group(
        AutoScalingGroupName=asg_name,
        LaunchTemplate={"LaunchTemplateId": launch_template_id, "Version": "$Latest"},
        MinSize=asg_min_cap,
        MaxSize=asg_max_cap,
        DesiredCapacity=asg_desired_cap,
        AvailabilityZones=["us-east-1a", "us-east-1b"],
        HealthCheckType="EC2",
        HealthCheckGracePeriod=300,
    )
    print(f"Created Auto Scaling Group: {asg_name}")
    return response


def create_scaling_policy():
    response = autoscaling_client.put_scaling_policy(
        AutoScalingGroupName=asg_name,
        PolicyName=asg_policy_name,
        PolicyType="TargetTrackingScaling",
        TargetTrackingConfiguration={
            "PredefinedMetricSpecification": {"PredefinedMetricType": "ASGAverageCPUUtilization"},
            "TargetValue": target_cpu_utilization,
        },
    )
    print(f"Created scaling policy: {asg_policy_name}")
    return response


def display_menu():
    print("Choose a deployment action:")
    print("1. Create Security Group")
    print("2. Launch EC2 Instance")
    print("3. Create AMI")
    print("4. Create Launch Template")
    print("5. Create Auto Scaling Group")
    print("6. Create Scaling Policy")
    print("7. Deploy All Components")
    print("8. Exit")


def main():
    sg_id = None 
    instance_id =None 
    ami_id= None 
    launch_template_id = None

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            sg_id = create_security_group()
        elif choice == "2":
            if sg_id:
                instance_id = launch_instance(sg_id)
            else:
                print("Please create a security group first.")
        elif choice == "3":
            if instance_id:
                ami_id =create_custom_ami(instance_id)
            else:
                print("Please launch an EC2 instance first.")
        elif choice == "4":
            if ami_id and sg_id:
                launch_template_id = create_launch_template(ami_id, sg_id)
            else:
                print("Please create a custom AMI and security group first.")
        elif choice == "5":
            if launch_template_id:
                create_auto_scaling_group(launch_template_id)
            else:
                print("Please create a launch template first.")
        elif choice == "6":
            create_scaling_policy()
        elif choice== "7":
            sg_id = create_security_group()
            instance_id = launch_instance(sg_id)
            time.sleep(60)  # Wait for the instance to initialize
            ami_id = create_custom_ami(instance_id)
            launch_template_id = create_launch_template(ami_id, sg_id)
            create_auto_scaling_group(launch_template_id)
            create_scaling_policy()
            print("All resources deployed successfully ^_^")
        elif choice == "8":
            print("Exiting! :)")
            break
        else:
            print("Invalid choice :( try again.")


if __name__ == "__main__":
    main()
