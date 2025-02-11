import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Descargar el binario de Minikube
    run_command("curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-arm64")

    # Hacer el binario ejecutable
    run_command("chmod +x minikube-linux-arm64")

    # Mover el binario a /usr/local/bin
    run_command("sudo mv minikube-linux-arm64 /usr/local/bin/minikube")

    # Verificar la instalación de Minikube
    run_command("minikube version")

if __name__ == "__main__":
    main()
