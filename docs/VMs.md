# Set up VM with vagrant

## Introducción

Como se comenta en el [Overview](index.md) de esta documentaicón, el desarrollo de este proyecto se realizó en una máquina fisica personal con **Windows 10**. Con el objetivo de evitar problemas con el *test&learn* propio de este proyecto y dado las limitaciones de Windows como OS de desarrollo, se optó por la creación de una máquina virtual **Linux** desplegada con **Virtualbox**.

Aunque la VM se podría haber creado manualmente, se dedició usar **Vagrant** como *infrastructure as a code* con el fin de aprender la tecnología y facilitar el re-despliegue esperado de la VM.

Vagrant permite crear maquina virtuales mediante código, como Terraform pero para entornos locales, funciona especialmente bien con Virtualbox.
Tambien permite instalar aplicaciones en la VM en el momento de la creación.
Para ello seguiremos los siguientes pasos

* Instalar Virtuabox
* Instalar Vagrant
* Crear las claves ssh
* Editar el ``Vagrantfile``
* Ejecutar Vagrant y crear la VM
* Conectarse a la VM

La idea es configurar la VM lo máximo posible desde el inicio, Asi si tenemos que eliminarla y volverla a crear, no perderemos tiempo en su setup.
En este caso la instalción es en Windows dado que el host de toda la infra es Windows.

## Instalar Virtualbox

Sencillamente sigue los pasos indicados en la [Web de Virtualbox](https://www.virtualbox.org/wiki/Downloads)

Dado que toda la configuración se incluira en el ``Vagrantfile``, no es necesario hacer nada más.

## Instalar Vagrant

1.  Descargar e instalar Vagrant desde https://www.vagrantup.com/
2.  Crear la carpeta que contendrá la configuración de la VM. En este caso la incluimos dentro del repositorio git en la carpeta infra.

```console
    mkdir vagrant && cd vagrant
```

3.  Crear el ``Vagrantfile`` en la carpeta del proyecto. Este archivo contiene una especificación muy basica de la VM.

```console
    vagrant init ubuntu/focal64
```

4. Editar el ``Vagrantfile`` que se ha creado para añadir configuración e instalar las aplicaciones iniciales. Ver siguiente seccion

## Crear las claves ssh

Antes de editar el Vagrantfile, es conveniente crear las claves ssh que permitirán conectarnos con la VM de forma normal una vez creada. La creación la realizaremos directaemnte en el Windows10.

Para ello, abrimos el ``cmd`` y ejecutamos

```console
ssh-keygen
```
Las claves se guardan por defecto (recomendado) en la carpeta .ssh del home del usuario que las crea.
En este caso les dimos el nombre ``ubuntu_server_key``
Cuando pida password apretamos enter para no crearlas con password (las claves en sí mismas ya son la seguridad)

La clave pública (acabada en .pub) es la que tenemos que copiar en la VM a la que queraoms contectar desde el Windows.
Este se hace normalmente con
```console
ssh-copy-id -i ~/.ssh/id_rsa_name.pub user@server
```
Sin embargo, en este caso, configuraremos el ``Vagrantfile`` para que copia automaticamente las claves en el momento de crear la VM.


## Editar el ``Vagrantfile``


El ``Vagrantfile`` contendrá toda la configuración de la VM:

* Parámetros de la VM
* Actualización del SO
* Creación del usuario mikel con permisos de sudo
* Copia de la clave publica para poder conectar por ssh
* Instalación de miniconda
*
*

Puedes encontrar el arhivo [Vagrantfile](./../infra/vagrant/Vagrantfile) en este mismo repositorio en la carpeta ``infra/vagrant/`` con los comentarios en el código.

## Scrip shell post_installs.sh

No he sido capaz de activar conda para el usuario mikel desde el usuario vagrant directamente en el ``Vagrantfile``. Una solución ha sido incluir todos los comandos de activación de conda y creación del entorno python en un *shell script* y ejecutarlo como usuario mikel desde el vagrant.

El script shell ``post_installs.sh`` de la carpeta ``infra`` contiene las instrucciones descritas en la [documentación de miniconda](miniconda.md).

```bash
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

echo "El entorno MLenv ha sido activado."
```
Este script es ejecutado desde el Vagrantfile con

```console
sudo chmod +x /home/mikel/devproject/infra/post_installs.sh
sudo -u mikel -i /home/mikel/devproject/infra/post_installs.sh
```

## Ejecutar Vagrant y crear la VM

Una vez editado el ``Vagrantfile`` creamos la VM con

```console
    vagrant up
```

Otros comandos útiles son los siguientes

* Apagar la VM

```console
    vagrant halt
```

* Reiniciar la VM

```console
    vagrant reload
```

* Destruir la VM

```console
     vagrant destroy -f
```

* Conectarse a la VM (a traves de Vagrant)

```console
    vagrant ssh
```

## Conectarse a la VM

Finalmente, comprobamos que la VM se ha creado correctamente y que podemos acceder a ella.

```console
        ssh -i ~/.ssh/ubuntu_server_key mikel@192.168.56.10
```

Para poder conectar sin especificar siempre la clave privada, y para facilitar la conexión por VS code. Ejecutamos en el Windows:

```console
        ssh-add ~/.ssh/ubuntu_server_key
```

Tendremos que tener instalado el ``ssh-agent`` par ello.
Ahora ya podremos acceder directamente con

```console
        ssh mikel@192.168.56.10
```
