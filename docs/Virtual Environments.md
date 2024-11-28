# Setting Up A Virtual Environment

How to set up a virtual environment.

## Conda Installation
For this, you need to install Conda first. To create a virtual environment named `ENVIRONMENT NAME` using Conda, run this a Terminal shell.
```bash
$ conda create --name ENVIRONMENT NAME
$ conda activate ENVIRONMENT NAME
```
In order to delete `ENVIRONMENT NAME` using Conda, run
```bash
$ conda deactivate
$ conda env remove --name ENVIRONMENT NAME
```