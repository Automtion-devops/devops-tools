import subprocess
import os
import sys
import json

def run_command(command):
    """Ejecuta un comando en la terminal y muestra la salida."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}", file=sys.stderr)

def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Error: El directorio {path} no se encuentra.", file=sys.stderr)
    except NotADirectoryError:
        print(f"Error: {path} no es un directorio.", file=sys.stderr)

def load_repositories(file_path):
    """Carga los repositorios desde un archivo JSON."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encuentra.", file=sys.stderr)
        return {}
    except json.JSONDecodeError:
        print(f"Error: El archivo {file_path} contiene JSON inválido.", file=sys.stderr)
        return {}

def git_status():
    run_command("git status")

def git_pull():
    run_command("git pull")

def git_push():
    run_command("git push origin")

def git_checkout(branch):
    run_command(f"git checkout {branch}")

def git_checkout_main():
    run_command("git checkout main")

def git_branch_delete(branch):
    run_command(f"git branch -D {branch}")

def git_commit(message):
    run_command(f"git commit -am '{message}'")

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
    repos_file_path = '/home/jaime/Escritorio/devops-scripts/devops-tools/python/github/repos.json'
    repos = load_repositories(repos_file_path)

    if not repos or "Repos" not in repos:
        print("No se pudieron cargar los repositorios o el formato del archivo es incorrecto. Regresando al menú principal.")
        return

    # Usa la lista de repositorios directamente desde la clave "Repos"
    repo_list = repos["Repos"]

    while True:
        print("\n\nMenú de GitHub")
        
        print()  # Espacio adicional antes de la lista de repositorios
        for i, repo_path in enumerate(repo_list, start=1):
            repo_name = os.path.basename(repo_path)
            print(f"  {i}. {repo_name}")
        
        print("\n0. Volver al menú principal")  # Espacio antes de esta línea
        
        print()  # Espacio adicional entre las opciones y la selección
        choice = input("Selecciona un repositorio: ")

        if choice == '0':
            break

        try:
            # Obtén el índice de la selección
            selected = int(choice) - 1
           
            if 0 <= selected < len(repo_list):
                found_repo = repo_list[selected]

                if found_repo:
                    change_directory(found_repo)

                    while True:
                        print(f"\n\nAcciones para el repositorio: {found_repo}")
                        print()  # Espacio adicional antes de las acciones
                        print("1. Git Status")
                        print("2. Git Pull")
                        print("3. Git Push")
                        print("4. Git Checkout")
                        print("5. Git Checkout Main")
                        print("6. Git Branch Delete")
                        print("7. Git Commit")
                        print("8. Cambiar Repositorio")
                        print("9. Volver al menú principal")
                        print("10. Clone a repository")
                        print("11. List repositories of a user")
                        print("12. Create a new repository")
                        
                        print()  # Espacio adicional entre las opciones y la selección
                        action_choice = input("Selecciona una acción: ")
                        print()

                        if action_choice == '1':
                            git_status()
                        elif action_choice == '2':
                            git_pull()
                        elif action_choice == '3':
                            git_push()
                        elif action_choice == '4':
                            branch = input("Ingresa el nombre de la rama: ")
                            git_checkout(branch)
                        elif action_choice == '5':
                            git_checkout_main()
                        elif action_choice == '6':
                            branch = input("Ingresa el nombre de la rama a eliminar: ")
                            git_branch_delete(branch)
                        elif action_choice == '7':
                            message = input("Ingresa el mensaje del commit: ")
                            git_commit(message)
                        elif action_choice == '8':
                            break  # Vuelve a la lista de repositorios
                        elif action_choice == '9':
                            break  # Vuelve al menú principal
                        elif action_choice == '10':
                            clone_repository()
                        elif action_choice == '11':
                            list_repositories()
                        elif action_choice == '12':
                            create_repository()
                        else:
                            print("Opción no válida. Intenta de nuevo.")
                else:
                    print("Selección no válida. Intenta de nuevo.")
            else:
                print("Selección no válida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# The entry point of the script
if __name__ == "__main__":
    github_menu()