import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise subprocess.CalledProcessError(result.returncode, command)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Desinstalar GitHub CLI
    run_command("sudo apt-get remove -y gh")

    # Eliminar dependencias no necesarias
    run_command("sudo apt-get autoremove -y")

    # Verificar la desinstalación de GitHub CLI
    try:
        run_command("gh --version")
    except subprocess.CalledProcessError:
        print("GitHub CLI has been successfully uninstalled.")

if __name__ == "__main__":
    main()