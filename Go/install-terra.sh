#!/bin/bash

# Actualizar el sistema
echo "Actualizando el sistema..."
sudo apt update && sudo apt upgrade -y

# Definir la versión de Terraform a instalar
VERSION="1.5.0"  # Cambia esto a la versión que desees
TERRAFORM_ZIP="terraform_${VERSION}_linux_arm.zip"
TERRAFORM_URL="https://releases.hashicorp.com/terraform/${VERSION}/${TERRAFORM_ZIP}"

# Descargar Terraform
echo "Descargando Terraform ${VERSION}..."
wget $TERRAFORM_URL

# Descomprimir el archivo descargado
echo "Descomprimiendo Terraform..."
unzip $TERRAFORM_ZIP

# Mover el binario a /usr/local/bin/
echo "Moviendo el binario de Terraform a /usr/local/bin/..."
sudo mv terraform /usr/local/bin/

# Verificar la instalación
echo "Verificando la instalación de Terraform..."
terraform -version

# Limpiar los archivos descargados
echo "Limpiando archivos temporales..."
rm $TERRAFORM_ZIP

echo "Terraform instalado correctamente."