~~~ txt
 __      __ __                                   
/  \    /  \__| ____   ___  __ ____   _______  __
\   \/\/   /  |/    \  \  \/ // __ \ /    \  \/ /
 \        /|  |   |  \  \   /\  ___/|   |  \   / 
  \__/\  / |__|___|  /   \_/  \___  >___|  /\_/  
       \/          \/             \/     \/      
~~~

[BACK](../THEORY.md)

**CONTENIDO**

- [Requisitos](#requisitos)
  - [requirements.txt](#requirementstxt)
    - [Caso simple](#caso-simple)
    - [Caso con versiones](#caso-con-versiones)
    - [Semántica de versiones](#semántica-de-versiones)
- [Ejemplo de creación y uso desde cmd](#ejemplo-de-creación-y-uso-desde-cmd)
  - [Resumen](#resumen)
  - [Creación](#creación)
  - [Activación](#activación)
  - [Uso](#uso)
  - [Desactivación](#desactivación)
- [Contenido del venv](#contenido-del-venv)
  - [.venv\\Scripts\\python.exe](#venvscriptspythonexe)

# Requisitos

- Se usa python 3.3 o mayor
- Se puede crear usando un fichero `requirements.txt`

## requirements.txt

- Cada una de sus líneas es una dependencia
- Pueden existir diferentes ficheros (el nombre no es obligatorio)
  - Ej: `requirements-dev.txt`
- Se puede crear usando `pip`:
  - `pip freeze > requirements.txt`
- Si el fichero existe se puede usar para instalar todas las dependencias justo depués de haber activado el `venv`
  - `(venv_name) C:\[...]>pip install -r requirements.txt`

### Caso simple

~~~ python
flask
requests
gunicorn
~~~

### Caso con versiones

- Para indicar una versión exacta se usa `==`
  - `flask==1.0.0`
- Para indicar versión dentro de un intervalo
  - `flask>=1.1.2,<2.0`


### Semántica de versiones

- Por convención se suele usar tres números separados por dos puntos
  - Ej: `1.8.2`
    - `1`: Major version
      - Se incrementa cuando hay cambios mayores.
        - Ej: arquitectura
        - Son cambios que hacen que versiones anteriores no vayan a funcionar
    - `8`: Minor version
        - Las nuevas versiones menores no deberían impedir que las anteriores funcionen
      - Se incrementa cuando hay cambios menores.
        - Ej: nuevas características
    - `3`: Patch version
      - Se incrementa cuando se resuelven `bugs`



# Ejemplo de creación y uso desde cmd

## Resumen

~~~ sh

# Ir a carpeta
cd python\flask

# Creación
C:\Users\carlo\AppData\Local\Programs\Python\Python312\python.exe -m venv .venv

# Activación
## Command Prompt
.\.venv\Scripts\activate.bat
## PowerShell
.\.venv\Scripts\Activate

# Comprobación
## Command Prompt
echo %PATH%
## PowerShell
echo $env:PATH

# Desactivación
deactivate

~~~

## Creación

~~~ sh
chdir project_dir
path_to_python_3.3_or_greater/python.exe -m venv .venv
~~~

Una vez creado hay que activarlo para poder usarlo

## Activación

Cuando se activa:

- Se aplican algunos cambios a la cmd actual
  - Activarlo en una cmd no tiene efecto en otras consolas separadas
  - Los paths en el que se buscan los fiheros y aplicaciones cambian
- La consola indica que está usando el venv con el nombre entre paréntesis al inicio de la línea
  - `(venv_name) C:\[...]>`

~~~ sh
source .venv\Scripts\activate.bat
~~~ 

- Si después de activarlo se mira el PATH `echo %PATH%`
  - El primer elemento en el path es a la carpeta `Scripts` del venv

## Uso

- Tanto los comandos de `python` como de `pip` serán los contenidos dentro del `vevn`
- Si se instala una bibloteca, ejemplo `pip install flask`:
  - El ejecutable estará dentro de `.venv\Scripts`
    - Recordar que esa es la primera carpeta dentro del PATH

## Desactivación

Ejecutar:
  - `(venv_name) C:\[...]>deactivate.bat`

# Contenido del venv

Aquí se muestran los componentes principales de la carpeta que contiene al `venv`:

- include
- Lib
- Scripts
  - python.exe
  - pip.exe

## .venv\Scripts\python.exe

- No es el mismo `python.exe` usado para la creación del `vevn`:
  - Es una copia
  - Tiene la misma versión