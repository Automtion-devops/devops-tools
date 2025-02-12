import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Instalar Git
    run_command("sudo apt-get install -y git")

    # Verificar la instalación de Git
    run_command("git --version")

if __name__ == "__main__":
    main()