import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Descargar el binario de kubectl
    run_command("curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl\"")

    # Hacer el binario ejecutable
    run_command("chmod +x kubectl")

    # Mover el binario a /usr/local/bin
    run_command("sudo mv kubectl /usr/local/bin/")

    # Verificar la instalación de kubectl
    run_command("kubectl version --client")

if __name__ == "__main__":
    main()
