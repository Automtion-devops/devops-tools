import platform
import psutil
import subprocess
import time

def show_system_info():
    print("\nSystem Information:")
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

def show_disk_usage():
    print("\nDisk Usage:")
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Partition {partition.device}:")
        print(f"  Mount Point: {partition.mountpoint}")
        print(f"  File System Type: {partition.fstype}")
        print(f"  Total Space: {usage.total / (1024 ** 3):.2f} GB")
        print(f"  Used Space: {usage.used / (1024 ** 3):.2f} GB")
        print(f"  Free Space: {usage.free / (1024 ** 3):.2f} GB")
        print(f"  Used Percentage: {usage.percent}%")

def show_running_processes():
    print("\nRunning Processes:")
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, User: {proc.info['username']}")
    print(f"Running Processes: {len(psutil.pids())}")

def show_cpu_usage():
    print("\nCPU Usage")
    print(f"CPU Usage Percentage: {psutil.cpu_percent(interval=1)}%")
    print(f"CPU Usage Per Core: {psutil.cpu_percent(interval=1, percpu=True)}%")

def show_memory_usage():
    print("\nMemory Usage:")
    memory = psutil.virtual_memory()
    print(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {memory.available / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {memory.used / (1024 ** 3):.2f} GB")
    print(f"Used Percentage: {memory.percent}%")

def update_upgrade_system():
    print("Updating the system...")
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'full-upgrade', '-y'])
    print(f"Available Updates: {subprocess.run(['apt', 'list', '--upgradable'], capture_output=True, text=True).stdout.count('upgradable')}")

def show_htop():
    print("Showing htop...")
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

def system_menu():
    while True:
        print("\nSystem Menu")
        print("1. Show system information")
        print("2. Show disk usage")
        print("3. Show running processes")
        print("4. Show CPU usage")
        print("5. Show memory usage")
        print("6. Update system")
        print("7. Show htop")
        print("8. Install application")
        print("9. Back")
        choice = input("Select an option: ")
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