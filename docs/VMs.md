# Set up VM with Vagrant

## Introduction

As mentioned in the [Overview](index.md) of this documentation, the development of this project was carried out on a personal physical machine with **Windows 10**. To avoid problems with the _test&learn_ nature of this project and given the limitations of Windows as a development OS, it was decided to create a **Linux** virtual machine deployed with **Virtualbox**.

Although the VM could have been created manually, it was decided to use **Vagrant** as _infrastructure as code_ to learn the technology and facilitate the expected re-deployment of the VM.

Vagrant allows creating virtual machines through code, similar to Terraform but for local environments, and works especially well with Virtualbox. It also allows installing applications on the VM at the time of creation. To do this, we will follow these steps:

- Install Virtualbox
- Install Vagrant
- Create SSH keys
- Edit the `Vagrantfile`
- Run Vagrant and create the VM
- Connect to the VM

The idea is to configure the VM as much as possible from the start, so if we have to delete it and recreate it, we won't waste time on its setup. In this case, the installation is on Windows since the host of the entire infrastructure is Windows.

## Install Virtualbox

Simply follow the steps indicated on the [Virtualbox website](https://www.virtualbox.org/wiki/Downloads).

Since all the configuration will be included in the `Vagrantfile`, nothing else is necessary.

## Install Vagrant

1. Download and install Vagrant from https://www.vagrantup.com/
2. Create the folder that will contain the VM configuration. In this case, we include it within the git repository in the infra folder.

```console
    mkdir vagrant && cd vagrant
```

3. Create the `Vagrantfile` in the project folder. This file contains a very basic specification of the VM.

```console
    vagrant init ubuntu/focal64
```

4. Edit the created `Vagrantfile` to add configuration and install initial applications. See the next section.

## Create SSH keys

Before editing the Vagrantfile, it is advisable to create the SSH keys that will allow us to connect to the VM normally once created. The creation will be done directly on Windows 10.

To do this, open `cmd` and run:

```console
ssh-keygen
```

The keys are saved by default (recommended) in the .ssh folder of the user's home directory. In this case, we named them `ubuntu_server_key`. When it asks for a password, press enter to not create them with a password (the keys themselves are the security).

The public key (ending in .pub) is the one we need to copy to the VM we want to connect to from Windows. This is usually done with:

```console
ssh-copy-id -i ~/.ssh/id_rsa_name.pub user@server
```

However, in this case, we will configure the `Vagrantfile` to automatically copy the keys when creating the VM.

## Edit the `Vagrantfile`

The `Vagrantfile` will contain all the VM configuration:

- VM parameters
- OS update
- Creation of the user mikel with sudo permissions
- Copy of the public key to connect via SSH
- Installation of Miniconda

You can find the [Vagrantfile](./../infra/vagrant/Vagrantfile) in this repository in the `infra/vagrant/` folder with comments in the code.

## Post-installation shell script `post_installs.sh`

I have not been able to activate conda for the user mikel from the vagrant user directly in the `Vagrantfile`. A solution has been to include all the conda activation commands and the creation of the python environment in a shell script and execute it as the user mikel from vagrant.

The shell script `post_installs.sh` in the infra folder contains the instructions described in the [Miniconda documentation](miniconda.md).

```bash
#!/bin/bash

echo "Creating virtual environment with conda"

# Activate Conda
source /home/mikel/miniconda3/bin/activate
conda init --all

# Create a Conda environment (if it doesn't exist)
conda create --name MLenv python=3.13 -y

# Activate the newly created environment
conda activate MLenv

# Optional: Install packages in the environment
conda install pip -y

# Install project packages
pip install -r /home/mikel/devproject/requirements.txt -y

echo "The MLenv environment has been activated."
```

This script is executed from the Vagrantfile with:

```console
sudo chmod +x /home/mikel/devproject/infra/post_installs.sh
sudo -u mikel -i /home/mikel/devproject/infra/post_installs.sh
```

## Run Vagrant and create the VM

Once the `Vagrantfile` is edited, create the VM with:

```console
    vagrant up
```

Other useful commands are:

- Shut down the VM

```console
    vagrant halt
```

- Restart the VM

```console
    vagrant reload
```

- Destroy the VM

```console
     vagrant destroy -f
```

- Connect to the VM (through Vagrant)

```console
    vagrant ssh
```

## Connect to the VM

Finally, check that the VM has been created correctly and that we can access it.

```console
        ssh -i ~/.ssh/ubuntu_server_key mikel@192.168.56.10
```

To connect without always specifying the private key, and to facilitate connection via VS Code, run on Windows:

```console
        ssh-add ~/.ssh/ubuntu_server_key
```

We will need to have the `ssh-agent` installed for this. Now we can directly access with:

```console
        ssh mikel@192.168.56.10
```
