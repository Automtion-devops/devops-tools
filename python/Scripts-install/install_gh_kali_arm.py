import subprocess
import os

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise subprocess.CalledProcessError(result.returncode, command)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Añadir el repositorio de GitHub CLI
    run_command("curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg")
    run_command("echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main\" | sudo tee /etc/apt/sources.list.d/github-cli.list")

    # Instalar GitHub CLI
    run_command("sudo apt-get update")
    run_command("sudo apt-get install gh -y")

    # Verificar la instalación de GitHub CLI
    run_command("gh --version")

if __name__ == "__main__":
    main()
