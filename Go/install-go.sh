#!/bin/bash

# Actualizar el sistema
echo "Actualizando el sistema..."
sudo apt update && sudo apt upgrade -y

# Definir la versión de Go a instalar
VERSION="1.20.5"  # Cambia esto a la versión que desees
GO_TAR="go${VERSION}.linux-arm64.tar.gz"
GO_URL="https://golang.org/dl/${GO_TAR}"

# Descargar Go
echo "Descargando Go ${VERSION}..."
wget $GO_URL

# Extraer el archivo descargado
echo "Extrayendo Go..."
sudo tar -C /usr/local -xzf $GO_TAR

# Configurar variables de entorno
echo "Configurando variables de entorno..."
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc

# Verificar la instalación
echo "Verificando la instalación de Go..."
go version

# Limpiar archivos temporales
echo "Limpiando archivos temporales..."
rm $GO_TAR

echo "Go instalado correctamente."