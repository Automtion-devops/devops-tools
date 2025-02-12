import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Eliminar el binario de Minikube
    run_command("sudo rm /usr/local/bin/minikube")

    # Verificar la desinstalación de Minikube
    try:
        run_command("minikube version")
    except subprocess.CalledProcessError:
        print("Minikube has been successfully uninstalled.")

if __name__ == "__main__":
    main()