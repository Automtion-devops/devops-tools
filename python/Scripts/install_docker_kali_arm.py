import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Instalar Docker desde los repositorios de Kali
    run_command("sudo apt-get install -y docker.io")

    # Iniciar y habilitar el servicio de Docker
    run_command("sudo systemctl start docker")
    run_command("sudo systemctl enable docker")

    # Verificar la instalación de Docker
    run_command("sudo docker --version")

if __name__ == "__main__":
    main()
