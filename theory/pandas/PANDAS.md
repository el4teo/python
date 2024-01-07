```txt
__________                     ___            
\______   \_____    ____    __| _/____    ______
 |     ___/\__  \  /    \  / __ |\__  \  /  ___/
 |    |     / __ \|   |  \/ /_/ | / __ \_\___ \ 
 |____|    (____  /___|  /\____ |(____  /____  >
                \/     \/      \/     \/     \/ 
```

[BACK](../THEORY.md)

**CONTENIDO**

- [Instalación](#instalación)
- [Ejemplos](#ejemplos)

# Instalación

~~~ python
pip install pandas
~~~

Verificación:

~~~ python
python -c "import pandas as pd; print(pd.__version__)"
~~~

# Ejemplos

```python
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Access and manipulate the data
print(df)
```
