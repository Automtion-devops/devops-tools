import os
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.stderr}")

def main():
    install_dir = "/usr/local/aws-cli"  # Ajusta el directorio de instalación si es necesario
    
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Desinstalar AWS CLI
    run_command("sudo apt-get remove -y awscli")
    run_command("sudo apt-get purge -y awscli")
    run_command("sudo apt-get autoremove -y")

    # Eliminar el directorio de instalación
    if os.path.exists(install_dir):
        run_command(f"sudo rm -rf {install_dir}")

    # Verificar la desinstalación de AWS CLI
    try:
        run_command("aws --version")
    except subprocess.CalledProcessError:
        print("AWS CLI has been successfully uninstalled.")

if __name__ == "__main__":
    main()