import os
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.stderr}")

def main():
    install_dir = "/home/jaime/Escritorio/devops-scripts/python/Install/aws_cli"
    os.makedirs(install_dir, exist_ok=True)
    
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Instalar dependencias
    run_command("sudo apt-get install unzip -y")

    # Descargar el instalador de AWS CLI
    run_command(f"curl 'https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip' -o '{install_dir}/awscliv2.zip'")
    
    # Descomprimir el archivo descargado
    run_command(f"unzip {install_dir}/awscliv2.zip -d {install_dir}")
    
    # Ejecutar el instalador
    run_command(f"sudo {install_dir}/aws/install")

    # Verificar la instalación de AWS CLI
    run_command("aws --version")

if __name__ == "__main__":
    main()
