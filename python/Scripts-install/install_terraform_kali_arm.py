import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)

def main():
    # Actualizar el sistema
    run_command("sudo apt-get update")
    run_command("sudo apt-get upgrade -y")

    # Descargar el binario de Terraform
    run_command("curl -LO https://releases.hashicorp.com/terraform/$(curl -s https://checkpoint-api.hashicorp.com/v1/check/terraform | jq -r .current_version)/terraform_$(curl -s https://checkpoint-api.hashicorp.com/v1/check/terraform | jq -r .current_version)_linux_arm64.zip")

    # Descomprimir el binario
    run_command("unzip terraform_*_linux_arm64.zip")

    # Mover el binario a /usr/local/bin
    run_command("sudo mv terraform /usr/local/bin/")

    # Verificar la instalación de Terraform
    run_command("terraform version")

if __name__ == "__main__":
    main()
