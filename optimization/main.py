from AntColony import AntColony
from function import eggholder
import numpy as np
import random

# constantes del problema
LOW, HIGH = -512.0, 512.0  # limites de todas las dimensiones

# constantes del algoritmo gentico
POPULATION_SIZE = 100
MAX_GENERATIONS = 2000
HALL_OF_FAME_SIZE = 30
CROWDING_FACTOR = 20.0


def distance(a, b):
    if (a[0] == b[0] and a[1] == b[1]):
        return np.inf
    return max(eggholder(a[0], a[1]), eggholder(b[0], b[1]))


positions = [(random.uniform(LOW, HIGH), random.uniform(LOW, HIGH))
             for i in range(POPULATION_SIZE)]
# print(positions)
distances = [[distance(positions[i], positions[j])
              for i in range(len(positions))] for j in range(len(positions))]
# print(distances)

ants = AntColony(np.array(distances), 10, 2,
                 MAX_GENERATIONS, 0.5, alpha=20, beta=1)
ants.run()
