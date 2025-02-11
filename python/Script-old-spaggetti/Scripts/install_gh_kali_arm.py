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

    # Descargar el binario de GitHub CLI
    run_command("curl -LO https://github.com/cli/cli/releases/latest/download/gh_2.0.0_linux_arm64.tar.gz")

    # Descomprimir el binario
    try:
        run_command("tar -zxvf gh_2.0.0_linux_arm64.tar.gz")
    except subprocess.CalledProcessError:
        print("Error extracting the tar file.")
        return

    # Mover el binario a /usr/local/bin
    run_command("sudo mv gh_2.0.0_linux_arm64/bin/gh /usr/local/bin/gh")

    # Verificar la instalación de GitHub CLI
    run_command("gh --version")

if __name__ == "__main__":
    main()
