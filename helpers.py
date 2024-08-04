import re
import ast

""" obtiene los nombres de los meses """
def get_month_name(x):
     meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
     return meses[x]

""" Normaliza el ordend el df"""

def normalize_df(df_in):
     return df_in[["id","evento","descripcion","fecha","anio","mes","tag","organismo","organismo_tipo","ciudad","nota"]]

"""" Esta función lo que hace es corregir nombres de diferentes tags """
def normalize_tag(tag):
    # limpia el tag
    tag=tag.replace("\'","")
    tag=tag.replace("[","")
    tag=tag.replace("]","")
     # corrije los nombres del tag
    if (tag==""):
        tag="no-especificado"
    elif(tag=="interrupcióndelervicio"):
         tag="dos"
    elif(tag=="cordoba"):
         return False
    elif(tag=="chubut"):
         return False
    elif(tag=="defecement"):
         tag="defacement"
    elif(tag=="rionegro"):
         return False
    elif(tag=="ffaa"):
        return False
    elif(tag=="akira" or tag=="medusa" or tag=="rhysida" or tag=="revil" or tag=="hive" or tag=="play" or tag=="playcript" or tag=="lockbit" or tag=="netwalker" or tag=="egregor"):
     #     Estos son tipos de ransomware que se descartan. Para no modificar las estadísticas. Ya están contados como ransomware
         return False

    return tag

def add_to_tag_unique(tag_list,tag):
    tag=normalize_tag(tag)
    if (tag!=False):
        tag_list.append(tag)
    return tag_list

def get_tag_list_unique(tag_list_original):
     tag_list_clean=list()
     for tag in tag_list_original:
          if ("," in tag):
               # tag=list(tag)
               tag=ast.literal_eval(tag)
               for subtag in tag:
                    tag_list_clean=add_to_tag_unique(tag_list_clean,subtag)
          else:
               tag_list_clean=add_to_tag_unique(tag_list_clean,tag)
     return tag_list_clean

def count_tag_list(tag_list_original):
     tag_list_counter=list()
     for tag in tag_list_original:
          counter=0
          if ("," in tag):
               tag=ast.literal_eval(tag)
               for subtag in tag:
                    counter+=1
          else:
               counter+=1
          tag_list_counter.append(counter)
     return tag_list_counter

# obtiene los hashes de los eventos
def get_hashes(texto):
    # Expresión regular insensible a mayúsculas y minúsculas para buscar palabras que comiencen con #[PALABRA]
    patron = r'#(\w+)'
    # Usamos re.findall para encontrar todas las coincidencias del patrón en el texto
    palabras_encontradas = re.findall(patron, texto, flags=re.IGNORECASE)
    # Convertimos todas las palabras encontradas a minúsculas para uniformidad
    hashes_list = [palabra.lower() for palabra in palabras_encontradas]

    # lo devuelve como un string
    # return ",".join(hashes_list)
    return hashes_list

""" Esta función se utiliza para mostrar los porcentajes en un gráfico """
# EJ: df_tag_grouped.plot.pie(y='tags',autopct=autopct,subplots=True,figsize=(SIZE_X, SIZE_Y),)
def autopct(pct): # only show the label when it's > 10%
    return ('%.2f' % pct) if pct > 10 else ''

""" Agrega el 0 delante del mes """
def agregar_cero_mes(mes):
    # Verificamos si el mes es un número y es menor a 10
    if mes.isdigit() and int(mes) < 10:
        # Añadimos un cero delante y devolvemos el nuevo string
        return mes.zfill(2)
    # Si ya tiene el formato correcto o no es un número, simplemente lo devolvemos
    return mes