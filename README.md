# Script para graficar los ciberincidentes relevantes en Argentina

### Fuente de datos: Timeline realizado por Marcela Pallero

# instalar

jupyter notebook [tutorial](https://python.land/data-science/jupyter-notebook)

# Instalar
```bash
pip install -r requirements.txt
```

# Uso

Para utilizar esto hay que correr dos scripts.

## Parser

El primero parseará el archivo .xlsx del [timeline creado por Marcela Pallero](https://time.graphics/es/line/630567) y generará un archivo **eventos_procesados.csv**

## Importante:

El archivo descargo debe ser en formato .xlsx y la ubicación por defecto es en la misma carpeta. El nombre puede cambiarse desde el mismo archivo.

```python
python3 convert.ipynb
```
## Visualizador

Una vez creado ese archivo entonces se procede a parsearlo para ver los resultados

```python
python3 parse_events.ipynb
```

# Exportar

Con Jupyter se puede exportar a un archivo .html o pdf

# Ejemplo

Puede verse un [ejemplo de los datos reflejados](export_example.html)

# Referencias de pandas

(Tutorial de pandas)[https://www.datacamp.com/es/tutorial/pandas]
(Ayuda y tutoriales de panda)[https://joserzapata.github.io/courses/python-ciencia-datos/pandas]

