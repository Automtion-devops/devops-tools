import os
import subprocess
import getpass

def install_tools():
    scripts_dir = "/home/jaime/Escritorio/devops-scripts/devops-tools/python/Scripts-install"
    if not os.path.exists(scripts_dir):
        print(f"The directory {scripts_dir} does not exist.")
        return

    while True:
        tools = [f for f in os.listdir(scripts_dir) if os.path.isfile(os.path.join(scripts_dir, f))]
        if not tools:
            print("No tools available for installation.")
            return

        print("Select a tool to install:")
        print()
        for idx, tool in enumerate(tools, start=1):
            alias = tool.replace('install_', '').replace('_kali_arm', '').replace('.py', '')
            print(f"{idx}. {alias}")
        print(f"{len(tools) + 1}. Install Jenkins in Docker")
        print("0. Back")
        print()

        choice = input("Enter the number of the tool you want to install or '0' to go back: ")
        if choice == '0':
            break
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
            elif choice == len(tools) + 1:
                install_jenkins_docker()
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def uninstall_tools():
    scripts_dir = "/home/jaime/Escritorio/devops-scripts/devops-tools/python/Scripts-uninstall"
    if not os.path.exists(scripts_dir):
        print(f"The directory {scripts_dir} does not exist.")
        return

    while True:
        tools = [f for f in os.listdir(scripts_dir) if os.path.isfile(os.path.join(scripts_dir, f))]
        if not tools:
            print("No tools available for uninstallation.")
            return

        print("Select a tool to uninstall:")
        print()
        for idx, tool in enumerate(tools, start=1):
            alias = tool.replace('uninstall_', '').replace('_kali_arm', '').replace('.py', '')
            print(f"{idx}. {alias}")
        print("0. Back")
        print()

        choice = input("Enter the number of the tool you want to uninstall or '0' to go back: ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(tools):
                tool_to_uninstall = tools[choice - 1]
                print(f"Uninstalling {tool_to_uninstall}...")
                try:
                    result = subprocess.run(['python3', os.path.join(scripts_dir, tool_to_uninstall)], check=True, capture_output=True, text=True)
                    print(f"{tool_to_uninstall} uninstalled successfully.")
                    print(result.stdout)
                except subprocess.CalledProcessError:
                    print(f"Error trying to uninstall {tool_to_uninstall}.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def install_docker():
    print("Installing Docker...")
    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'apt-transport-https', 'ca-certificates', 'curl', 'software-properties-common'], check=True)
        subprocess.run(['curl', '-fsSL', 'https://download.docker.com/linux/ubuntu/gpg', '|', 'sudo', 'apt-key', 'add', '-'], check=True)
        subprocess.run(['sudo', 'add-apt-repository', 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable'], check=True)
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'docker-ce'], check=True)
        print("Docker installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing Docker.")
        return False
    return True

def add_user_to_docker_group():
    user = getpass.getuser()
    try:
        subprocess.run(['sudo', 'usermod', '-aG', 'docker', user], check=True)
        print(f"User {user} added to the docker group. Please log out and log back in for the changes to take effect.")
        input("Press Enter to continue after logging back in...")
    except subprocess.CalledProcessError:
        print(f"Error adding user {user} to the docker group.")
        return False
    return True

def install_jenkins_docker():
    print("Please ensure Docker is installed before proceeding.")
    input("Press Enter to continue...")

    try:
        subprocess.run(['docker', '--version'], check=True)
    except subprocess.CalledProcessError:
        print("Docker is not installed. Installing Docker...")
        if not install_docker():
            return

    if not add_user_to_docker_group():
        return

    try:
        subprocess.run(['docker', 'pull', 'jenkins/jenkins:lts'], check=True)
        subprocess.run(['docker', 'run', '-d', '--name', 'jenkins', '-p', '8080:8080', '-p', '50000:50000', '-v', 'jenkins_home:/var/jenkins_home', 'jenkins/jenkins:lts'], check=True)
        print("Jenkins installed and started successfully in Docker.")
        print("\nTo access Jenkins, follow these steps:")
        print("1. Open your web browser and go to http://localhost:8080")
        print("2. Retrieve the initial admin password by running the following command:")
        print("   docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword")
        print("3. Copy the password and paste it into the Jenkins setup page.")
        print("4. Follow the on-screen instructions to complete the setup.")
    except subprocess.CalledProcessError:
        print("Error trying to install Jenkins in Docker.")

def update_tools():
    scripts_dir = "/home/jaime/Escritorio/devops-scripts/devops-tools/python/Scripts-install"
    if not os.path.exists(scripts_dir):
        print(f"The directory {scripts_dir} does not exist.")
        return

    while True:
        tools = [f for f in os.listdir(scripts_dir) if os.path.isfile(os.path.join(scripts_dir, f))]
        if not tools:
            print("No tools available for update.")
            return

        print("Select a tool to update:")
        print()
        for idx, tool in enumerate(tools, start=1):
            alias = tool.replace('install_', '').replace('_kali_arm', '').replace('.py', '')
            print(f"{idx}. {alias}")
        print("0. Back")
        print()

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

def devops_tools_menu():
    while True:
        print("\nDevops-tools Menu")
        print()
        print("1. Install tools")
        print("2. Update tools")
        print("3. Uninstall tools")
        print("4. Back")
        print()
        choice = input("Select an option: ")
        print()
        if choice == '1':
            install_tools()
        elif choice == '2':
            update_tools()
        elif choice == '3':
            uninstall_tools()
        elif choice == '4':
            break
        else:
            print("Invalid selection. Please try again.")