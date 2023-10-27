# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:13:41 2023

@author: Javier
"""

def encadenamiento_hacia_adelante(reglas, hechos_iniciales):
    hechos = hechos_iniciales.copy()
    while True:
        nueva_inferencia = False
        for regla in reglas:
            antecedentes, consecuente = regla
            if all(hecho in hechos for hecho in antecedentes) and consecuente not in hechos:
                hechos.append(consecuente)
                nueva_inferencia = True
                print(f"Inferencia: {', '.join(antecedentes)} => {consecuente}")
        if not nueva_inferencia:
            break
    return hechos

# Reglas: (antecedentes, consecuente)
reglas = [(["lluvia"], "paraguas"), (["sol"], "gafas de sol"), (["viento"], "chaqueta")]
hechos_iniciales = ["lluvia"]

hechos_finales = encadenamiento_hacia_adelante(reglas, hechos_iniciales)
print("Hechos finales:", hechos_finales)