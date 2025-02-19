# Set up virtual envs with conda

## Introduction

There are several ways to manage virtual environments in Python. For ML projects, it is common to use [Miniconda](https://docs.anaconda.com/miniconda/).

This documentation describes the most basic setup. For more information and options, you can refer to this complete tutorial on how to [manage virtual environments with miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

## Set up miniconda

The entire miniconda setup and the creation of the Python virtual environment are executed from the Vagrantfile when creating the VM. Below, the process is described for educational purposes.

To install miniconda on the VM with:

```console
    sudo mkdir -p /home/mikel/miniconda3
    sudo wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /home/mikel/miniconda3/miniconda.sh
    sudo bash /home/mikel/miniconda3/miniconda.sh -b -u -p /home/mikel/miniconda3
    sudo rm /home/mikel/miniconda3/miniconda.sh
```

This installation does not add `conda` to the `PATH` nor activate miniconda. To do this (only the first time):

```console
source /home/mikel/miniconda3/bin/activate
conda init --all
```

Once installed, we can create a new environment with:

```console
conda create -n my_env python=3.12.9
```

(or the Python version you want).

Once created, it is activated with:

```console
conda activate my_env
```

Once created and activated, we can install packages with `conda install pkg_name` or also with `pip install pkg_name` after installing pip with `conda install pip` (recommended).

If we want to install packages from a requirements file, with the environment activated, we will run:

```console
pip install -r path_to_requirements.txt
```

If, on the other hand, we want to update the requirements as we install packages, we will do:

```console
pip freeze > requirements.txt
```

## Conda environments from VS Code

In the tutorial [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments), you can learn how to choose and manage different environments from VS Code.
