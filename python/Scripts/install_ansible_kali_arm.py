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

    # Instalar dependencias
    run_command("sudo apt-get install -y software-properties-common")

    # Añadir el repositorio de Ansible (Kali Linux no usa PPA, se usa pip)
    try:
        run_command("sudo apt-add-repository --yes --update ppa:ansible/ansible")
    except subprocess.CalledProcessError:
        print("Error adding PPA repository. Skipping this step.")

    # Instalar Ansible
    run_command("sudo apt-get install -y ansible")

    # Verificar la instalación de Ansible
    run_command("ansible --version")

if __name__ == "__main__":
    main()
