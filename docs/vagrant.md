# Set up VM with vagrant

## Introducción

Vagrant permite crear maquina virtuales mediante codigo, como Terraform pero para entornos locales. En este caso la crearemos sobre un Virtualbox.
Tambien permite instalar aplicaciones en la VM en el momento de la creación.
Para ello seguiremos los siguientes pasos

* Instalar Vagrant
* Crear las claves ssh
* Editar el ``Vagrantfile``
* Ejecutar Vagrant y crear la VM
* Conectarse a la VM

La idea es configurar la VM lo máximo posible desde el inicio, Asi si tenemos que eliminarla y volverla a crear, no perderemos tiempo en su setup.
En este caso la instalción es en Windows dado que el host de toda la infra es Windows.

## Vagrant

1.  Descargar e instalar Vagrant desde https://www.vagrantup.com/
2.  Crear la carpeta que contendrá la configuración de la VM. En este caso la incluimos dentro del repositorio git en la carpeta infraestructura.

```bash
    mkdir vagrant && cd vagrant
```

3.  Crear el ``Vagrantfile`` en la carpeta del proyecto. Este archivo contiene una especificación muy basica de la VM.

```bash
    vagrant init ubuntu/focal64
```

4. Editar el ``Vagrantfile`` que se ha creado para añadir configuración e instalar las aplicaciones iniciales. Ver siguiente seccion

## Crear las claves ssh




## Editar el ``Vagrantfile``


El ``Vagrantfile`` contendrá toda la configuración de la VM:

* Parámetros de la VM
* Actualización del SO
* Creación del usuario mikel con permisos de sudo
* Copia de la clave publica para poder conectar por ssh
* Instalación de miniconda

A continuación se presenta el archivo ``Vagrantfile`` del proyecto con los comentarios en el codigo.



## Ejecutar Vagrant y crear la VM

Una vez editado el ``Vagrantfile`` creamos la VM con 

```bash
    vagrant up
```

Otros comandos útiles son los siguientes

* Apagar la VM

```bash
    vagrant halt
```

* Reiniciar la VM

```bash
    vagrant reload
```

* Destruir la VM

```bash
     vagrant destroy -f
```

* Conectarse a la VM (a traves de Vagrant)

```bash
    vagrant ssh
```

## Conectarse a la VM

Finalmente, comprobamos que la VM se ha creado correctamente y que podemos acceder a ella.

```bash
        ssh -i ~/.ssh/ubuntu_server_key mikel@192.168.56.10
```

Para poder conectar sin especificar siempre la clave privada, y para facilitar la conexión por VS code. Ejecutamos:

```bash
        ssh-add ~/.ssh/ubuntu_server_key
```

Tendremos que tener instalado el ssh-agent par ello.
Ahora ya podremos acceder directamente con

```bash
        ssh mikel@192.168.56.10
```

