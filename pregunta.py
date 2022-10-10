"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
  with open('clusters_report.txt') as report:
    filas = report.readlines()

  filas = filas[4:]

  clusters = []
  cluster = [0, 0, 0, '']

  for fila in filas:
    if re.match('^ +[0-9]+ +', fila):
      numero, cantidad, porcentaje, *palabras = fila.split()
      
      cluster[0] = int(numero)
      cluster[1] = int(cantidad)
      cluster[2] = float(porcentaje.replace(',','.'))

      palabras.pop(0)
      palabras = ' '.join(palabras)
      cluster[3] += palabras

    elif re.match('^ +[a-z]', fila):
      palabras = fila.split()
      palabras = ' '.join(palabras)
      cluster[3] += ' ' + palabras

    elif re.match('^\n', fila) or re.match('^ +$', fila):
      cluster[3] = cluster[3].replace('.', '')
      clusters.append(cluster)
      cluster = [0, 0, 0, '']

  df = pd.DataFrame (clusters, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
  return df
