======================
Set up VM with vagrant
======================

Introduction
============

Vagrant permite crear maquina virtuales mediante codigo, como Terraform pero para entornos locales. En este caso la crearemos sobre un Virtualbox.
Tambien permite instalar aplicaciones en la VM en el momento de la creación.
Para ello seguiremos los siguientes pasos

* Instalar Vagrant
* Editar el ``Vagrantfile``
* Ejecutar Vagrant y crear la VM

La idea es configurar la VM lo máximo posible desde el inicio, Asi si tenemos que eliminarla y volverla a crear, no perderemos tiempo en su setup.
En este caso la instalción es en Windows dado que el host de toda la infra es Windows.

.. code-block:: python

   print("Hello World")

Instalar Vagrant
================

1.  Descargar e instalar Vagrant desde https://www.vagrantup.com/
2.  Crear la carpeta que contendra la configuración de la VM. En este caso la incluimos dentro del repositorio git en la carpeta infraestructura.

.. code-block:: bash

    mkdir vagrant && cd vagrant

3.  Crear el ``Vagrantfile`` en la carpeta del proyecto






