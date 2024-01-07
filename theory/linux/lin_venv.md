~~~ txt
 ____     __                                   
|    |   |__| ____   ___  __ ____   _______  __
|    |   |  |/    \  \  \/ // __ \ /    \  \/ /
|    |___|  |   |  \  \   /\  ___/|   |  \   / 
|_______ \__|___|  /   \_/  \___  >___|  /\_/  
        \/       \/             \/     \/      
~~~

[BACK](../THEORY.md)

- [Requirements](#requirements)
  - [requirements.txt](#requirementstxt)
    - [Simple case](#simple-case)
    - [With versions](#with-versions)
    - [Versions semantics](#versions-semantics)
- [Practical example](#practical-example)
  - [Creating the venv](#creating-the-venv)
  - [Activation](#activation)
  - [Usage](#usage)
  - [Deactivation](#deactivation)
- [Content del venv](#content-del-venv)

# Requirements

- Python 3.3 or grater
- It is posible to use a `requirements.txt` file

## requirements.txt

- Each line is a dependency
- The name is just a convention, but it can have different names
  - Example: `requirements-dev.txt`
- It can be created with `pip`:
  - `pip freeze > requirements.txt`
- It can be used to install all dependencies at once after the `venv` has been started
  - `(venv_name) ~/repos/project$ pip install -r requirements.txt`

### Simple case

~~~ python
flask
requests
gunicorn
~~~

### With versions

- If you want an exact version `==`
  - `flask==1.0.0`
- Using an interval
  - `flask>=1.1.2,<2.0`


### Versions semantics

- The convention is to use three numbers separated by dots
  - Example: `1.8.2`
    - `1`: Major version
      - It increases with major changes.
        - Example: architecture
        - Big changes that would break the excecution of old code
    - `8`: Minor version
        - Changes that doesn't break the excecution of old code
        - Example: new features
    - `3`: Patch version
      - Increamented when `bugs` are fixed



# Practical example

## Creating the venv

- Install `venv` in Ubuntu
  - `sudo apt install python3.10-venv`

~~~ sh
cd project_dir
python3 -m venv .venv
~~~

Once created it must be activated

## Activation

When it is activated:

- Changes are applied to the current terminal simulator
  - It has no effect in new terminals
  - The path from where bins and files are search is changed
- The console shows that `venv` is beeing used by adding the name in parenthesis at the begining of the line
  - `(venv_name) ~/repos/project$ `

~~~ sh
# Before activation
which python3
# /usr/bin/python3

# Activation
source .venv/bin/activate

# After activation
which python3
# ~/repos/project/.venv/bin/python3
~~~ 

- You can print the PATH with `echo $PATH`
  - the first element should be the `bin` folder of the `venv`

## Usage

- All `python` commands as well as `pip` commands would be using the binaries of the `vevn`
- When a libreary is installed, example `pip install flask`:
  - The new binary will be installed on `.venv\bin`
    - That is the firt dir on the PATH

- If it is used from `VSCode`:
  - `Ctrl` + `Shift` + `P`
    - `Python: Select Interpeter`
      - Choose the one of the `venv`

## Deactivation

From the active venv sesion run `deactivate`:
  - `(venv_name) ~/repos/project$ deactivate`

# Content del venv

Aquí se muestran los componentes principales de la carpeta que contiene al `venv`:

- include
- lib
- lib64 -> lib
- bin
  - python3
  - pip
-  pyvenv.cfg