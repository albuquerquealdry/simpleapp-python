import questionary
import os

def acctionManagement():
    os.system("clear")
    acction = questionary.select(
            "Tempest Script Managemente Resource AWS 🌴 💚 ",
            choices=[
                'List  All Resources',
                'Set EC2',
                'List Bucket'
                'Exit'
            ]).ask()
    if (acction == "List Resources"):
        print(os.system("aws resourcegroupstaggingapi get-resources --region us-east-1")

    
acctionManagement()