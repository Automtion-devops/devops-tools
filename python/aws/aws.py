import subprocess

def configure_aws_cli():
    print("Remember to install AWS CLI and configure the config file.")
    input("Press Enter to continue...")
    try:
        subprocess.run(['aws', 'sso', 'login', '--sso-session', 'nexus'], check=True)
        print("AWS CLI configured successfully.")
    except subprocess.CalledProcessError:
        print("Error trying to configure AWS CLI.")

def list_ec2_instances():
    try:
        result = subprocess.run(['aws', 'ec2', 'describe-instances'], capture_output=True, text=True)
        if result.returncode == 0:
            instances = result.stdout
            print("EC2 Instances:")
            print(instances)
        else:
            print("Error fetching EC2 instances.")
    except subprocess.CalledProcessError:
        print("Error trying to fetch EC2 instances.")

def start_ec2_instance():
    instance_id = input("Enter the EC2 instance ID to start: ")
    try:
        subprocess.run(['aws', 'ec2', 'start-instances', '--instance-ids', instance_id], check=True)
        print(f"EC2 instance {instance_id} started successfully.")
    except subprocess.CalledProcessError:
        print(f"Error trying to start EC2 instance {instance_id}.")

def stop_ec2_instance():
    instance_id = input("Enter the EC2 instance ID to stop: ")
    try:
        subprocess.run(['aws', 'ec2', 'stop-instances', '--instance-ids', instance_id], check=True)
        print(f"EC2 instance {instance_id} stopped successfully.")
    except subprocess.CalledProcessError:
        print(f"Error trying to stop EC2 instance {instance_id}.")

def aws_menu():
    while True:
        print("\nAWS Menu")
        print("1. Configure AWS CLI")
        print("2. List EC2 instances")
        print("3. Start an EC2 instance")
        print("4. Stop an EC2 instance")
        print("5. Back")
        choice = input("Select an option: ")
        if choice == '1':
            configure_aws_cli()
        elif choice == '2':
            list_ec2_instances()
        elif choice == '3':
            start_ec2_instance()
        elif choice == '4':
            stop_ec2_instance()
        elif choice == '5':
            break
        else:
            print("Invalid selection. Please try again.")