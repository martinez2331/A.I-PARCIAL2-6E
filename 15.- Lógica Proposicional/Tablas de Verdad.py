# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:15:04 2023

@author: Javier
"""

# Función para la operación AND
def logical_and(a, b):
    return a and b

# Función para la operación OR
def logical_or(a, b):
    return a or b

# Función para la operación NOT
def logical_not(a):
    return not a

# Imprime la tabla de verdad para AND, OR y NOT
def print_truth_table():
    print("Tabla de verdad para AND:")
    print("A     B     Resultado")
    for a in [False, True]:
        for b in [False, True]:
            result = logical_and(a, b)
            print(f"{a}  and  {b}  =>  {result}")

    print("\nTabla de verdad para OR:")
    print("A     B     Resultado")
    for a in [False, True]:
        for b in [False, True]:
            result = logical_or(a, b)
            print(f"{a}   or   {b}  =>  {result}")

    print("\nTabla de verdad para NOT:")
    print("A     Resultado")
    for a in [False, True]:
        result = logical_not(a)
        print(f"not  {a}  =>  {result}")

print_truth_table()