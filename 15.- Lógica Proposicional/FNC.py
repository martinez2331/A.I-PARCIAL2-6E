# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:14:23 2023

@author: Javier
"""

import sympy

# Símbolos
p, q, r = sympy.symbols('p q r')

# Fórmulas
formula1 = (p | q) & (~p | r)
formula2 = (~r | q) & (p | ~q)

# Realizar resolución manualmente
resolvent = sympy.to_cnf(formula1 | formula2, True)
print("Resolución:", resolvent)

# Conversión a Forma Normal Conjuntiva (FNC)
fnc_formula1 = sympy.to_cnf(formula1, True)
fnc_formula2 = sympy.to_cnf(formula2, True)
print("FNC de formula1:", fnc_formula1)
print("FNC de formula2:", fnc_formula2)