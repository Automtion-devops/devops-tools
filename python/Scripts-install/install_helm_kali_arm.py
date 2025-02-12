import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Descargar el binario de Helm
    run_command("curl -LO https://get.helm.sh/helm-v3.7.2-linux-arm64.tar.gz")

    # Descomprimir el binario
    run_command("tar -zxvf helm-v3.7.2-linux-arm64.tar.gz")

    # Mover el binario a /usr/local/bin
    run_command("sudo mv linux-arm64/helm /usr/local/bin/")

    # Verificar la instalación de Helm
    run_command("helm version")

if __name__ == "__main__":
    main()
