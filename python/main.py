from system.system import system_menu
from devops_tools.devops_tools import devops_tools_menu
from github.github_menu import github_menu
from aws.aws import aws_menu
from k8s.k8s import k8s_menu
from docker.docker import docker_menu

def print_welcome_message():
    print("****************************************")
    print("*                                      *")
    print("*            Welcome to                *")
    print("*         DEVOPS TOOLS SCRIPT          *")
    print("*                                      *")
    print("*           By Andres Henao            *")
    print("*                                      *")
    print("****************************************")

def main_menu():
    print()
    print_welcome_message()
    while True:
        print("\nMain Menu")
        print()
        print("1. System")
        print("2. Devops-tools")
        print("3. GitHub")
        print("4. AWS")
        print("5. K8s")
        print("6. Docker")
        print("7. Exit")
        print()
        choice = input("Select an option: ")
        if choice == '1':
            system_menu()
        elif choice == '2':
            devops_tools_menu()
        elif choice == '3':
            github_menu()
        elif choice == '4':
            aws_menu()
        elif choice == '5':
            k8s_menu()
        elif choice == '6':
            docker_menu()
        elif choice == '7':
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main_menu()