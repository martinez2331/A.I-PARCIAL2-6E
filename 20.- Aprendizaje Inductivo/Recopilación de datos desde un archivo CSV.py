# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:55:45 2023

@author: PC
"""

import csv

# Abre el archivo CSV en modo de lectura
with open('datos.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    
    # Itera a través de las filas del archivo CSV
    for fila in lector_csv:
        # Accede a los datos de cada fila, por ejemplo, fila[0] es el primer elemento de la fila
        print(fila)
