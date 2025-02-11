import subprocess

def clone_repository():
    repo_url = input("Enter the GitHub repository URL to clone: ")
    try:
        subprocess.run(['git', 'clone', repo_url], check=True)
        print("Repository cloned successfully.")
    except subprocess.CalledProcessError:
        print("Error trying to clone the repository.")

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

def github_menu():
    while True:
        print("\nGitHub Menu")
        print("1. Clone a repository")
        print("2. List repositories of a user")
        print("3. Create a new repository")
        print("4. Back")
        choice = input("Select an option: ")
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