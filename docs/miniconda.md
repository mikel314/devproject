# Set up virtual envs with conda

## Introducción

Hay varias formas de gestionar entornos virtuales en Python, para los proyectos de ML es común usar [Miniconda](https://docs.anaconda.com/miniconda/).

En esta documentación se describe la configuración más basica, para más información y opciones, se puede consultar este tutorial completo de como [gestionar entornos virutales con miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

## Set up miniconda

Todo el set de miniconda y la creación del entorno virtual de python se ejecutan desde el Vagrantfile en el momento de crear la VM. A continuación se describe con motivos didácticos el proceso.

Para instalar miniconda en la VM con:

```console
    sudo mkdir -p /home/mikel/miniconda3
    sudo wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /home/mikel/miniconda3/miniconda.sh
    sudo bash /home/mikel/miniconda3/miniconda.sh -b -u -p /home/mikel/miniconda3
    sudo rm /home/mikel/miniconda3/miniconda.sh
```

Esta instalación no añade ``conda`` al ``PATH`` ni activa el miniconda. Para ello es necesario hacer (solo la primera vez)
```console
source /home/mikel/miniconda3/bin/activate
conda init --all
```

Una vez instalado, podremos crear un entorno nuevo con:
```console
conda create -n mi_entorno python=3.12.9
```
(o la versión de python que desees). 

Una vez creado se activa con:
```console
conda activate mi_entorno 
```
Una vez creado y activado podemos instalar paquetes con ``conda install pkg_name`` o tambien con ``pip install pkg_name`` tras instalar el pip con ``conda install pip`` (recomendado)

Si queremos instalar los paquetes desde un archivo de requeriments, con el entorno activado ejecutaremos
```console
pip install -r ruta_al_requeriments.txt
```
Si en cambio, queremos actualizar el requeriments a medida que vayamos instalando paquetes, haremos:
```console
pip freeze > requirements.txt
```


## Conda environments desde VS code

En el tutorial [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments) se puede consultar como elegir y gestionar los diferentes environmetns desde VS Code



