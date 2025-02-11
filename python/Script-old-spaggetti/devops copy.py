import os
import time
from colorama import init, Fore, Style
import subprocess
import platform
import psutil

# Initialize colorama
init(autoreset=True)

# Function to print the welcome message
def print_welcome_message():
    print(Fore.CYAN + Style.BRIGHT + "****************************************")
    print(Fore.CYAN + Style.BRIGHT + "*                                      *")
    print(Fore.CYAN + Style.BRIGHT + "*            Welcome to                *")
    print(Fore.CYAN + Style.BRIGHT + "*         DEVOPS TOOLS SCRIPT          *")
    print(Fore.CYAN + Style.BRIGHT + "*                                      *")
    print(Fore.CYAN + Style.BRIGHT + "*           By Andres Henao            *")
    print(Fore.CYAN + Style.BRIGHT + "*                                      *")
    print(Fore.CYAN + Style.BRIGHT + "****************************************")
    time.sleep(0.5)

# Function to show system information
def show_system_info():
    print("\nSystem Information:")
    print()
    print(f"System Name: {platform.system()}")
    print(f"Host Name: {platform.node()}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"OS Version: {platform.version()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Connected Users: {len(psutil.users())}")
    print(f"Public IP: {subprocess.run(['curl', 'ifconfig.me'], capture_output=True, text=True).stdout.strip()}")
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_string = time.strftime('%H:%M:%S', time.gmtime(uptime_seconds))
    print(f"Uptime: {uptime_string}")
    print()

# Function to show disk usage
def show_disk_usage():
    print("\nDisk Usage:")
    print()
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Partition {partition.device}:")
        print(f"  Mount Point: {partition.mountpoint}")
        print(f"  File System Type: {partition.fstype}")
        print(f"  Total Space: {usage.total / (1024 ** 3):.2f} GB")
        print(f"  Used Space: {usage.used / (1024 ** 3):.2f} GB")
        print(f"  Free Space: {usage.free / (1024 ** 3):.2f} GB")
        print(f"  Used Percentage: {usage.percent}%")
    print()

# Function to show running processes
def show_running_processes():
    print("\nRunning Processes:")
    print()
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, User: {proc.info['username']}")
    print(f"Running Processes: {len(psutil.pids())}")
    print()

# Function to show CPU usage
def show_cpu_usage():
    print()
    print("\nCPU Usage")
    print(f"CPU Usage Percentage: {psutil.cpu_percent(interval=1)}%")
    print(f"CPU Usage Per Core: {psutil.cpu_percent(interval=1, percpu=True)}%")
    print()

# Function to show memory usage
def show_memory_usage():
    print("\nMemory Usage:")
    print()
    memory = psutil.virtual_memory()
    print(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {memory.available / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {memory.used / (1024 ** 3):.2f} GB")
    print(f"Used Percentage: {memory.percent}%")
    print()

# Function to update the system
def update_upgrade_system():
    print("Updating the system...")
    print()
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'full-upgrade', '-y'])
    print(f"Available Updates: {subprocess.run(['apt', 'list', '--upgradable'], capture_output=True, text=True).stdout.count('upgradable')}")
    print()

# Function to show htop
def show_htop():
    print("Showing htop...")
    print()
    try:
        subprocess.run(['htop'])
    except FileNotFoundError:
        print("Error: 'htop' is not installed.")
        choice = input("Do you want to install 'htop'? (1 for yes, 0 for no): ")
        if choice == '1':
            try:
                subprocess.run(['sudo', 'apt-get', 'install', '-y', 'htop'])
                print("htop installed successfully. Please try again.")
            except subprocess.CalledProcessError:
                print("Error trying to install 'htop'.")
        else:
            print("Returning to menu.")
    print()

# Function to install applications
def install_app():
    app_name = input("Enter the name of the application you want to install: ")
    try:
        result = subprocess.run([app_name, '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"{app_name} is already installed. The version is: {result.stdout.strip()}")
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        try:
            subprocess.run(['sudo', 'apt-get', 'install', '-y', app_name])
            print(f"{app_name} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Error trying to install {app_name}.")

# System menu
def system_menu():
    while True:
        print("\nSystem Menu")
        print()
        print("1. Show system information")
        print("2. Show disk usage")
        print("3. Show running processes")
        print("4. Show CPU usage")
        print("5. Show memory usage")
        print("6. Update system")
        print("7. Show htop")
        print("8. Install application")
        print("9. Back")
        print()
        choice = input("Select an option: ")
        print()

        if choice == '1':
            show_system_info()
        elif choice == '2':
            show_disk_usage()
        elif choice == '3':
            show_running_processes()
        elif choice == '4':
            show_cpu_usage()
        elif choice == '5':
            show_memory_usage()
        elif choice == '6':
            update_upgrade_system()
        elif choice == '7':
            show_htop()
        elif choice == '8':
            install_app()
        elif choice == '9':
            break
        else:
            print("Invalid selection. Please try again.")

# Function to install tools
def install_tools():
    scripts_dir = "/home/jaime/Escritorio/devops-scripts/python/Scripts"
    if not os.path.exists(scripts_dir):
        print(f"The directory {scripts_dir} does not exist.")
        return

    while True:
        tools = [f for f in os.listdir(scripts_dir) if os.path.isfile(os.path.join(scripts_dir, f))]
        if not tools:
            print("No tools available for installation.")
            return

        print("Select a tool to install:")
        for idx, tool in enumerate(tools, start=1):
            alias = tool.replace('install_', '').replace('_kali_arm', '').replace('.py', '')
            print(f"{idx}. {alias}")
        print("0. Back")
        print("J. Install Jenkins")

        choice = input("Enter the number of the tool you want to install, 'J' to install Jenkins, or '0' to go back: ")
        if choice == '0':
            break
        elif choice.lower() == 'j':
            install_jenkins()
        else:
            try:
                choice = int(choice)
                if 1 <= choice <= len(tools):
                    tool_to_install = tools[choice - 1]
                    print(f"Installing {tool_to_install}...")
                    try:
                        result = subprocess.run(['python3', os.path.join(scripts_dir, tool_to_install)], check=True, capture_output=True, text=True)
                        print(f"{tool_to_install} installed successfully.")
                        print(result.stdout)
                    except subprocess.CalledProcessError:
                        print(f"Error trying to install {tool_to_install}.")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# Function to install Jenkins
def install_jenkins():
    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'openjdk-11-jdk'], check=True)
        subprocess.run(['wget', '-q', '-O', '-', 'https://pkg.jenkins.io/debian/jenkins.io.key', '|', 'sudo', 'apt-key', 'add', '-'], check=True)
        subprocess.run(['sudo', 'sh', '-c', 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'], check=True)
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'jenkins'], check=True)
        subprocess.run(['sudo', 'systemctl', 'start', 'jenkins'], check=True)
        subprocess.run(['sudo', 'systemctl', 'enable', 'jenkins'], check=True)
        print("Jenkins installed and started successfully.")
    except subprocess.CalledProcessError:
        print("Error trying to install Jenkins.")

# Function to update tools
def update_tools():
    scripts_dir = "/home/jaime/Escritorio/devops-scripts/python/Scripts"
    if not os.path.exists(scripts_dir):
        print(f"The directory {scripts_dir} does not exist.")
        return

    while True:
        tools = [f for f in os.listdir(scripts_dir) if os.path.isfile(os.path.join(scripts_dir, f))]
        if not tools:
            print("No tools available for update.")
            return

        print("Select a tool to update:")
        for idx, tool in enumerate(tools, start=1):
            alias = tool.replace('install_', '').replace('_kali_arm', '').replace('.py', '')
            print(f"{idx}. {alias}")
        print("0. Back")

        choice = input("Enter the number of the tool you want to update or '0' to go back: ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(tools):
                tool_to_update = tools[choice - 1]
                print(f"Updating {tool_to_update}...")
                try:
                    result = subprocess.run(['python3', os.path.join(scripts_dir, tool_to_update)], check=True, capture_output=True, text=True)
                    print(f"{tool_to_update} updated successfully.")
                    print(result.stdout)
                except subprocess.CalledProcessError:
                    print(f"Error trying to update {tool_to_update}.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to clone a GitHub repository
def clone_repository():
    repo_url = input("Enter the GitHub repository URL to clone: ")
    try:
        subprocess.run(['git', 'clone', repo_url], check=True)
        print("Repository cloned successfully.")
    except subprocess.CalledProcessError:
        print("Error trying to clone the repository.")

# Function to list GitHub repositories of a user
def list_repositories():
    username = input("Enter the GitHub username: ")
    try:
        result = subprocess.run(['curl', f'https://api.github.com/users/{username}/repos'], capture_output=True, text=True)
        if result.returncode == 0:
            repos = result.stdout
            print(f"Repositories of {username}:")
            print(repos)
        else:
            print("Error fetching repositories.")
    except subprocess.CalledProcessError:
        print("Error trying to fetch repositories.")

# Function to create a new GitHub repository
def create_repository():
    repo_name = input("Enter the name of the new repository: ")
    description = input("Enter the description of the new repository: ")
    private = input("Should the repository be private? (yes/no): ").lower() == 'yes'
    try:
        result = subprocess.run([
            'curl', '-u', 'USERNAME:TOKEN',  # Replace USERNAME and TOKEN with your GitHub username and token
            '-d', f'{{"name": "{repo_name}", "description": "{description}", "private": {str(private).lower()}}}',
            'https://api.github.com/user/repos'
        ], capture_output=True, text=True)
        if result.returncode == 0:
            print("Repository created successfully.")
        else:
            print("Error creating repository.")
    except subprocess.CalledProcessError:
        print("Error trying to create repository.")

# GitHub menu
def github_menu():
    while True:
        print("\nGitHub Menu")
        print()
        print("1. Clone a repository")
        print("2. List repositories of a user")
        print("3. Create a new repository")
        print("4. Back")
        print()
        choice = input("Select an option: ")
        print()

        if choice == '1':
            clone_repository()
        elif choice == '2':
            list_repositories()
        elif choice == '3':
            create_repository()
        elif choice == '4':
            break
        else:
            print("Invalid selection. Please try again.")

# Function to list EC2 instances
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

# Function to start an EC2 instance
def start_ec2_instance():
    instance_id = input("Enter the EC2 instance ID to start: ")
    try:
        subprocess.run(['aws', 'ec2', 'start-instances', '--instance-ids', instance_id], check=True)
        print(f"EC2 instance {instance_id} started successfully.")
    except subprocess.CalledProcessError:
        print(f"Error trying to start EC2 instance {instance_id}.")

# Function to stop an EC2 instance
def stop_ec2_instance():
    instance_id = input("Enter the EC2 instance ID to stop: ")
    try:
        subprocess.run(['aws', 'ec2', 'stop-instances', '--instance-ids', instance_id], check=True)
        print(f"EC2 instance {instance_id} stopped successfully.")
    except subprocess.CalledProcessError:
        print(f"Error trying to stop EC2 instance {instance_id}.")

# Function to configure AWS CLI
def configure_aws_cli():
    print(Fore.RED + "Remember to install AWS CLI and configure the config file.")
    input("Press Enter to continue...")
    try:
        subprocess.run(['aws', 'sso', 'login', '--sso-session', 'nexus'], check=True)
        print("AWS CLI configured successfully.")
    except subprocess.CalledProcessError:
        print("Error trying to configure AWS CLI.")

# AWS menu
def aws_menu():
    while True:
        print("\nAWS Menu")
        print()
        print("1. Configure AWS CLI")
        print("2. List EC2 instances")
        print("3. Start an EC2 instance")
        print("4. Stop an EC2 instance")
        print("5. Back")
        print()
        choice = input("Select an option: ")
        print()

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

# Function to list Kubernetes pods
def list_pods():
    try:
        result = subprocess.run(['kubectl', 'get', 'pods'], capture_output=True, text=True)
        if result.returncode == 0:
            pods = result.stdout
            print("Kubernetes Pods:")
            print(pods)
        else:
            print("Error fetching pods.")
    except subprocess.CalledProcessError:
        print("Error trying to fetch pods.")

# Function to create a Kubernetes pod
def create_pod():
    pod_name = input("Enter the name of the new pod: ")
    image = input("Enter the container image for the pod: ")
    try:
        subprocess.run(['kubectl', 'run', pod_name, '--image', image], check=True)
        print(f"Pod {pod_name} created successfully.")
    except subprocess.CalledProcessError:
        print(f"Error trying to create pod {pod_name}.")

# Function to delete a Kubernetes pod
def delete_pod():
    pod_name = input("Enter the name of the pod to delete: ")
    try:
        subprocess.run(['kubectl', 'delete', 'pod', pod_name], check=True)
        print(f"Pod {pod_name} deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Error trying to delete pod {pod_name}.")

# Function to run k9s
def run_k9s():
    try:
        subprocess.run(['k9s'], check=True)
    except FileNotFoundError:
        print("Error: 'k9s' is not installed.")
        choice = input("Do you want to install 'k9s'? (1 for yes, 0 for no): ")
        if choice == '1':
            try:
                subprocess.run(['sudo', 'apt-get', 'install', '-y', 'k9s'])
                print("k9s installed successfully. Please try again.")
            except subprocess.CalledProcessError:
                print("Error trying to install 'k9s'.")
        else:
            print("Returning to menu.")
    print()

# Function to update kube-config
def update_kube_config():
    cluster_name = input("Enter the cluster name: ")
    region = input("Enter the AWS region: ")
    try:
        subprocess.run(['aws', 'eks', 'update-kubeconfig', '--name', cluster_name, '--region', region], check=True)
        print("kube-config updated successfully.")
    except subprocess.CalledProcessError:
        print("Error trying to update kube-config.")

# Kubernetes menu
def k8s_menu():
    while True:
        print("\nKubernetes Menu")
        print()
        print("1. List pods")
        print("2. Create a pod")
        print("3. Delete a pod")
        print("4. Run k9s")
        print("5. Update kube-config")
        print("6. Back")
        print()
        choice = input("Select an option: ")
        print()

        if choice == '1':
            list_pods()
        elif choice == '2':
            create_pod()
        elif choice == '3':
            delete_pod()
        elif choice == '4':
            run_k9s()
        elif choice == '5':
            update_kube_config()
        elif choice == '6':
            break
        else:
            print("Invalid selection. Please try again.")

# Main menu
def main_menu():
    print_welcome_message()
    while True:
        print("\nMain Menu")
        print()
        print("1. System")
        print("2. Devops-tools")
        print("3. GitHub")
        print("4. AWS")
        print("5. K8s")
        print("6. Exit")
        print()
        choice = input("Select an option: ")
        print()

        if choice == '1':
            system_menu()
        elif choice == '2':
            while True:
                print("\nDevops-tools Menu")
                print()
                print("1. Install tools")
                print("2. Update tools")
                print("3. Back")
                print()
                sub_choice = input("Select an option: ")
                if sub_choice == '1':
                    install_tools()
                elif sub_choice == '2':
                    update_tools()
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid selection.")
        elif choice == '3':
            github_menu()
        elif choice == '4':
            aws_menu()
        elif choice == '5':
            k8s_menu()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main_menu()