# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:12:26 2023

@author: Javier
"""

import random

# Función objetivo unidimensional (puede ser reemplazada por cualquier otra función)
def funcion_objetivo(x):
    return -(x ** 2)

def hill_climbing(funcion_objetivo, limite_iteraciones, paso_inicial, paso_maximo):
    x = random.uniform(-paso_inicial, paso_inicial)
    valor_actual = funcion_objetivo(x)
    for _ in range(limite_iteraciones):
        paso = random.uniform(-paso_maximo, paso_maximo)
        nuevo_x = x + paso
        nuevo_valor = funcion_objetivo(nuevo_x)
        if nuevo_valor > valor_actual:
            x = nuevo_x
            valor_actual = nuevo_valor
    return x, valor_actual

limite_iteraciones = 1000
paso_inicial = 0.1
paso_maximo = 0.01

mejor_x, mejor_valor = hill_climbing(funcion_objetivo, limite_iteraciones, paso_inicial, paso_maximo)

print(f"El máximo local se encuentra en x = {mejor_x}")
print(f"El valor máximo es {mejor_valor}")