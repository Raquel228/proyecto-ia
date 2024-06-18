import numpy as np
import random

def objetivo(tablero):
    n = len(tablero)
    conflictos = 0
    for i in range(n):
        for j in range(i + 1, n):
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == j - i:
                conflictos += 1
    return conflictos

def vecino(tablero):
    n = len(tablero)
    i, j = random.sample(range(n), 2)
    nuevo_tablero = tablero.copy()
    nuevo_tablero[i], nuevo_tablero[j] = nuevo_tablero[j], nuevo_tablero[i]
    return nuevo_tablero

def simulated_annealing(n, temperatura_inicial, tasa_enfriamiento):
    tablero = list(range(n))
    random.shuffle(tablero)
    temperatura = temperatura_inicial

    while temperatura > 1:
        nuevo_tablero = vecino(tablero)
        delta = objetivo(nuevo_tablero) - objetivo(tablero)
        if delta < 0 or random.uniform(0, 1) < np.exp(-delta / temperatura):
            tablero = nuevo_tablero
        temperatura *= tasa_enfriamiento

    return tablero, objetivo(tablero)

n = 8
temperatura_inicial = 1000
tasa_enfriamiento = 0.99

solucion, conflictos = simulated_annealing(n, temperatura_inicial, tasa_enfriamiento)
print(f"Solución: {solucion} con {conflictos} conflictos")
