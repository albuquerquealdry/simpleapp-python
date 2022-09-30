import questionary
import os

def acctionManagement():
    os.system("clear")
    acction = questionary.select(
            "Tempest Script Managemente Resource AWS 🌴 💚 ",
            choices=[
                'List Resources',
                'Exit'
            ]).ask()
            
    if (acction == "List Resources"):
        
        region = questionary.select(
            "Select You Region 🌴 💚 ",
            choices=[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "af-south-1",
                "ap-east-1",
                "ap-southeast-3",
                "ap-south-1",
                "ap-northeast-3",
                "ap-northeast-2",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "ca-central-1",
                "eu-central-1",
                "eu-west-1",
                "eu-west-2",
                "eu-south-1",
                "eu-west-3",
                "eu-north-1",
                "me-south-1",
                "me-central-1",
                "sa-east-1",
                "us-gov-east-1",
                "us-gov-west-1"
            ]).ask()
        resource = questionary.select(
            "Select Resource 🌴 💚 ",
            choices=[
                'Bucket',
                'EC2',
                'EKS',
                'ALL'
            ]).ask()
        if (resource == "EKS"):
            os.system(f"aws eks list-clusters --region {region}")
        if (resource == "EC2"):
            os.system(f"aws ec2 describe-instances --region {region}")
        if (resource == "Bucket"):
            os.system(f"aws s3api list-buckets  --region {region}")
        if (resource == "ALL"):
            os.system(f" aws resourcegroupstaggingapi get-resources --region {region}")
acctionManagement()