import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Descargar el binario de Argo CD
    run_command("curl -LO https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-arm64")

    # Hacer el binario ejecutable
    run_command("chmod +x argocd-linux-arm64")

    # Mover el binario a /usr/local/bin
    run_command("sudo mv argocd-linux-arm64 /usr/local/bin/argocd")

    # Verificar la instalación de Argo CD
    run_command("argocd version --client")

if __name__ == "__main__":
    main()
