#!/bin/bash

echo "Creado entorno virtual con conda"

# Activar Conda
source /home/mikel/miniconda3/bin/activate
conda init --all

# Crear un entorno Conda (si no existe)
conda create --name MLenv python=3.13 -y

# Activar el entorno recién creado
conda activate MLenv

# Opcional: Instalar paquetes en el entorno
conda install pip -y

# instalamos los paquetes del proyecto
pip install -r /home/mikel/devproject/requeriments.txt -y

echo "El entorno mi_entorno ha sido activado."