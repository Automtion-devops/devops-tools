import subprocess

def list_containers():
    try:
        result = subprocess.run(['docker', 'ps', '-a'], capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError:
        print("Error listing containers.")

def list_images():
    try:
        result = subprocess.run(['docker', 'images'], capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError:
        print("Error listing images.")

def start_container():
    container_id = input("Enter the container ID or name to start: ")
    try:
        subprocess.run(['docker', 'start', container_id], check=True)
        print(f"Container {container_id} started successfully.")
    except subprocess.CalledProcessError:
        print(f"Error starting container {container_id}.")

def stop_container():
    container_id = input("Enter the container ID or name to stop: ")
    try:
        subprocess.run(['docker', 'stop', container_id], check=True)
        print(f"Container {container_id} stopped successfully.")
    except subprocess.CalledProcessError:
        print(f"Error stopping container {container_id}.")

def remove_container():
    container_id = input("Enter the container ID or name to remove: ")
    try:
        subprocess.run(['docker', 'rm', container_id], check=True)
        print(f"Container {container_id} removed successfully.")
    except subprocess.CalledProcessError:
        print(f"Error removing container {container_id}.")

def remove_image():
    image_id = input("Enter the image ID or name to remove: ")
    try:
        subprocess.run(['docker', 'rmi', image_id], check=True)
        print(f"Image {image_id} removed successfully.")
    except subprocess.CalledProcessError:
        print(f"Error removing image {image_id}.")

def run_container():
    image_name = input("Enter the image name to run: ")
    container_name = input("Enter the container name (optional): ")
    command = ['docker', 'run', '-d']
    if container_name:
        command.extend(['--name', container_name])
    command.append(image_name)
    try:
        subprocess.run(command, check=True)
        print(f"Container from image {image_name} started successfully.")
    except subprocess.CalledProcessError:
        print(f"Error running container from image {image_name}.")

def docker_menu():
    while True:
        print("\nDocker Menu")
        print("1. List containers")
        print("2. List images")
        print("3. Start a container")
        print("4. Stop a container")
        print("5. Remove a container")
        print("6. Remove an image")
        print("7. Run a container")
        print("8. Back")
        choice = input("Select an option: ")
        if choice == '1':
            list_containers()
        elif choice == '2':
            list_images()
        elif choice == '3':
            start_container()
        elif choice == '4':
            stop_container()
        elif choice == '5':
            remove_container()
        elif choice == '6':
            remove_image()
        elif choice == '7':
            run_container()
        elif choice == '8':
            break
        else:
            print("Invalid selection. Please try again.")