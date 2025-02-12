import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Eliminar el binario de Argo CD
    run_command("sudo rm /usr/local/bin/argocd")

    # Verificar la desinstalación de Argo CD
    try:
        run_command("argocd version --client")
    except subprocess.CalledProcessError:
        print("Argo CD has been successfully uninstalled.")

if __name__ == "__main__":
    main()