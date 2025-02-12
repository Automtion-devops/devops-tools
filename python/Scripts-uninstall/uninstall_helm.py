import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Eliminar el binario de Helm
    run_command("sudo rm /usr/local/bin/helm")

    # Verificar la desinstalación de Helm
    try:
        run_command("helm version")
    except subprocess.CalledProcessError:
        print("Helm has been successfully uninstalled.")

if __name__ == "__main__":
    main()