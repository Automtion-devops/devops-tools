import os
import subprocess

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
        print(f"{len(tools) + 1}. Install Jenkins")
        print("0. Back")

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
                install_jenkins()
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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

def devops_tools_menu():
    while True:
        print("\nDevops-tools Menu")
        print("1. Install tools")
        print("2. Update tools")
        print("3. Back")
        choice = input("Select an option: ")
        if choice == '1':
            install_tools()
        elif choice == '2':
            update_tools()
        elif choice == '3':
            break
        else:
            print("Invalid selection. Please try again.")