# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:14:45 2023

@author: Javier
"""

def llevar_paraguas(clima, pronostico_lluvia):
    # Reglas lógicas
    if clima == "lluvia" or pronostico_lluvia == "lluvia":
        return "Lleva un paraguas"
    else:
        return "No lleves un paraguas"

# Datos de entrada
clima_actual = "soleado"
pronostico_lluvia_hoy = "lluvia"

# Realiza una inferencia basada en las reglas lógicas
recomendacion = llevar_paraguas(clima_actual, pronostico_lluvia_hoy)

# Imprime la recomendación
print(recomendacion)