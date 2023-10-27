# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:12:53 2023

@author: Javier
"""

import sympy

# Crear símbolos
p, q = sympy.symbols('p q')

# Definir dos fórmulas lógicas
formula1 = (p & q) | (~p)
formula2 = (p | q) & (p >> q)

# Verificar la equivalencia
equivalencia = sympy.Equivalent(formula1, formula2)
print("Equivalencia:", equivalencia)

# Verificar la validez
validez_formula1 = sympy.simplify_logic(formula1)
validez_formula2 = sympy.simplify_logic(formula2)
print("Validez de formula1:", validez_formula1)
print("Validez de formula2:", validez_formula2)

# Verificar satisfacibilidad
satisfacibilidad_formula1 = sympy.satisfiable(formula1)
satisfacibilidad_formula2 = sympy.satisfiable(formula2)
print("Satisfacibilidad de formula1:", satisfacibilidad_formula1)
print("Satisfacibilidad de formula2:", satisfacibilidad_formula2)