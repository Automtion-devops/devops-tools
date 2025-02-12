import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Descargar el binario de K9s
    run_command("curl -LO https://github.com/derailed/k9s/releases/latest/download/k9s_Linux_arm64.tar.gz")

    # Descomprimir el binario
    run_command("tar -zxvf k9s_Linux_arm64.tar.gz")

    # Mover el binario a /usr/local/bin
    run_command("sudo mv k9s /usr/local/bin/")

    # Verificar la instalación de K9s
    run_command("k9s version")

if __name__ == "__main__":
    main()
