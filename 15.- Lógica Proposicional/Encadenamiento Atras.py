# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:14:03 2023

@author: Javier
"""

def encadenamiento_hacia_atras(reglas, objetivo):
    def buscar_hechos_consecuentes(reglas, objetivo):
        hechos_consecuentes = []
        for regla in reglas:
            antecedentes, consecuente = regla
            if objetivo == consecuente:
                hechos_consecuentes.extend(antecedentes)
        return hechos_consecuentes

    def demostrar_objetivo(reglas, objetivo, hechos):
        if objetivo in hechos:
            return True
        hechos_consecuentes = buscar_hechos_consecuentes(reglas, objetivo)
        for consecuente in hechos_consecuentes:
            if not demostrar_objetivo(reglas, consecuente, hechos):
                return False
        return True

    hechos = []
    if demostrar_objetivo(reglas, objetivo, hechos):
        return "El objetivo es válido."
    else:
        return "El objetivo no es válido."

# Reglas: (antecedentes, consecuente)
reglas = [(["lluvia"], "paraguas"), (["sol"], "gafas de sol"), (["viento"], "chaqueta")]
objetivo = "chaqueta"

resultado = encadenamiento_hacia_atras(reglas, objetivo)
print(resultado)