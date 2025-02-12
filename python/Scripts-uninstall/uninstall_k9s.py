import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Eliminar el binario de K9s
    run_command("sudo rm /usr/local/bin/k9s")

    # Verificar la desinstalación de K9s
    try:
        run_command("k9s version")
    except subprocess.CalledProcessError:
        print("K9s has been successfully uninstalled.")

if __name__ == "__main__":
    main()