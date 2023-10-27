# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:57:43 2023

@author: PC
"""

import requests

# URL de la API a la que deseas acceder
url = 'https://api.ejemplo.com/datos'

# Realiza una solicitud GET a la API
respuesta = requests.get(url)

# Verifica si la solicitud fue exitosa
if respuesta.status_code == 200:
    # Convierte la respuesta JSON en un diccionario de Python (si la respuesta es JSON)
    datos = respuesta.json()
    
    # Puedes acceder a los datos según la estructura proporcionada por la API
    print(datos)
else:
    print("Error al realizar la solicitud a la API")
