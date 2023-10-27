# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:11:38 2023

@author: Javier
"""

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

def es_seguro(tablero, fila, columna):
    # Verificar si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i][columna] == 'Q':
            return False

    # Verificar la diagonal superior izquierda
    i, j = fila, columna
    while i >= 0 and j >= 0:
        if tablero[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Verificar la diagonal superior derecha
    i, j = fila, columna
    while i >= 0 and j < N:
        if tablero[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def resolver_n_reinas(tablero, fila):
    if fila == N:
        imprimir_tablero(tablero)
        return True

    for columna in range(N):
        if es_seguro(tablero, fila, columna):
            tablero[fila][columna] = 'Q'
            if resolver_n_reinas(tablero, fila + 1):
                return True
            tablero[fila][columna] = '.'

    return False

N = 8  # Número de reinas y tamaño del tablero
tablero = [['.' for _ in range(N)] for _ in range(N)]

if resolver_n_reinas(tablero, 0):
    print("Solución encontrada:")
    imprimir_tablero(tablero)
else:
    print("No se encontró solución.")