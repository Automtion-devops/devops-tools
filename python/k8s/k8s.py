import subprocess

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

def create_pod():
    pod_name = input("Enter the name of the new pod: ")
    image = input("Enter the container image for the pod: ")
    try:
        subprocess.run(['kubectl', 'run', pod_name, '--image', image], check=True)
        print(f"Pod {pod_name} created successfully.")
    except subprocess.CalledProcessError:
        print(f"Error trying to create pod {pod_name}.")

def delete_pod():
    pod_name = input("Enter the name of the pod to delete: ")
    try:
        subprocess.run(['kubectl', 'delete', 'pod', pod_name], check=True)
        print(f"Pod {pod_name} deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Error trying to delete pod {pod_name}.")

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

def update_kube_config():
    cluster_name = input("Enter the cluster name: ")
    region = input("Enter the AWS region: ")
    try:
        subprocess.run(['aws', 'eks', 'update-kubeconfig', '--name', cluster_name, '--region', region], check=True)
        print("kube-config updated successfully.")
    except subprocess.CalledProcessError:
        print("Error trying to update kube-config.")

def k8s_menu():
    while True:
        print("\nKubernetes Menu")
        print("1. List pods")
        print("2. Create a pod")
        print("3. Delete a pod")
        print("4. Run k9s")
        print("5. Update kube-config")
        print("6. Back")
        choice = input("Select an option: ")
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