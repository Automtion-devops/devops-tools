import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Detener el servicio de Docker
    run_command("sudo systemctl stop docker")

    # Deshabilitar el servicio de Docker
    run_command("sudo systemctl disable docker")

    # Eliminar Docker y sus dependencias
    run_command("sudo apt-get remove -y docker.io")
    run_command("sudo apt-get purge -y docker.io")
    run_command("sudo apt-get autoremove -y")

    # Eliminar directorios y archivos relacionados con Docker
    run_command("sudo rm -rf /var/lib/docker")
    run_command("sudo rm -rf /etc/docker")
    run_command("sudo rm -rf /var/run/docker.sock")

    # Verificar la desinstalación de Docker
    try:
        run_command("sudo docker --version")
    except subprocess.CalledProcessError:
        print("Docker uninstalled successfully.")

if __name__ == "__main__":
    main()