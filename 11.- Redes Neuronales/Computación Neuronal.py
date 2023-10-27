# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 23:16:01 2023

@author: bruno
"""

# Importar las bibliotecas necesarias
# Importar las bibliotecas necesarias
import numpy as np
from tensorflow.keras import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Datos de entrada y salida de ejemplo
X = np.array([0, 1, 2, 3, 4, 5])
y = X * 2 + 1  # Una relación simple: y = 2x + 1

# Crear un modelo de red neuronal
model = Sequential()
model.add(Dense(units=1, input_dim=1))  # Una sola neurona con una entrada

# Compilar el modelo
model.compile(loss='mean_squared_error', optimizer='sgd')  # Usamos el error cuadrático medio y el descenso de gradiente estocástico

# Entrenar la red neuronal
model.fit(X, y, epochs=1000)

# Realizar una predicción
x_new = np.array([6])
y_new = model.predict(x_new)
print("Predicción para x = 6:", y_new[0][0])
