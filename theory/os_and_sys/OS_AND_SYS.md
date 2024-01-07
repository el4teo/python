~~~ txt
                                              
  ____  ______            _________ __  ______
 /  _ \/  ___/   ______  /  ___<   |  |/  ___/
(  /_\ )___ \   /_____/  \___ \ \___  |\___ \ 
 \____/____  >          /____  >/ ____/____  >
           \/                \/ \/         \/ 
~~~

[BACK](../THEORY.md)

# os


# sys

## Examples

- Para mirar los paths que python usará para buscar ficheros y aplicaciones
- Los revisa en orden (de izquierda a derecha)
  - Una vez encontrado en algún path deja de buscar en los siguientes
  - Si no es encontrado en ninguno se produce una excepción "no existe"

~~~ python
import sys

print(sys.path)
~~~