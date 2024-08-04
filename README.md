# Script para graficar los ciberincidentes relevantes en Argentina

### Fuente de datos: Timeline realizado por Marcela Pallero
### Fuente de datos: Datos en fuga datosenfuga.org

# instalar

jupyter notebook [tutorial](https://python.land/data-science/jupyter-notebook)

# Instalar
```bash
pip install -r requirements.txt
```

# Instrucciones

Primero que nada descargar las fuentes de datos para poder trabajar con ellas:

[timeline creado por Marcela Pallero](https://time.graphics/es/line/630567)
[Data set de Datos en fuga](https://docs.google.com/spreadsheets/d/1J08Xeu2yuttfuBVT6dFeRCADBe-y9FsOAiqBv74MUAU/edit?gid=1638781659#gid=1638781659)


## Converter

### Timeline de Marcela Pallero

El primero parseará el archivo .xlsx del [timeline creado por Marcela Pallero](https://time.graphics/es/line/630567) y generará un archivo **eventos_procesados_timeline.csv**

**Importante: El archivo descargo debe ser en formato .xlsx y la ubicación por defecto es en la misma carpeta. El nombre puede cambiarse desde el mismo archivo.**

```python
python3 convert_timeline.ipynb
```

### Datosenfuga

El primero parseará el archivo .csv del [Data set de Datos en fuga](https://docs.google.com/spreadsheets/d/1J08Xeu2yuttfuBVT6dFeRCADBe-y9FsOAiqBv74MUAU/edit?gid=1638781659#gid=1638781659) y se guardará en el archivo **eventos_procesados_datosenfuga.csv**

```python
python3 convert_datosenfuga.ipynb
```


## Mezclar los datos

Para mezclar los datos y evitar que haya duplicados deberá realizarse una mezcla de datos. Esto dará como resultado en el archivo **eventos_procesados.csv** para trabajar luego.

```python
python3 merge_data.ipynb
```

## Parser

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

